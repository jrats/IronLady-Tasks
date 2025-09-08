Employee CRUD with Sentiment Analysis 🚀

This is a FastAPI-based CRUD application for managing employees.
It comes with an AI-powered sentiment analysis feature using NLTK VADER, which analyzes employee feedback as positive, negative, or neutral.

------------------------------------------------------------------

🛠️ Tools & Tech Stack Used

FastAPI
 → Web framework for APIs

Uvicorn
 → ASGI server for running FastAPI

SQLite
 → Lightweight database

SQLAlchemy
 → ORM for database interaction

Pydantic
 → Data validation and serialization

NLTK
 → Natural Language Toolkit (for sentiment analysis)

VADER Sentiment Analyzer used to classify text as positive, negative, or neutral

------------------------------------------------------------------

📂 Project Structure

.
├── main.py          # FastAPI app entry point
├── crud.py          # CRUD logic + sentiment analysis
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── database.py      # DB connection setup
├── requirements.txt # Dependencies
└── README.md        # Project documentation

------------------------------------------------------------------

▶️ How to Run the Code
1. Clone this repository

git clone https://github.com/your-username/employee-crud-sentiment.git
cd employee-crud-sentiment

2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the FastAPI server
uvicorn main:app --reload

5. Open the Swagger UI

Go to 👉 http://127.0.0.1:8000/docs
 in your browser.
 
------------------------------------------------------------------

 🧪 Example Request
Create an Employee

POST /employees/

{
  "name": "Ram",
  "email": "ram@example.com",
  "feedback": "I like the company culture."
}

Example Response
{
  "id": 1,
  "name": "Ram",
  "email": "ram@example.com",
  "feedback": "I like the company culture.",
  "sentiment": "positive"
}

------------------------------------------------------------------