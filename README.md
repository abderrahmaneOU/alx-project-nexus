<div align="center">
  
  <h1>🏡 Full Stack Real Estate App with Django</h1>
  <p>
    <b>Modern, feature-rich real estate platform built with Django</b><br>
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
    <img src="https://img.shields.io/badge/PostgreSQL-Required-blue?logo=postgresql" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/Redis-Required-red?logo=redis" alt="Redis">
    <img src="https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel" alt="Vercel">
  </p>
</div>

---

## 🚀 Overview

A professional full-stack real estate web application built with Django. Includes user authentication, property listings, agent management, messaging, REST API, and more—all ready for modern deployment.

---

## ✨ Features

- 👤 User registration & authentication
- 🏠 Property listing & advanced search
- 🧑‍💼 Agent management
- 💬 Messaging system
- 🛠️ Admin dashboard
- 🔗 REST API support

---

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL (production database)
- Redis (channels/celery)
- Vercel account (for deployment)

---

## 🛠️ Local Development Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd full-stack-realestate-app-with-django
   ```
2. **Create a virtual environment & install dependencies:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```
3. **Configure environment:**
   - Copy `.env` and update secrets/database credentials as needed.
4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

---

## ☁️ Deploying to Vercel

> Vercel is optimized for serverless and frontend apps, but you can deploy Django using a serverless WSGI adapter.

### 1️⃣ Prepare for Vercel

- Ensure your database is PostgreSQL and accessible from Vercel (e.g., Supabase, Railway, Neon).
- `vercel-wsgi` is already included in `requirements.txt`.
- `api/index.py` is the WSGI entrypoint for Vercel.
- `vercel.json` configures Vercel to use this handler.

### 2️⃣ Set Environment Variables

In the Vercel dashboard, set:

- `SECRET_KEY`
- `DEBUG` (set to `False` in production)
- `ALLOWED_HOSTS` (comma-separated, e.g., `your-vercel-domain.vercel.app`)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` (for PostgreSQL)
- Any other secrets (email, API keys, etc.)

### 3️⃣ Deploy

1. Push your code to GitHub.
2. Import the repo in Vercel and select Python as the framework.
3. Vercel will detect `vercel.json` and deploy using `api/index.py`.
4. After deployment, run migrations from the Vercel dashboard or locally against the production database:
   ```sh
   vercel --prod
   # or
   python manage.py migrate
   ```

### 4️⃣ Static & Media Files

> ⚠️ Vercel is not ideal for serving static/media files. Use AWS S3, Cloudinary, or similar for production static/media hosting. Update your Django settings accordingly.

---

## 📝 Notes

- ❌ SQLite is not supported in serverless/production. Use PostgreSQL.
- 🔴 Redis is required for channels/celery (use a managed Redis provider).
- 💡 For best results, consider Render, Railway, or Heroku for Django hosting.

---

## 🧰 Useful Commands

- `python manage.py migrate` — Apply database migrations
- `python manage.py createsuperuser` — Create admin user
- `python manage.py collectstatic` — Collect static files for production

---

## 📄 License

MIT
