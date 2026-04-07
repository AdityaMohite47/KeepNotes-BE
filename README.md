# KeepNotes — Backend (Django REST API)

The backend API for [KeepNotes](https://github.com/AdityaMohite47/KeepNotes), a Google Keep-style notes app. Built with Django REST Framework and PostgreSQL, secured with JWT authentication.

> 🔗 **Frontend Repository:** [KeepNotes-FE](https://github.com/AdityaMohite47/KeepNotes)

## Features

- 🔐 JWT Authentication (access + refresh tokens) via SimpleJWT
- 📝 Full CRUD for notes (create, read, update, delete)
- 📌 Pin/Unpin notes toggle
- 🛡️ Per-user data isolation — users can only access their own notes
- 👤 User registration with password validation
- 🌐 CORS configured for React frontend
- ⚙️ Django Admin panel for data management

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | Django 4.2 |
| API Layer | Django REST Framework 3.14 |
| Auth | SimpleJWT 5.3 (JWT Access + Refresh tokens) |
| Database | PostgreSQL |
| CORS | django-cors-headers 4.3 |
| Env Config | python-dotenv |

## Project Structure

```
KeepNotes-BE/
├── manage.py               # Django management CLI
├── .env                    # Environment variables (not committed)
├── Pipfile                 # Python dependencies (pipenv)
├── requirements.txt        # Python dependencies (pip)
├── keepnotes/              # Django project configuration
│   ├── settings.py         # All settings (DB, JWT, CORS, DRF)
│   ├── urls.py             # Root URL routing
│   └── wsgi.py             # WSGI entry point
└── notes/                  # Notes app module
    ├── models.py           # Note model (owner, title, content, pinned)
    ├── serializers.py      # NoteSerializer, RegisterSerializer
    ├── views.py            # NoteViewSet (CRUD + pin), RegisterView
    ├── urls.py             # App-level URL routing with DRF Router
    ├── permissions.py      # IsOwner custom permission
    ├── admin.py            # Admin panel configuration
    └── migrations/         # Database migration files
```

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL installed and running
- [pipenv](https://pipenv.pypa.io/) (recommended) or pip

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/KeepNotes-BE.git
cd KeepNotes-BE
```

### 2. Install dependencies

```bash
# Using pipenv (recommended)
pip install pipenv
pipenv install

# Or using pip
pip install -r requirements.txt
```

### 3. Set up PostgreSQL

```bash
psql -U postgres
```

```sql
CREATE DATABASE keepnotes;
\q
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

DB_NAME=keepnotes
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 7. Start the server

```bash
python manage.py runserver
```

Server runs on `http://localhost:8000`

Admin panel at `http://localhost:8000/admin/`

## API Endpoints

### Authentication (Public)

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|-------------|
| `POST` | `/api/auth/register/` | Register a new user | `{ username, email, password }` |
| `POST` | `/api/auth/token/` | Login — get JWT tokens | `{ username, password }` |
| `POST` | `/api/auth/token/refresh/` | Refresh access token | `{ refresh }` |

### Notes (Requires JWT)

Include header: `Authorization: Bearer <access_token>`

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|-------------|
| `GET` | `/api/notes/` | List all notes (current user) | — |
| `POST` | `/api/notes/` | Create a note | `{ title, content }` |
| `GET` | `/api/notes/:id/` | Get a single note | — |
| `PUT` | `/api/notes/:id/` | Update a note | `{ title, content, pinned }` |
| `DELETE` | `/api/notes/:id/` | Delete a note | — |
| `POST` | `/api/notes/:id/pin/` | Toggle pin/unpin | — |

## Connecting to the Frontend

This backend is designed to work with [KeepNotes-FE](https://github.com/AdityaMohite47/KeepNotes). Make sure:

1. The backend is running on `http://localhost:8000`
2. `CORS_ALLOWED_ORIGINS` in `.env` includes the frontend URL (`http://localhost:5173`)
3. The frontend's Axios base URL points to `http://localhost:8000/api`

## License

MIT
