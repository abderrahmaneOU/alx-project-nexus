# Full Stack Real Estate App with Django

## Project Overview

This is a full-stack real estate web application built with Django. It supports user authentication, property listings, agent management, messaging, and more.

## Features

- User registration and authentication
- Property listing and search
- Agent management
- Messaging system
- Admin dashboard
- REST API support

## Requirements

- Python 3.10+
- PostgreSQL (for production)
- Redis (for channels/celery)
- Vercel account (for deployment)

## Local Development Setup

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd full-stack-realestate-app-with-django
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```
3. Copy `.env` and update secrets and database credentials as needed.
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Deploying to Vercel

Vercel is designed for serverless and frontend apps, but you can deploy Django using a serverless WSGI adapter.

### 1. Prepare for Vercel

- Ensure your database is PostgreSQL and accessible from Vercel (e.g., use Supabase, Railway, or Neon).
- Add `vercel-wsgi` to `requirements.txt` (already included).
- The `api/index.py` file is the WSGI entrypoint for Vercel.
- The `vercel.json` file configures Vercel to use this handler.

### 2. Set Environment Variables

In the Vercel dashboard, set the following environment variables:

- `SECRET_KEY`
- `DEBUG` (set to `False` in production)
- `ALLOWED_HOSTS` (comma-separated, e.g., `your-vercel-domain.vercel.app`)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` (for PostgreSQL)
- Any other secrets (email, API keys, etc.)

### 3. Deploy

1. Push your code to GitHub.
2. Import the repo in Vercel and select Python as the framework.
3. Vercel will detect `vercel.json` and deploy using `api/index.py`.
4. After deployment, run migrations from the Vercel dashboard or locally against the production database:
   ```sh
   vercel --prod
   # or
   python manage.py migrate
   ```

### 4. Static & Media Files

Vercel is not ideal for serving static/media files. Use AWS S3, Cloudinary, or similar for production static/media hosting. Update your Django settings accordingly.

## Notes

- SQLite is not supported in serverless/production. Use PostgreSQL.
- Redis is required for channels/celery (use a managed Redis provider).
- For best results, consider Render, Railway, or Heroku for Django hosting.

## Useful Commands

- `python manage.py migrate` — Apply database migrations
- `python manage.py createsuperuser` — Create admin user
- `python manage.py collectstatic` — Collect static files for production

## License

MIT
