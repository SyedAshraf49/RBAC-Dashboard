# RBAC Dashboard - Role-Based Access Control Dashboard

A comprehensive web-based dashboard for managing contractors, bill tracking, and EPBG (Electronic Performance Bank Guarantee) with role-based access control.

## Features

- **User Authentication**: Secure login system with role-based access (Admin/User)
- **Contractor Management**: Track contractor details, contracts, and documents
- **Bill Tracker**: Monitor bill payments, due dates, and payment status
- **EPBG Management**: Manage bank guarantees and related documents
- **File Attachments**: Upload and store PDF/document attachments
- **Password Reset**: Email-based OTP password reset functionality
- **Theme Support**: Light/Dark mode toggle
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

**Backend:**
- Python 3.11
- Flask (Web Framework)
- PostgreSQL (Database)
- Gunicorn (WSGI Server)

**Frontend:**
- HTML5, CSS3, JavaScript
- Vanilla JS (No framework dependencies)

## Project Structure

```
RBAC-Dashboard/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables (local)
│   └── .env.example          # Environment template
├── frontend/
│   ├── index.html            # Dashboard home
│   ├── login.html            # Login page
│   ├── bill-tracker.html     # Bill tracking
│   ├── epbg.html            # EPBG management
│   ├── styles.css           # Main styles
│   ├── login.css            # Login styles
│   └── *.js                 # JavaScript files
├── database/
│   └── database.sql         # Database schema
├── RENDER_DEPLOYMENT_GUIDE.md  # Deployment instructions
├── RENDER_COMMANDS.md          # Quick reference
└── README.md
```

## Local Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 14+
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyedAshraf49/RBAC-Dashboard.git
   cd RBAC-Dashboard
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Set up PostgreSQL database**
   ```bash
   # Create database
   psql -U postgres
   CREATE DATABASE reminder_dashboard;
   \q
   ```

5. **Configure environment variables**
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your database credentials and SMTP settings
   ```

6. **Run the application**
   ```bash
   cd backend
   python app.py
   ```

7. **Access the application**
   ```
   Open browser: http://localhost:5000
   ```

### Default Login Credentials

```
Username: Subikshan
Password: Admin@123
Email: n.subikshan07@gmail.com
```

## Deployment to Render

### Quick Deployment

1. **Fork/Push this repository to your GitHub**
2. **Sign up at Render.com**
3. **Follow the detailed guide**: See [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)
4. **Quick commands**: See [RENDER_COMMANDS.md](RENDER_COMMANDS.md)

### Essential Render Configuration

**PostgreSQL Database:**
- Plan: Free
- Database Name: `reminder_dashboard`

**Web Service:**
- Build Command: `pip install -r backend/requirements.txt`
- Start Command: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`

**Environment Variables Required:**
- `DATABASE_URL` (from Render PostgreSQL)
- `SECRET_KEY` (random string)
- `FLASK_ENV=production`
- `SMTP_SERVER`, `SMTP_PORT`, `SMTP_EMAIL`, `SMTP_PASSWORD`

## User Roles & Permissions

### Admin
- Full access to all features
- Create, read, update, delete operations
- User management capabilities

### User
- Read-only access to dashboards
- View contractor lists, bills, and EPBG data
- Cannot modify data

## API Endpoints

### Authentication
- `POST /api/login` - User login
- `POST /api/logout` - User logout
- `GET /api/check-auth` - Check authentication status
- `POST /api/forgot-password` - Request password reset OTP
- `POST /api/reset-password` - Reset password with OTP

### Contractor Management
- `GET /api/contractor-list` - Get all contractors
- `POST /api/contractor-list` - Save contractor data (Admin only)

### Bill Tracker
- `GET /api/bill-tracker` - Get all bills
- `POST /api/bill-tracker` - Save bill data (Admin only)

### EPBG
- `GET /api/epbg` - Get all EPBG records
- `POST /api/epbg` - Save EPBG data (Admin only)

### User Management
- `PUT /api/user/theme` - Update user theme preference

## Security Considerations

⚠️ **Important Security Notes:**

1. **Password Hashing**: Currently using plain text passwords - **implement bcrypt hashing** for production
2. **CORS**: Update CORS settings to restrict origins in production
3. **Environment Variables**: Never commit `.env` file to repository
4. **Secret Key**: Use strong, random SECRET_KEY in production
5. **SMTP Credentials**: Use app-specific passwords, not main account password
6. **Input Validation**: Implement additional server-side validation
7. **SQL Injection**: Using parameterized queries (already implemented)

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For issues and questions:
- Open an issue on GitHub
- Check [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md) for deployment help

## Authors

- Syed Ashraf - [@SyedAshraf49](https://github.com/SyedAshraf49)

## Acknowledgments

- Original project contributors
- Render.com for hosting platform
- Open source community

---

**Repository**: https://github.com/SyedAshraf49/RBAC-Dashboard
**Deployed on**: Render.com
