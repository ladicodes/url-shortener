🔗 URL Shortener

A lightweight and efficient URL shortening service built with Django — designed to turn long, cluttered links into short, trackable URLs in seconds.

✨ Overview

This project simplifies link sharing while offering useful insights.
Users can create short links, view their history, and track how many times each link has been clicked — all through a clean, intuitive interface.

⚙️ Tech Stack

Backend: Django (Python)

Database: SQLite

Frontend: HTML, CSS

Utilities: Random string generation for unique short IDs

🚀 Getting Started

Clone the repository and run locally 👇

git clone https://github.com/<your-username>/url-shortener.git

cd url-shortener

python -m venv venv

venv\Scripts\activate   # For Windows

# source venv/bin/activate   # For Mac/Linux

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


Then open your browser and visit:

👉 http://127.0.0.1:8000/

💡 Features

✅ Generate short links automatically
✅ Redirect users seamlessly to original URLs
✅ Track link clicks in real time
✅ View all shortened links in a simple dashboard
