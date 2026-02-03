# blogproject - Django Blog

This repository contains a simple Django blog project built for learning and demonstration purposes.

## Features
- User authentication (signup, login)
- Create, edit and delete posts
- Categories, tags, contact form, and newsletter
- Image uploads for posts (media/ and posts/ directories)

## Prerequisites
- Python 3.8+ (use your virtual environment)
- pip
- (Optional) MySQL if configured — install `mysqlclient` or use SQLite

## Setup (local)
1. Create and activate a virtual environment:

	python -m venv venv
	venv\Scripts\activate

2. Install dependencies:

	pip install -r requirements.txt

	(If `requirements.txt` is not present, install Django and any DB clients: `pip install django mysqlclient`)

3. Apply migrations and create a superuser:

	python manage.py migrate
	python manage.py createsuperuser

4. Collect static files (for production) and run the development server:

	python manage.py runserver

5. Open http://127.0.0.1:8000/ in your browser.

## Media files
Uploaded images are expected in the `media/` and `posts/` directories. Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in `blogproject/settings.py`.

## Notes
- The project uses Django's built-in auth system. Templates are in `blog/templates/`.
- If you plan to deploy, configure allowed hosts, static files, and secure settings (secret key, DEBUG).

## Repository
The project is hosted at: https://github.com/SupriyaSandipShelke/blogproject-Django-Framework.git

## License
This project is provided as-is for learning. Add a license if you plan to reuse or share it.

---
Updated README and pushed to the `main` branch.