# SPEC-1-The Real Crypto G

## Background

“The Real Crypto G” is a personal product focused on helping beginner to intermediate crypto enthusiasts by offering clear education, actionable market signals, and simple dashboards. The product emphasizes authentic, real-world crypto experience — not hype — and aims to provide real value to users who often get lost in the noise of crypto Twitter, Reddit, and trading forums.

## Requirements

### Must Have

* User Authentication (Signup/Login/Logout)
* User Roles: Admin, Free, Premium
* Admin Dashboard:

  * Manage users (view, promote, delete)
  * Post crypto signals (with result status updates: pending/success/fail)
  * Post blog content (educational or analytical)
* End-User Features:

  * View blog posts (Free for all)
  * View signal feed:

    * Premium users: Full access to current/upcoming signals
    * Free users: Limited/blurred signal access
* Basic UI/UX for mobile and desktop usability

### Should Have

* Payment Integration (for Premium user subscription model — future)
* Signal performance dashboard (summary of signal outcomes over time)

### Could Have

* Bookmark or Save feature for blogs/signals
* Notifications (when a new signal is posted)

### Won’t Have (for MVP)

* Trading bots or exchange integration
* Real-time price charts/technical indicators

## Method

### Architecture Overview

**Stack**

* Frontend: React + Next.js (responsive)
* Backend: Django + Django REST Framework
* Database: PostgreSQL
* Auth: JWT via djangorestframework-simplejwt
* File Storage: Cloudinary (for images)
* Hosting: Vercel (frontend), Render or Railway (backend)

**Architecture Diagram**

```plantuml
@startuml

actor "Visitor" as Visitor
actor "Free User" as FreeUser
actor "Premium User" as PremiumUser
actor "Admin" as Admin

rectangle "Frontend (Next.js)" {
  Visitor --> (Signup/Login Page)
  FreeUser --> (Blog Feed)
  FreeUser --> (Signal Feed - Limited)
  PremiumUser --> (Signal Feed - Full)
  Admin --> (Admin Dashboard UI)
}

rectangle "Backend (Django + DRF)" {
  (Auth API)
  (User API)
  (Blog API)
  (Signal API)
  (Role & Permission Middleware)
  Admin --> (Django Admin Panel)
}

rectangle "Database (PostgreSQL)" {
  (User Table)
  (Blog Table)
  (Signal Table)
  (Roles)
}

rectangle "File Storage (Cloudinary)" {
  (Blog Images)
}

@enduml
```

### Database Schema

**User**

```python
class User(AbstractUser):
    ROLE_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='free')
```

**Signal**

```python
class Signal(models.Model):
    coin = models.CharField(max_length=10)
    direction = models.CharField(max_length=5)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    leverage = models.PositiveSmallIntegerField()
    targets = models.JSONField()  # e.g. {"42000": "pending", "45000": "hit"}
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
```

**Blog**

```python
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
```

### API Endpoints

**Authentication**

* `POST /api/register/`
* `POST /api/token/`
* `POST /api/token/refresh/`

**Signal API**

* `GET /api/signals/` (Free/Premium access logic)
* `GET /api/signals/<id>/`
* `POST /api/signals/` (Admin only)
* `PATCH /api/signals/<id>/` (Admin only)

**Blog API**

* `GET /api/blogs/`
* `GET /api/blogs/<id>/`
* `POST /api/blogs/` (Admin only)

### Access Logic (Frontend)

* Free users see coin, direction, entry; targets and stop loss are blurred
* Premium users see all fields

## Implementation

1. Set up Django + PostgreSQL backend
2. Implement custom User model and REST API for Blog & Signal
3. Set up JWT authentication
4. Use Django Admin for content/user management
5. Build Next.js frontend with auth, blog, and signal pages
6. Add role-based access and frontend blurring logic
7. Deploy frontend on Vercel, backend on Render/Railway, media via Cloudinary

## Milestones

| Week | Milestone                                                       |
| ---- | --------------------------------------------------------------- |
| 1    | Project setup: Django + Next.js + DB schema complete            |
| 2    | Backend APIs for Auth, Blog, and Signals with role-based access |
| 3    | Frontend basic pages for login, blog, and signal viewing        |
| 4    | Admin workflows in Django Admin (post signals, manage users)    |
| 5    | Styling, mobile responsiveness, and final bug fixes             |
| 6    | Deployment + soft launch                                        |

## Gathering Results

* Track user registrations and role stats
* Monitor blog engagement
* Collect signal result accuracy
* Take feedback from users and iterate toward Premium feature monetization

