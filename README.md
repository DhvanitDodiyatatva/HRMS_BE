# HRMS Backend (HRMS_BE)

> **Human Resource Management System — Django REST Framework Backend**

[![Python](https://img.shields.io/badge/Python-3.12.x-blue?logo=python)](https://python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15.x-red)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.x-336791?logo=postgresql)](https://www.postgresql.org/)

## 📋 Project Overview

Backend REST API for the HRMS platform built with **Python**, **Django**, and **Django REST Framework (DRF)**. Provides secure, role-scoped APIs for attendance, leave, employee onboarding, resignation, transfer, salary configuration & processing, master data, dashboards and reporting.

**Frontend Repo:** [HRMS_FE](https://github.com/Dhvanit_Dodiya/HRMS_FE)

---

## 🛠️ Technology Stack

| Technology              | Version | Purpose                          |
|-------------------------|---------|----------------------------------|
| Python                  | 3.12.x  | Core language                    |
| Django                  | 5.x     | Web framework                    |
| Django REST Framework   | 3.15.x  | REST API layer                   |
| PostgreSQL              | 16.x    | Primary database                 |
| Celery                  | 5.x     | Async/background task processing |
| Redis                   | 7.x     | Celery broker & cache            |
| Simple JWT              | 5.x     | JWT authentication               |
| django-filter           | 23.x    | API filtering                    |
| drf-spectacular         | 0.27.x  | OpenAPI/Swagger docs             |
| Pillow                  | 10.x    | Image handling                   |
| openpyxl                | 3.x     | Excel export                     |
| reportlab               | 4.x     | PDF generation                   |

---

## 📂 Folder Structure

```
HRMS_BE/
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py             # Common settings
│   │   ├── development.py      # Dev overrides
│   │   ├── staging.py          # Staging overrides
│   │   └── production.py       # Production overrides
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── authentication/         # HRMS-005, HRMS-006 — Auth & RBAC
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── employees/              # HRMS-034–037, HRMS-068 — Onboarding
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── attendance/             # HRMS-011–020, HRMS-069 — Attendance
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── leave/                  # HRMS-038–047, HRMS-070 — Leave
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── salary/                 # HRMS-051–058, HRMS-071 — Salary
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── resignation/            # HRMS-048–050 — Resignation
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── transfer/               # HRMS-061 — Employee Transfer
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── master_data/            # HRMS-021–033 — Reference Masters
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   ├── dashboard/              # HRMS-059–060, HRMS-067 — Reporting
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── notifications/          # Email/notification integration seam
│       ├── migrations/
│       ├── tests/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       └── services.py
├── common/
│   ├── mixins/                 # DRF mixin base classes
│   ├── permissions/            # Custom DRF permission classes
│   ├── pagination/             # Standard pagination classes
│   ├── exceptions/             # Global exception handler, error contracts
│   ├── validators/             # Shared field validators
│   ├── utils/                  # Helper utilities (date, string, etc.)
│   └── services/               # Shared service base classes
├── api/
│   └── v1/                     # API v1 URL aggregation
├── tasks/                      # Celery task definitions
├── infrastructure/
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   ├── nginx/
│   │   └── nginx.conf
│   └── scripts/
│       ├── entrypoint.sh
│       └── wait-for-db.sh
├── tests/
│   ├── integration/
│   └── fixtures/
├── docs/                       # Architecture decisions, API contracts
├── scripts/                    # Utility scripts (migrations, seed data)
├── static/                     # Dev static files
├── media/                      # Dev media uploads
├── .env.example
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── staging.txt
│   └── production.txt
└── pyproject.toml
```

---

## 🚀 Getting Started

### Prerequisites

- Python >= 3.12
- PostgreSQL >= 16
- Redis >= 7 (for Celery)

### Installation

```bash
# Clone the repository
git clone https://github.com/Dhvanit_Dodiya/HRMS_BE.git
cd HRMS_BE

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements/development.txt

# Copy environment variables
cp .env.example .env

# Run database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

API available at [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
Swagger docs at [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

### Environment Variables

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/hrms_db
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🧪 Scripts

```bash
python manage.py runserver          # Development server
python manage.py test               # Run all tests
python manage.py test apps.authentication  # Run app-specific tests
pytest --cov=apps                   # Coverage report
celery -A config worker -l info     # Celery worker
python manage.py makemigrations     # Generate migrations
python manage.py migrate            # Apply migrations
python manage.py collectstatic      # Collect static files
```

---

## 🔌 API Structure

```
/api/v1/
├── auth/           # Login, logout, token refresh
├── employees/      # Employee CRUD, listing, onboarding
├── attendance/     # Punch, admin dashboard, devices, shifts, policy
├── leave/          # Types, rules, templates, balances, applications
├── salary/         # Types, heads, templates, monthly run, slips
├── resignation/    # Apply, track, approve
├── transfer/       # Employee transfer workflow
├── master/         # All reference data masters
├── dashboard/      # Analytics, reports, exports
└── notifications/  # Notification management
```

---

## 📦 Phase-wise Modules (HRMS-001 – HRMS-071)

| Phase | Module | Task IDs |
|-------|--------|----------|
| 01 | Analysis & Planning | HRMS-001, HRMS-002 |
| 02 | Project Setup | HRMS-003, HRMS-004 |
| 03 | Authentication & Authorization | HRMS-005, HRMS-006 |
| 04 | Shared UI & APIs | HRMS-007 |
| 05 | HR Dashboard Navigation | HRMS-008 |
| 06 | Information Management | HRMS-009, HRMS-010 |
| 07 | Employee Dashboard | HRMS-011–HRMS-013 |
| 08 | Attendance Management | HRMS-014–HRMS-020, HRMS-069 |
| 09 | Master Data Management | HRMS-021–HRMS-033 |
| 10 | Employee Onboarding | HRMS-034–HRMS-037, HRMS-068 |
| 11 | Leave Management | HRMS-038–HRMS-047, HRMS-070 |
| 12 | Resignation Management | HRMS-048–HRMS-050 |
| 13 | Salary Configuration | HRMS-051–HRMS-055 |
| 14 | Monthly Salary Processing | HRMS-056–HRMS-058, HRMS-071 |
| 15 | Dashboards & Reporting | HRMS-059, HRMS-060, HRMS-067 |
| 16 | Employee Transfer | HRMS-061 |
| 17 | Integration & System Testing | HRMS-062, HRMS-063 |
| 18 | Bug Fixing & Stabilization | HRMS-064 |
| 19 | Deployment & Documentation | HRMS-065, HRMS-066 |

---

## 🌿 Branching Strategy

```
main          ← Production-ready code
develop       ← Integration branch
feature/*     ← Feature branches (e.g., feature/HRMS-005-auth)
bugfix/*      ← Bug fix branches
hotfix/*      ← Production hotfixes
release/*     ← Release preparation
```

---

## 📄 License

Private – All rights reserved.
