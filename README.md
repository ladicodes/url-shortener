URL Shortener 

A fast and simple URL shortening app built with Django. Turn long, messy links into short, shareable URLs in seconds—and track how many times each link is clicked.

Features

Generate unique short URLs from long URLs

Redirect short URLs to the original link

Track clicks for every link

Clean, minimal web interface

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Quick Start
git clone <repo-url>
cd url-shortener
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Open http://127.0.0.1:8000/ and start shortening URLs!
