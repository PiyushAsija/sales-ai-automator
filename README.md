# AI Sales Insight Automator

## Overview

AI Sales Insight Automator is a full-stack application that analyzes sales CSV datasets using AI and automatically emails a professional summary report.

The system allows users to upload a CSV file containing sales data and receive AI-generated insights such as:

* Top performing product categories
* Regional performance
* Revenue highlights
* Key trends

## Architecture

Frontend:

* React (Vite)
* Axios for API calls

Backend:

* FastAPI
* Pandas for CSV processing
* Gemini AI for generating insights
* SMTP for sending email reports

Infrastructure / DevOps:

* Docker
* Docker Compose
* GitHub
* CI/CD (GitHub Actions)

## Project Structure

sales-ai-automator/
├── backend
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend
│   └── vite-project
│       ├── src
│       └── package.json
│
└── docker-compose.yml

## Features

* Upload CSV sales dataset
* AI powered data analysis
* Automatic summary generation
* Email delivery of insights
* REST API documentation with Swagger
* Docker containerization
* CI/CD pipeline

## Running Locally

Start backend:

```
cd backend
python -m uvicorn main:app --reload
```

Start frontend:

```
cd frontend/vite-project
npm install
npm run dev
```

Open browser:

```
http://localhost:5173
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Environment Variables

Create `.env` in backend folder:

```
GEMINI_API_KEY=your_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

## Docker Run

```
docker-compose up --build
```

## Author

Piyush Asija
