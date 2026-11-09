from fastapi import FastAPI
from pydantic import BaseModel
from io import BytesIO

from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader

app = FastAPI(
    title="ResumeIQ",
    description="AI-Powered ATS Resume Analyzer and Tracker",
    version="1.0.0"
)
# Home
@app.get("/")
def home():
    return {
        "project": "AI Career Companion & ATS Resume Analyzer"
    }

# ATS Score
@app.post("/ats-score")
def ats_score(data: dict):

    skills = len(data.get("skills", []))
    projects = data.get("projects", 0)

    score = 0

    if skills >= 5:
        score += 50

    if projects >= 2:
        score += 30

    score += 20

    return {
        "ats_score": score
    }

# Resume Analysis
@app.post("/resume-analysis")
def resume_analysis(data: dict):

    skills = len(data.get("skills", []))
    projects = data.get("projects", 0)
    certifications = data.get("certifications", 0)

    strengths = []
    weaknesses = []
    suggestions = []

    if skills >= 5:
        strengths.append("Strong Technical Skills")
    else:
        weaknesses.append("Lack of Technical Skills")
        suggestions.append("Learn FastAPI, SQL and Git")

    if projects >= 2:
        strengths.append("Good Project Experience")
    else:
        weaknesses.append("Need More Projects")
        suggestions.append("Build 2 more Projects")

    if certifications >= 1:
        strengths.append("Has Certifications")
    else:
        weaknesses.append("No Certifications")
        suggestions.append("Complete Python Certification")

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }

# Interview Questions
@app.post("/interview-questions")
def interview_questions(data: dict):

    skill = data.get("skill")

    if skill == "Python":
        return {
            "questions": [
                "What is OOP?",
                "What is Inheritance?",
                "What is Polymorphism?",
                "Difference between List and Tuple?"
            ]
        }

    if skill == "MongoDB":
        return {
            "questions": [
                "What is MongoDB?",
                "What is Collection?",
                "What is Document?",
                "What is MongoDB Atlas?"
            ]
        }

    return {
        "questions": [
            "No Questions Available"
        ]
    }

# Career Roadmap
@app.post("/career-roadmap")
def career_roadmap(data: dict):

    role = data.get("role")

    if role == "Data Scientist":
        return {
            "skills": [
                "Python",
                "SQL",
                "Machine Learning",
                "Statistics"
            ],
            "projects": [
                "House Price Prediction",
                "Movie Recommendation",
                "Customer Churn Prediction"
            ]
        }

    if role == "Backend Developer":
        return {
            "skills": [
                "Python",
                "FastAPI",
                "MongoDB",
                "Git"
            ],
            "projects": [
                "ATS Resume Builder",
                "E-Commerce API",
                "Hospital Management System"
            ]
        }

    return {
        "message": "Role Not Found"
    }

# Missing Skills
@app.post("/missing-skills")
def missing_skills(data: dict):

    role = data.get("role")
    skills = data.get("skills", [])

    role_skills = {
        "Backend Developer":
        ["Python", "FastAPI", "MongoDB", "Git"],

        "Data Scientist":
        ["Python", "SQL",
         "Machine Learning", "Statistics"]
    }

    required = role_skills.get(role, [])

    missing = []

    for skill in required:
        if skill not in skills:
            missing.append(skill)

    return {
        "missing_skills": missing
    }

# Resume Rating
@app.post("/resume-rating")
def resume_rating(data: dict):

    score = data.get("ats_score", 0)

    if score >= 80:
        rating = "Excellent"
    elif score >= 60:
        rating = "Good"
    else:
        rating = "Needs Improvement"

    return {
        "rating": rating
    }

# Project Recommendations
@app.post("/project-recommendation")
def project_recommendation(data: dict):

    role = data.get("role")

    if role == "Backend Developer":
        return {
            "projects": [
                "ATS Resume Builder",
                "E-Commerce Backend",
                "Hospital Management API"
            ]
        }

    if role == "Data Scientist":
        return {
            "projects": [
                "House Price Prediction",
                "Movie Recommender",
                "Customer Churn Prediction"
            ]
        }

    return {"projects": []}

# Certification Suggestions
@app.post("/certifications")
def certifications(data: dict):

    role = data.get("role")

    if role == "Data Scientist":
        return {
            "certifications": [
                "IBM Data Science",
                "Google Data Analytics",
                "Machine Learning Specialization"
            ]
        }

    return {
        "certifications": [
            "Python Certification",
            "MongoDB Associate",
            "AWS Cloud Practitioner"
        ]
    }

# Salary Predictor
@app.post("/salary-prediction")
def salary_prediction(data: dict):

    skills = len(data.get("skills", []))

    if skills >= 6:
        salary = "8-12 LPA"

    elif skills >= 4:
        salary = "5-8 LPA"

    else:
        salary = "3-5 LPA"

    return {
        "estimated_salary": salary
    }

#@app.post("/upload-resume")
#async def upload_resume(file: UploadFile = File(...)):
    #return {
       # "filename": file.filename,
        #"message": "Resume Uploaded Successfully"
    #}

#@app.post("/upload-resume")
#async def upload_resume(file: UploadFile = File(...)):

    #return {
        #"filename": file.filename,
        #"message": "Resume Uploaded Successfully"
   # }
@app.post("/ai-resume-review")
async def review_resume(
    resume: UploadFile = File(...),
    job_description: str = Form("")
):
    if resume.filename.endswith(".pdf"):
        pdf = PdfReader(BytesIO(await resume.read()))
        text = "\n".join(
            page.extract_text() or "" for page in pdf.pages
        )
    else:
        return {"error": "Please upload a PDF resume"}

    if not text.strip():
        return {"error": "Could not extract resume text"}

    sections = ["education", "skills", "projects", "experience"]
    found = [s for s in sections if s in text.lower()]

    score = int((len(found) / len(sections)) * 100)

    return {
        "filename": resume.filename,
        "ats_score": score,
        "sections_found": found,
        "missing_sections": [
            s for s in sections if s not in found
        ],
        "recommendation": "Improve missing resume sections."
    }
class ChatRequest(BaseModel):
    question: str

@app.post("/career-chatbot")
def career_chatbot(data: ChatRequest):

    q = data.question.lower()

    if "career" in q:
        answer = "Learn DSA, Python, SQL and build projects."
    elif "job" in q:
        answer = "Prepare your resume, practice interviews and apply for jobs."
    elif "skills" in q:
        answer = "Learn Python, Java, DSA, DBMS and communication skills."
    elif "internship" in q:
        answer = "Build projects, improve GitHub and apply for internships."
    elif "salary" in q:
        answer = "Salary depends on skills, experience and company."
    else:
        answer = "I can help with career, jobs, skills, internships and salary."

    return {"answer": answer}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/test")
def test():
    return {"message": "Frontend connected successfully!"}
from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    skills: str

@app.post("/resume")
def create_resume(resume: Resume):
    return {
        "message": "Resume received successfully!",
        "name": resume.name,
        "email": resume.email,
        "skills": resume.skills
    }