import os
import json
from flask import Flask, request, jsonify, send_file, render_template
from pymongo import MongoClient
import PyPDF2

app = Flask(__name__)

# -------------------- PATHS --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

# -------------------- DATABASE --------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["ResumeSkillGapAnalyzer"]
collection = db["analysis"]

# -------------------- SKILLS --------------------
ROLE_SKILLS = {
    "data-scientist": ["Python", "Statistics", "Machine Learning", "Pandas", "NumPy", "SQL"],
    "ml-engineer": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning"],
    "software-engineer": ["Python", "Java", "DSA", "OOP", "Git"],
    "web-developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "data-analyst": ["Python", "Excel", "SQL", "Power BI", "Statistics"],
    "ai-researcher": ["Python", "Deep Learning", "Research", "Math", "Neural Networks"]
}

# -------------------- HOME --------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------- ANALYZE --------------------
@app.route("/analyze", methods=["POST"])
def analyze_resume():

    if "file" not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    resume_file = request.files["file"]
    role = request.form.get("role")

    if resume_file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    if not role:
        return jsonify({"error": "No job role selected"}), 400

    # Save resume
    file_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
    resume_file.save(file_path)

    # Read PDF
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""

    text = text.lower()

    required = ROLE_SKILLS.get(role, [])
    matching = [s for s in required if s.lower() in text]
    missing = [s for s in required if s not in matching]

    skill_match = int((len(matching) / len(required)) * 100) if required else 0

    result = {
        "role": role,
        "matchingSkills": matching,
        "missingSkills": missing,
        "skillMatch": skill_match
    }

    # Insert into MongoDB
    inserted = collection.insert_one(result)

    # ✅ REMOVE MongoDB _id BEFORE JSON
    result.pop("_id", None)

    report_data = {
        "record_id": str(inserted.inserted_id),
        "role": role,
        "matchingSkills": matching,
        "missingSkills": missing,
        "skillMatch": skill_match
    }

    # Save JSON report
    report_path = os.path.join(REPORT_FOLDER, "resume_report.json")
    with open(report_path, "w") as f:
        json.dump(report_data, f, indent=4)

    return jsonify(result)

# -------------------- DOWNLOAD --------------------
@app.route("/download")
def download():
    return send_file(
        os.path.join(REPORT_FOLDER, "resume_report.json"),
        as_attachment=True
    )

# -------------------- SHARE --------------------
@app.route("/share")
def share():
    return jsonify({"message": "Results shared successfully (simulation)"})

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
