# Render Dashboard Configuration - Quick Reference

## Copy-Paste Commands for Render Dashboard

### 1. PostgreSQL Database Settings

**When creating PostgreSQL database, use these settings:**

```
Name: rbac-dashboard-db
Database: reminder_dashboard
Region: Singapore (or closest to you)
Plan: Free
```

### 2. Web Service Build & Start Commands

**Build Command:**
```bash
pip install -r backend/requirements.txt
```

**Start Command:**
```bash
cd backend && gunicorn --bind 0.0.0.0:$PORT app:app
```

### 3. Environment Variables to Add

Copy these one by one into your Render Web Service environment variables:

```
DATABASE_URL = <Copy from your PostgreSQL database Internal URL>
SECRET_KEY = <Generate random 32+ character string>
FLASK_ENV = production
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
SMTP_EMAIL = <your-email@gmail.com>
SMTP_PASSWORD = <your-gmail-app-password>
```

#### Example Environment Variables (Replace with your values):
```
DATABASE_URL: postgresql://user:password@hostname:5432/reminder_dashboard
SECRET_KEY: 8k9JdL2mN5pQ7rS1tU3vW4xY6zA0bC2dE4fG6hI8jK0lM2nO4pQ6rS8tU0vW2xY4zA6
FLASK_ENV: production
SMTP_SERVER: smtp.gmail.com
SMTP_PORT: 587
SMTP_EMAIL: your-email@gmail.com
SMTP_PASSWORD: abcd efgh ijkl mnop
```

### 4. Deployment Checklist

- [ ] Create PostgreSQL database first
- [ ] Wait for database to be fully initialized
- [ ] Copy the Internal Database URL
- [ ] Create Web Service
- [ ] Add all environment variables
- [ ] Set Build Command
- [ ] Set Start Command
- [ ] Deploy and monitor logs
- [ ] Test application URL
- [ ] Login with default credentials
- [ ] Change default passwords

### 5. Default Login Credentials

```
Username: Subikshan
Password: Admin@123
Email: n.subikshan07@gmail.com
```

### 6. Post-Deployment Tasks

After successful deployment:

1. **Test the application**: Visit your Render URL
2. **Login**: Use default credentials above
3. **Change passwords**: Update all default user passwords
4. **Configure SMTP**: Test password reset functionality
5. **Add users**: Create actual user accounts
6. **Monitor logs**: Watch for any errors in Render dashboard

### 7. Common Issues & Fixes

**Issue**: Application not starting
**Fix**: Check logs in Render dashboard, verify all environment variables are set

**Issue**: Database connection error
**Fix**: Ensure DATABASE_URL is correct and database is running

**Issue**: Email not sending
**Fix**: Verify SMTP credentials, enable "Less secure app access" or use App Password

**Issue**: 502 Bad Gateway
**Fix**: App is starting up (wait 30-60 seconds) or check logs for errors

---

## Need Help?

- Check RENDER_DEPLOYMENT_GUIDE.md for detailed instructions
- View Render logs for error messages
- Ensure all steps above are completed
