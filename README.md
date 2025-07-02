---
title: FastAPI + Streamlit Task App (Personal Course Tutorial)
description: Build FastAPI backends and Streamlit dashboards practically and efficiently.
---

#  FastAPI + Streamlit Task App

This repository is part of **my personal course tutorials** teaching **FastAPI** and **Streamlit** to build clean, practical Python web applications.

It demonstrates:

- ✅ **FastAPI** for CRUD APIs with Pydantic validation and SQLAlchemy ORM.
- ✅ **Streamlit** for lightweight, interactive dashboards without heavy frontends.
- ✅ Clean project structuring for rapid prototyping and scalable learning.

---

##  Features

- Task management: **Create, Read, Update, Delete (CRUD)**.
- Streamlit dashboard:
  - View tasks in a clean table.
  - Create, update, delete tasks with live refresh.
- Uses SQLite for local lightweight storage.
- Clean, scalable, beginner-friendly codebase.

---

## 🛠 Installation

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-streamlit-tutorial.git
cd fastapi-streamlit-tutorial

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

---

## Running the Application

### 1️⃣ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 2️⃣ Run Streamlit Frontend

In a new terminal:

```bash
streamlit run frontend.py
```

- Dashboard: [http://localhost:8501](http://localhost:8501)

---

##  Project Structure

```
.
├── main.py              # FastAPI backend
├── frontend.py          # Streamlit dashboard
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── crud.py              # CRUD utilities
├── database.py          # DB configuration
├── config.py            # Environment settings
├── requirements.txt     # Dependencies
└── .gitignore           # Ignore rules
```

---

##  Purpose

This project is designed for **my FastAPI + Streamlit course tutorials** to help learners:

✅ Build CRUD APIs confidently with FastAPI.  
✅ Create dashboards using Streamlit easily.  
✅ Understand clean architecture for backend + frontend using Python only.  
✅ Prepare for scalable, professional Python projects and interviews.

---

## Next Learning Steps

- JWT Authentication with FastAPI.
- Deployment to Render/AWS.
- Using Postgres for production apps.
- Advanced dashboards with Streamlit and plotting libraries.

---

## ✨ License

MIT License.

---

> **Follow my course series to learn FastAPI and modern Python backend development practically and efficiently.**
