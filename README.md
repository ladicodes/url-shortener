# 🔗 URL Shortener

A lightweight, efficient **URL shortening service** built with **Django** — designed to turn long, cluttered links into short, trackable ones in seconds.

---

## ✨ Overview

Tired of messy links?  
This project transforms long URLs into short, clean, and shareable links — while tracking how many times each one is clicked.  
Fast, simple, and a great way to learn backend logic and database handling with Django.

---

## ⚙️ Tech Stack

- **Backend:** Django (Python)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS  
- **Utilities:** Random string generation for unique short IDs  

---

## 🚀 Getting Started

Clone this repository and set it up locally 👇  

```bash
git clone https://github.com/<your-username>/url-shortener.git
```
```bash
cd url-shortener
```
python -m venv venv
venv\Scripts\activate     # For Windows
# source venv/bin/activate   # For Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Now visit 👉 http://127.0.0.1:8000/ to try it out!
