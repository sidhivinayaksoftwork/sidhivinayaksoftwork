# sidhivinayaksoftwork

## Make useful things. Beautifully.

**sidhivinayaksoftwork** is an IT company based in India, delivering reliable software, digital products, technology solutions, and growth services for businesses and organizations.

We combine technical expertise, thoughtful design, and dependable engineering to help organizations build, improve, and grow their digital presence.

### What we do

- **Web development** - Fast, accessible websites and web applications built around the way your business works.
- **Android development** - Reliable Android experiences that feel natural to use and dependable at scale.
- **Digital marketing** - Clear campaigns that connect your brand with the people looking for it.
- **AI & automation** - Practical systems that reduce busywork and help teams make better decisions.

### The site

The website is a responsive company website with:

- A focused home page with company introduction, capabilities, selected work, insights, and contact CTA
- Services, work, about, insights, and contact routes
- Responsive layouts for desktop, tablet, and mobile
- Framer Motion transitions and Lucide icons
- Django-powered content management for services, projects, case studies, testimonials, team members, blog posts, careers, and site settings
- Fallback editorial content so the frontend remains useful while the CMS is empty

### Tech stack

| Area | Technology |
| --- | --- |
| Frontend | React, Vite, React Router, Tailwind CSS, Framer Motion |
| Backend | Django, Django REST Framework |
| Database | PostgreSQL-compatible configuration |
| Deployment | Vercel-ready frontend, Render-ready backend |

## Run locally

### 1. Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at `http://localhost:5173`.

### 2. Backend

Create `backend/.env` from the root `.env.example`, install the Python dependencies, then run:

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API runs at `http://localhost:8000`, with public resources under `/api/v1/` and Django Admin at `/admin/`.

For local PostgreSQL and Django services, use:

```bash
docker compose up --build
```

## Configuration

Copy `.env.example` and set environment-specific values. The main settings are:

- `VITE_API_URL` - frontend API base URL
- `DATABASE_URL` - PostgreSQL connection string
- `DJANGO_SECRET_KEY` - production secret
- `DJANGO_ALLOWED_HOSTS` - permitted backend hosts
- `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` - frontend origins

Never commit real credentials or production secrets.

## Useful commands

```bash
# Frontend production build
cd frontend
npm run build

# Frontend preview
npm run preview

# Frontend tests
npm run test
```

## Deployment

- **Frontend:** deploy the `frontend/` app to Vercel using `frontend/vercel.json`.
- **Backend:** deploy the Django service to Render using `render.yaml` and `backend/Dockerfile`.
- Configure the frontend API URL, database, CORS, CSRF, allowed hosts, and secrets in the target environment.

## Contact

- Email: [sidhivinayaksoftwork@gmail.com](mailto:sidhivinayaksoftwork@gmail.com)
- Phone: [+91 9755550213](tel:+919755550213)

Copyright 2026 sidhivinayaksoftwork - Digital products with intent.
