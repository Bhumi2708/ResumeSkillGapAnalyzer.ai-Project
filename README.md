# Resume Skill Gap Analyzer

**Project Type:** Web-based Python Project (Flask + MongoDB)  
**Developer:** Bhumika Sham Gujar  
**Branch:** main  

---

## **Project Overview**

The Resume Skill Gap Analyzer is a web application that allows users to upload their resumes and identify missing skills for a specific job role. The system analyzes the resume content (PDF/DOCX), compares it with predefined skills stored in MongoDB, and displays **matched skills** and **missing skills**. This helps students, freshers, and professionals understand which skills they need to improve for their desired job.

---

## **Features**

- Upload resumes in **PDF** or **DOCX** format  
- Select a **job role** from the dropdown menu  
- View **matched skills** (highlighted in green)  
- View **missing skills** (highlighted in red)  
- Store analysis results in **MongoDB** for record keeping  
- Clean, attractive, and responsive UI  

---

## **Technologies Used**

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Backend web framework |
| MongoDB | NoSQL database for storing job roles and analysis results |
| PDFMiner | Extract text from PDF resumes |
| python-docx | Extract text from DOCX resumes |
| HTML & CSS | Frontend UI design |
| Jinja2 | Dynamic HTML templating |

---

## System Requirements

**Hardware:**
- Processor: Intel Core i3 or higher  
- RAM: 4 GB or higher  
- Hard Disk: 20 GB free space  
- Input Devices: Keyboard, Mouse  
- Internet: Required for web access  

**Software:**
- Python 3.x  
- Anaconda (Spyder IDE recommended)  
- MongoDB Community Server  
- Web Browser (Chrome, Edge, Firefox)  

---

## **Installation & Setup**

1. **Clone the repositor:**
```bash
git clone https://github.com/<your-username>/ResumeSkillGapAnalyzer.git
Navigate to project folder:

cd ResumeSkillGapAnalyzer


Install required libraries:

pip install flask pymongo pdfminer.six python-docx


Start MongoDB
Make sure MongoDB server is running on localhost:27017.

Run the Flask app:

python app.py


Open the application in your browser:

http://127.0.0.1:5000

Usage Instructions

Open the web application in your browser.

Upload your resume (PDF or DOCX).

Select a job role from the dropdown menu.

Click the Analyze Resume button.

View matched skills (green) and missing skills (red).

Optional: Check the uploads folder for saved resume files.

Screenshots

You can add screenshots here to make your repo more attractive




Limitations

Cannot analyze scanned or image-based resumes

Supports limited predefined job roles

Matching is keyword-based, not context-based

No advanced NLP or AI scoring yet

Future Enhancements

Add more job roles and skill sets dynamically

Use NLP/ML models for intelligent skill matching

Provide skill improvement suggestions

Generate graphical reports and charts

License

This project is open-source and free to use for educational purposes.

Contact

Developer: Bhumika Sham Gujar
Email: [your-email@example.com
]
LinkedIn: https://www.linkedin.com/in/bhumika-gujar
