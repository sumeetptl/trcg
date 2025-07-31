# RealCryptoG Django Backend Documentation

## Overview

This Django backend powers the RealCryptoG platform. It supports:

* JWT-based authentication
* Role-based permissions (admin, free, premium)
* Blog and signal management
* Secure API endpoints for frontend consumption

---

## Project Structure

```
backend/
├── config/             # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/              # Custom user app
│   ├── models.py       # Custom User model with roles
│   ├── views.py        # Registration view
│   ├── serializers.py
│   └── urls.py         # /auth/token/, /auth/register/
├── blogs/              # Blog content
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py         # /blogs/
├── signals/            # Trading signals
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py         # /signals/
├── media/              # Image storage (Cloudinary or local fallback)
├── requirements.txt
├── .env                # Secret keys and DB config
└── manage.py
```

---

## Models

### User (custom)

* `username`, `email`, `password`
* `role`: free | premium | admin

### Blog

* `title`, `content`, `image`, `created_at`, `author`

### Signal

* `coin`, `direction`, `entry_price`, `leverage`
* `targets`: JSON (e.g. {"45000": "pending"})
* `stop_loss`, `status`: pending/success/fail
* `created_by`, `created_at`

---

## Authentication (JWT)

### Endpoints:

* `POST /api/auth/register/` – creates a user (free by default)
* `POST /api/auth/token/` – returns JWT access & refresh tokens
* `POST /api/auth/token/refresh/` – refreshes JWT access token

---

## API Endpoints

### Blogs (public read, admin write)

* `GET /api/blogs/` – list all blogs
* `POST /api/blogs/` – admin only

### Signals

* `GET /api/signals/` – all users (blurred for free)
* `POST /api/signals/` – admin only

---

## Permissions

* `IsAdminUserRole`: Custom permission class for admin-only access
* Free users have read-only access with field-level data restrictions

---

## Blurred Logic (Free Users)

In `SignalSerializer.to_representation()`:

```python
if user.role == 'free':
  rep['targets'] = '🔒 Upgrade to Premium'
  rep['stop_loss'] = '🔒 Upgrade to Premium'
```

---

## Deployment Suggestions

* Host on **Render**, **Railway**, or **Fly.io**
* Store secrets in `.env`
* Use **Gunicorn** for production WSGI

---

## Swagger Docs

* `/api/docs/` – Swagger UI
* `/api/schema/` – OpenAPI schema

---

## Local Dev

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Testing

```bash
python manage.py test
```

Includes tests for:

* Auth token flow
* Signal access (role-based)
* Blog posting

---

## Contact

For questions or contributions, please contact the developer or file an issue on GitHub.
