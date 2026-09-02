# Render Deployment Guide for RBAC Dashboard

## Prerequisites
- A Render account (sign up at https://render.com)
- Your GitHub repository connected to Render

## Step-by-Step Deployment Instructions

### 1. Create PostgreSQL Database

1. Log in to your Render dashboard (https://dashboard.render.com)
2. Click **"New +"** button at the top right
3. Select **"PostgreSQL"**
4. Fill in the details:
   - **Name**: `rbac-dashboard-db` (or any name you prefer)
   - **Database**: `reminder_dashboard`
   - **User**: (auto-generated)
   - **Region**: Choose closest to your users (e.g., Singapore)
   - **Plan**: **Free**
5. Click **"Create Database"**
6. **Wait for the database to be created** (this may take 1-2 minutes)
7. Once created, click on the database name to open its dashboard
8. Note down the **Internal Database URL** (you'll need this later)

### 2. Create Web Service

1. Go back to your Render dashboard
2. Click **"New +"** button
3. Select **"Web Service"**
4. Connect your GitHub repository:
   - Click **"Connect account"** if not already connected
   - Select the repository: `SyedAshraf49/RBAC-Dashboard`
   - Click **"Connect"**
5. Fill in the web service details:

   **Basic Settings:**
   - **Name**: `rbac-dashboard` (or any name you prefer)
   - **Region**: Choose the same region as your database (e.g., Singapore)
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Runtime**: **Python 3**
   - **Build Command**: 
     ```
     pip install -r backend/requirements.txt
     ```
   - **Start Command**: 
     ```
     cd backend && gunicorn --bind 0.0.0.0:$PORT app:app
     ```
   - **Plan**: **Free**

6. Click **"Advanced"** to add environment variables

### 3. Configure Environment Variables

Click **"Add Environment Variable"** for each of the following:

| Key | Value | Notes |
|-----|-------|-------|
| `DATABASE_URL` | (Paste the Internal Database URL from Step 1) | Copy from your PostgreSQL database dashboard |
| `SECRET_KEY` | (Generate a random string) | Use: https://djecrety.ir/ or any random 32+ character string |
| `FLASK_ENV` | `production` | Sets Flask to production mode |
| `SMTP_SERVER` | `smtp.gmail.com` | For email functionality |
| `SMTP_PORT` | `587` | SMTP port |
| `SMTP_EMAIL` | `your-email@gmail.com` | Your Gmail address |
| `SMTP_PASSWORD` | `your-app-password` | Gmail App Password (see below) |

#### How to Get Gmail App Password:
1. Go to your Google Account settings
2. Enable 2-Step Verification if not already enabled
3. Go to Security → 2-Step Verification → App passwords
4. Generate a new app password for "Mail"
5. Copy the 16-character password and use it as `SMTP_PASSWORD`

### 4. Deploy

1. After adding all environment variables, click **"Create Web Service"**
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Start your Flask application
3. **Initial deployment takes 5-10 minutes**
4. Watch the logs for any errors

### 5. Access Your Application

1. Once deployment is complete, Render will provide you with a URL like:
   ```
   https://rbac-dashboard.onrender.com
   ```
2. Click on the URL to access your live application
3. You should see the login page

### 6. Default Login Credentials

Use these credentials to log in:

**Admin Account:**
- Username: `Subikshan`
- Email: `n.subikshan07@gmail.com`
- Password: `Admin@123`

**Other Test Accounts:**
- Username: `admin2` / Password: `Admin@456`
- Username: `user1` / Password: `User@123`

## Important Notes

### Free Tier Limitations
- Database: 1 GB storage, expires after 90 days
- Web Service: Spins down after 15 minutes of inactivity
- First request after inactivity may take 30-60 seconds to wake up

### Database Persistence
- The PostgreSQL database on the free tier **expires after 90 days**
- Upgrade to a paid plan for persistent database
- Export your data regularly as backup

### SSL/HTTPS
- Render provides free SSL certificates automatically
- Your app will be accessible via HTTPS

### Custom Domain (Optional)
1. Go to your web service settings
2. Click "Custom Domain"
3. Add your domain and follow DNS configuration instructions

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure all dependencies in `requirements.txt` are correct
- Verify Python version compatibility

### Database Connection Errors
- Ensure `DATABASE_URL` environment variable is set correctly
- Check if database is in the same region as web service
- Verify database is fully initialized before deploying web service

### Application Errors
- View logs in Render dashboard (Logs tab)
- Check if all environment variables are set
- Ensure SMTP credentials are correct for email functionality

### Session Issues
- Flask sessions are stored on the server filesystem
- After app restarts, users will need to log in again
- Consider using a database-backed session store for production

## Updating Your Application

1. Push changes to your GitHub repository:
   ```bash
   git add .
   git commit -m "Update application"
   git push origin main
   ```
2. Render will automatically detect changes and redeploy
3. Auto-deploy can be disabled in service settings if needed

## Monitoring

- **Logs**: View real-time logs in the Render dashboard
- **Metrics**: Monitor CPU, memory usage, and request counts
- **Alerts**: Set up email notifications for deploy failures

## Support

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Status Page: https://status.render.com

## Security Recommendations

1. **Change default passwords** after first login
2. **Use strong SECRET_KEY** (32+ random characters)
3. **Implement password hashing** (currently using plain text - security risk!)
4. **Restrict CORS origins** in production (update `app.py`)
5. **Set up monitoring** for suspicious activities
6. **Regular backups** of your database
7. **Update dependencies** regularly for security patches

---

**Deployment Date**: February 2025
**Repository**: https://github.com/SyedAshraf49/RBAC-Dashboard
