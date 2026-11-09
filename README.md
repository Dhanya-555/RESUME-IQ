# ResumeIQ

AI-powered ATS resume analyzer built with FastAPI. Upload a PDF resume and get an ATS score, skill gap analysis, interview questions, and career guidance.

## Features

- ATS score for a resume against a job description
- Resume analysis and rating
- Missing skills detection
- Interview question generation
- Career roadmap
- Project and certification recommendations
- Salary prediction
- AI resume review

## Tech Stack

- Python
- FastAPI and Uvicorn
- PdfReader for PDF text extraction
- Swagger UI for interactive API docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /ats-score | ATS score for a resume |
| POST | /resume-analysis | Detailed resume analysis |
| POST | /interview-questions | Likely interview questions |
| POST | /career-roadmap | Suggested career path |
| POST | /missing-skills | Skills missing for a role |
| POST | /resume-rating | Overall resume rating |
| POST | /project-recommendation | Project ideas |
| POST | /certifications | Recommended certifications |
| POST | /salary-prediction | Salary estimate |
| POST | /ai-resume-review | AI feedback (PDF + optional job description) |

## Setup

1. Clone the repo

    git clone https://github.com/Dhanya-555/RESUME-IQ.git
    cd RESUME-IQ/backend

2. Install dependencies

    pip install -r requirements.txt

3. Create a `.env` file in the backend folder with your API key

    API_KEY=your_key_here

4. Run the server

    uvicorn main:app --reload

5. Open http://127.0.0.1:8000/docs to try the API.

## Screenshots

Add a screenshot of the Swagger UI here.

## Future Improvements

- Frontend dashboard
- Resume tracking history
- Deployment on Render or Railway

## Author

Dhanya
LinkedIn: your-linkedin-link