# 🤖 TalentScout Hiring Assistant

## 📌 Overview

TalentScout is an AI-powered Hiring Assistant chatbot built with **Streamlit** that helps recruitment teams conduct initial screening of candidates. It collects essential candidate details and automatically generates 5 relevant technical interview questions based on the candidate’s declared tech stack. This project was developed as part of the AI/ML Intern Assignment.

---

## 🚀 Features

- 🎯 Candidate information intake (Name, Email, Phone, Experience, Role, Tech Stack)
- 🧠 Automatic generation of **tech stack-based technical questions**
- 💾 Candidate data stored to a local CSV file
- ✅ Works completely **offline** (no API key or internet required)
- 🔄 Restart flow to handle multiple candidates
- 📦 Clean and user-friendly Streamlit interface

---

## 🖥️ Tech Stack

- **Python**
- **Streamlit** – for building the web interface
- **Pandas** – for handling and storing candidate data
- **Local Logic** – for generating placeholder technical questions without using external APIs (OpenAI, Hugging Face, Ollama, etc.)

---

## 📂 Project Structure


talentscout_chatbot/
│
├── app.py # Main Streamlit application
├── candidate_data.csv # Auto-generated: stores candidate submissions
├── requirements.txt # List of Python dependencies
└── README.md # Project overview and instructions

pip install -r requirements.txt
streamlit run app.py


