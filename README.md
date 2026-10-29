# HRMS Backend

> **Human Resource Management System — Django REST Framework Backend**

[![Python](https://img.shields.io/badge/Python-3.12.x-blue?logo=python)](https://python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15.x-red)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.x-336791?logo=postgresql)](https://www.postgresql.org/)

## Overview

Backend REST API for the HRMS platform built with **Python**, **Django**, and **Django REST Framework (DRF)**. Provides secure, role-scoped APIs for attendance, leave, employee onboarding, resignation, transfer, salary configuration & processing, master data, dashboards and reporting.

**Frontend Repo:** [HRMS_FE](https://github.com/DhvanitDodiyatatva/HRMS_FE)

---

## Technology Stack

| Technology            | Version | Purpose                         |
|-----------------------|---------|---------------------------------|
| Python                | 3.12.x  | Core language                   |
| Django                | 5.x     | Web framework                   |
| Django REST Framework | 3.15.x  | REST API layer                  |
| PostgreSQL            | 16.x    | Primary database                |
| Celery                | 5.x     | Background task processing      |
| Redis                 | 7.x     | Celery broker & cache           |
| Simple JWT            | 5.x     | JWT authentication              |
| django-filter         | 23.x    | API filtering                   |
| drf-spectacular       | 0.27.x  | OpenAPI / Swagger docs          |
| openpyxl              | 3.x     | Excel export                    |
| reportlab             | 4.x     | PDF generation                  |

---

## Folder Structure

```
HRMS_BE/
├── config/
│   ├── settings/
│   │   ├── base.py             # Common settings
│   │   ├── development.py      # Dev overrides
│   │   ├── staging.py          # Staging overrides
│   │   └── production.py       # Production overrides
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── authentication/         # Auth, JWT, RBAC
│   ├── employees/              # Employee onboarding & management
│   ├── attendance/             # Attendance, devices, policy, shifts
│   ├── leave/                  # Leave types, rules, balances, applications
│   ├── salary/                 # Salary config, run, slips
│   ├── resignation/            # Resignation workflow
│   ├── transfer/               # Employee transfer
│   ├── master_data/            # All reference data masters
│   ├── dashboard/              # Analytics & reporting
│   └── notifications/          # Email/notification integration
│   Each app: models.py | serializers.py | views.py | urls.py | services.py | tests/
├── common/
│   ├── models.py               # BaseModel (UUID, soft-delete, timestamps)
│   ├── exceptions/             # Custom exception handler & error contract
│   ├── pagination/             # Standard pagination classes
│   ├── permissions/            # Custom DRF permission classes
│   ├── mixins/                 # Reusable viewset mixins
│   ├── validators/             # Shared field validators
│   └── utils/                  # Helper utilities
├── api/
│   └── v1/                     # API v1 URL aggregation
├── tasks/                      # Celery task definitions
├── infrastructure/
│   ├── docker/
│   ├── nginx/
│   └── scripts/
├── tests/
│   ├── integration/
│   └── fixtures/
├── static/
├── media/
├── .env.example
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── pyproject.toml
```

---

## Getting Started

### Prerequisites

- Python >= 3.12
- PostgreSQL >= 16
- Redis >= 7

### Installation

```bash
# Clone the repository
git clone https://github.com/DhvanitDodiyatatva/HRMS_BE.git
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

## Scripts

```bash
python manage.py runserver           # Development server
python manage.py test                # Run all tests
pytest --cov=apps                    # Coverage report
celery -A config worker -l info      # Celery worker
python manage.py makemigrations      # Generate migrations
python manage.py migrate             # Apply migrations
python manage.py collectstatic       # Collect static files
```

---

## API Structure

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

## Modules

| Module                   | Description                                              |
|--------------------------|----------------------------------------------------------|
| Authentication & RBAC    | JWT login/logout, role-based access, org-scoped queries  |
| Employee Management      | Onboarding, profiles, invitations, safe deletion         |
| Attendance               | Punch, admin dashboard, devices, policy, shifts, timesheets |
| Leave                    | Types, rules, templates, balances, applications, approvals |
| Salary                   | Configuration, calculation engine, monthly run, payslips |
| Resignation              | Application, tracking, multi-step approval               |
| Employee Transfer        | From/to workflow with document and effective date        |
| Master Data              | All reference data (blood group, designation, holiday…)  |
| Dashboards & Reporting   | HR analytics, attendance reports, salary exports         |

---

## Branching Strategy

```
main          ← Production-ready code
develop       ← Integration branch
feature/*     ← Feature branches
bugfix/*      ← Bug fix branches
hotfix/*      ← Production hotfixes
release/*     ← Release preparation
```

---

## License

Private – All rights reserved.
