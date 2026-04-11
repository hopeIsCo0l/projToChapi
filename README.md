# Waitlist & Admin Dashboard

A full-stack waitlist management system built with FastAPI, Next.js, and PostgreSQL. Users can join a waitlist, and administrators can view and manage entries through a secure dashboard.

## Live Demo

- **Frontend (Waitlist)**: [https://your-frontend.vercel.app](https://your-frontend.vercel.app)
- **Backend API**: [https://your-backend.onrender.com](https://your-backend.onrender.com)
- **Admin Dashboard**: [https://your-frontend.vercel.app/admin/login](https://your-frontend.vercel.app/admin/login)

**Admin Password**: `admin123`

## Architecture

- **Backend**: FastAPI with SQLAlchemy ORM
- **Frontend**: Next.js 14 with TypeScript and Tailwind CSS
- **Database**: PostgreSQL
- **Deployment**: Render (Backend) + Vercel (Frontend)
- **Containerization**: Docker & Docker Compose

## Project Structure

```
projtoChapi/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py          # Admin API endpoints
│   │   │   └── waitlist.py       # Waitlist API endpoints
│   │   ├── __init__.py
│   │   ├── database.py           # Database configuration
│   │   ├── email_service.py      # Email service (stub)
│   │   ├── main.py              # FastAPI application
│   │   ├── models.py            # SQLAlchemy models
│   │   └── schemas.py           # Pydantic schemas
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── admin/
│   │   │   │   ├── dashboard/
│   │   │   │   │   └── page.tsx  # Admin dashboard
│   │   │   │   └── login/
│   │   │   │       └── page.tsx  # Admin login
│   │   │   └── page.tsx          # Main waitlist page
│   │   └── components/
│   │       └── WaitlistForm.tsx  # Waitlist signup form
│   ├── next.config.js
│   └── package.json
├── docker-compose.yml
├── Dockerfile
├── render.yaml
├── vercel.json
└── README.md
```

## Quick Start (Local Development)

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd projtoChapi
```

### 2. Backend Setup

```bash
# Using Docker Compose (Recommended)
docker-compose up -d

# Or run locally
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 4. Access the Application

- **Waitlist**: http://localhost:3000
- **Admin Login**: http://localhost:3000/admin/login
- **API Documentation**: http://localhost:8000/docs
- **Admin Password**: `admin123`

## Environment Variables

### Backend (.env)

```env
DATABASE_URL=postgresql://user:password@localhost:5432/waitlist_db
ADMIN_PASSWORD=admin123
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## API Endpoints

### Waitlist Endpoints

- `POST /api/v1/waitlist/signup` - Join the waitlist
- `GET /` - Health check

### Admin Endpoints

- `GET /api/v1/admin/entries` - Get all waitlist entries (Basic Auth required)

## Deployment

### Backend (Render)

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the `render.yaml` configuration
4. Set environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `ADMIN_PASSWORD`: Your admin password

### Frontend (Vercel)

1. Connect your GitHub repository to Vercel
2. Set the root directory to `frontend`
3. Add environment variable:
   - `NEXT_PUBLIC_API_URL`: Your deployed backend URL

### Database (Render PostgreSQL)

1. Create a PostgreSQL database on Render
2. Copy the connection string to your backend environment variables

## Security Features

- **HTTP Basic Authentication** for admin endpoints
- **CORS Configuration** for cross-origin requests
- **Input Validation** using Pydantic schemas
- **SQL Injection Protection** via SQLAlchemy ORM
- **Environment Variable Management** for sensitive data

## Features

### User Features
- Clean, responsive waitlist signup form
- Real-time validation and feedback
- Duplicate email prevention
- Email confirmation (stub implementation)

### Admin Features
- Secure login with password authentication
- Comprehensive dashboard with entry management
- Real-time data refresh
- Responsive table design
- Entry count and analytics

## Future Enhancements

- [ ] Real email sending integration
- [ ] Email templates and customization
- [ ] Export functionality (CSV/Excel)
- [ ] Advanced filtering and search
- [ ] User management and roles
- [ ] Analytics and reporting
- [ ] Email campaign management
- [ ] API rate limiting
- [ ] Database migrations
- [ ] Unit and integration tests

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check `DATABASE_URL` environment variable
   - Verify database credentials

2. **CORS Errors**
   - Update CORS origins in `backend/app/main.py`
   - Ensure frontend URL is included in allowed origins

3. **Admin Authentication Issues**
   - Verify `ADMIN_PASSWORD` environment variable
   - Check browser's developer tools for network errors

## Development Notes

- The email service is currently a stub implementation
- Admin authentication uses simple session storage
- Database tables are created automatically on startup
- All API responses follow consistent error handling patterns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with using FastAPI, Next.js, and modern web technologies.**


