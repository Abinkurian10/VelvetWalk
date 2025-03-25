# VelvetWalk - Shoe Blog Platform

A Django-based blog platform for shoe enthusiasts to share their thoughts, reviews, and experiences.

## Features
- User authentication and profiles
- Blog post creation and management
- Profile editing
- Public blog post viewing
- Image upload support

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv shoevenv
source shoevenv/bin/activate  # On Windows: shoevenv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the site. 