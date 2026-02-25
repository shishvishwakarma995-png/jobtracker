# 🗂️ Job Tracker — Django Web App

A full-stack web application built with **Django** that helps job seekers track their job applications in one place. Users can manage applications, update statuses, and monitor their job hunt progress through a clean dashboard.

---

## 🚀 Live Demo

>[https://jobtracker-1-pmmw.onrender.com/]

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, logout
- 📊 **Dashboard** — Summary of total, applied, interviewing, and offer counts
- ➕ **Add Applications** — Log company, role, status, location, date, notes
- ✏️ **Edit & Delete** — Update or remove applications anytime
- 🔍 **Status Filters** — Filter by Applied, Interviewing, Offer, Rejected
- 👤 **Per-user Data** — Each user sees only their own applications
- ⚙️ **Django Admin** — Full admin panel for superusers
- 🌑 **Dark UI** — Sleek dark theme with glowing accents

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django 6 |
| Database | SQLite (dev), PostgreSQL (prod) |
| Frontend | Bootstrap 5, Bootstrap Icons |
| Auth | Django built-in auth |
| Deployment | Render.com |

---

## 📁 Project Structure

```
jobtracker/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jobs/
│   ├── models.py       # JobApplication model
│   ├── views.py        # Class-based views
│   ├── forms.py        # ModelForm
│   ├── urls.py         # App URLs
│   ├── admin.py        # Admin config
│   └── templates/
│       ├── base.html
│       ├── registration/
│       │   ├── login.html
│       │   └── register.html
│       └── jobs/
│           ├── dashboard.html
│           ├── job_list.html
│           ├── job_form.html
│           └── job_confirm_delete.html
├── requirements.txt
├── Procfile
├── build.sh
└── manage.py
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/shishvishwakarma995-png/jobtracker.git
cd jobtracker
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🌐 Deployment

This app is deployed on **Render.com** using:
- `gunicorn` as the WSGI server
- `whitenoise` for static files
- `dj-database-url` for database configuration

---

## 👩‍💻 Author

**Shishanki Vishwakarma**
- GitHub: [@shishvishwakarma995-png](https://github.com/shishvishwakarma995-png)
- Bio: Biotechnology graduate | Web Developer | Python & Django Enthusiast

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
