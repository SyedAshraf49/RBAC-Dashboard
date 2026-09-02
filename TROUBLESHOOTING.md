# Troubleshooting Guide

## Common Render Deployment Issues & Solutions

### ✅ FIXED: Python Version Compatibility Error

**Error Message:**
```
ImportError: undefined symbol: _PyInterpreterState_Get
Worker failed to boot
```

**Cause:** 
Render was using Python 3.14 (too new), but `psycopg2-binary` doesn't support it yet.

**Solution:** 
✅ **FIXED!** Updated to Python 3.11.9 (stable version)

**What was changed:**
- Updated `runtime.txt` to `python-3.11.9`
- Added `.python-version` file
- Updated `render.yaml` with correct version

**Action Required:**
Your repository now has the fix. Render will automatically redeploy with the correct Python version.

---

## Other Common Issues

### 1. Build Fails - "Could not find a version"

**Error:**
```
ERROR: Could not find a version that satisfies the requirement
```

**Solutions:**
- Check `requirements.txt` for typos
- Ensure all packages are available on PyPI
- Check Python version compatibility

---

### 2. Database Connection Error

**Error:**
```
Error connecting to PostgreSQL
OperationalError: could not connect to server
```

**Solutions:**
- ✅ Verify `DATABASE_URL` environment variable is set correctly
- ✅ Copy the **Internal Database URL** from PostgreSQL dashboard
- ✅ Ensure database is fully initialized (wait 2-3 minutes after creation)
- ✅ Check database and web service are in the same region
- ✅ Database URL should start with `postgresql://` or `postgres://`

**How to fix:**
1. Go to your PostgreSQL database in Render
2. Find **"Internal Database URL"** in the Connections section
3. Copy the entire URL
4. Go to your Web Service → Environment
5. Update `DATABASE_URL` with the copied URL
6. Save changes (Render will redeploy)

---

### 3. Application 502 Bad Gateway

**Symptoms:**
- Page shows "502 Bad Gateway"
- Application was working before

**Solutions:**
- ✅ **Wait 30-60 seconds** - App is waking up from sleep (free tier)
- ✅ Check logs in Render dashboard for actual errors
- ✅ Verify Start Command is correct: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
- ✅ Check if all environment variables are set

---

### 4. Email/SMTP Not Working

**Error:**
```
Failed to send email
SMTP Authentication Error
```

**Solutions:**
- ✅ Use Gmail App Password, NOT your regular password
- ✅ Enable 2-Step Verification in Google Account
- ✅ Generate App Password: myaccount.google.com/apppasswords
- ✅ Use 16-character app password (remove spaces)
- ✅ Verify SMTP settings:
  - `SMTP_SERVER`: `smtp.gmail.com`
  - `SMTP_PORT`: `587`
  - `SMTP_EMAIL`: Your full Gmail address
  - `SMTP_PASSWORD`: App password (16 chars)

**How to get Gmail App Password:**
1. Go to: https://myaccount.google.com/security
2. Enable "2-Step Verification" if not enabled
3. Go to "App passwords" (at bottom of security page)
4. Select "Mail" and "Other (Custom name)"
5. Generate password
6. Copy the 16-character password (ignore spaces)
7. Use this in `SMTP_PASSWORD` environment variable

---

### 5. Session/Login Issues

**Symptoms:**
- Users logged out after deployment
- Session expires immediately

**Causes:**
- Session files stored on filesystem (lost on redeploy)
- `SECRET_KEY` changed between deploys

**Solutions:**
- ✅ Ensure `SECRET_KEY` environment variable is set and consistent
- ✅ Sessions will reset on each deploy (expected behavior on free tier)
- ✅ For persistent sessions, consider database-backed session storage

---

### 6. Static Files Not Loading

**Symptoms:**
- CSS/JS files return 404
- Images not showing

**Solutions:**
- ✅ Verify frontend files are in the repository
- ✅ Check Flask static folder configuration in `app.py`
- ✅ Clear browser cache (Ctrl+Shift+R)
- ✅ Check file paths are correct in HTML

---

### 7. Application Logs Show Errors

**How to view logs:**
1. Go to Render Dashboard
2. Click on your Web Service
3. Click "Logs" tab
4. View real-time logs

**Common log errors:**

**a) Module Not Found:**
```
ModuleNotFoundError: No module named 'flask'
```
**Fix:** Check `requirements.txt` includes all dependencies

**b) Permission Denied:**
```
PermissionError: [Errno 13] Permission denied
```
**Fix:** Check file/folder permissions, remove hardcoded paths

**c) Port Already in Use:**
```
Address already in use
```
**Fix:** Use `$PORT` environment variable (already configured)

---

### 8. Database Tables Not Created

**Symptoms:**
- Login fails with database errors
- Tables missing

**Solutions:**
- ✅ Check if `init_database()` function runs on startup
- ✅ View logs for database initialization messages
- ✅ Manually run SQL schema if needed
- ✅ Verify database credentials are correct

**Manual table creation:**
1. Go to PostgreSQL database in Render
2. Click "Connect" → "External Connection"
3. Use connection details with a PostgreSQL client
4. Run the SQL from `database/database.sql`

---

### 9. Slow First Request (Free Tier)

**Symptoms:**
- First request takes 30-60 seconds
- "Please wait" or timeout errors

**This is normal on free tier:**
- Apps sleep after 15 minutes of inactivity
- First request wakes up the app (30-60 seconds)
- Subsequent requests are fast

**Solutions:**
- ✅ Just wait - this is expected behavior
- ✅ Upgrade to paid plan for always-on service
- ✅ Use a ping service to keep app awake (may violate ToS)

---

### 10. Build Command Errors

**Error:**
```
Build failed: pip install failed
```

**Solutions:**
- ✅ Verify Build Command: `pip install -r backend/requirements.txt`
- ✅ Check `requirements.txt` file exists in `backend/` folder
- ✅ Ensure Python version is specified: `3.11.9`
- ✅ Check for conflicting dependencies

---

## Render Dashboard Checklist

### Web Service Settings:
- [ ] **Name**: Any name you prefer
- [ ] **Repository**: Connected to GitHub
- [ ] **Branch**: `main`
- [ ] **Root Directory**: (empty/blank)
- [ ] **Runtime**: Python 3
- [ ] **Build Command**: `pip install -r backend/requirements.txt`
- [ ] **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
- [ ] **Region**: Same as database (e.g., Singapore)
- [ ] **Plan**: Free

### Environment Variables (All 7):
- [ ] `DATABASE_URL` - From PostgreSQL Internal URL
- [ ] `SECRET_KEY` - Generated random string
- [ ] `FLASK_ENV` - `production`
- [ ] `SMTP_SERVER` - `smtp.gmail.com`
- [ ] `SMTP_PORT` - `587`
- [ ] `SMTP_EMAIL` - Your Gmail
- [ ] `SMTP_PASSWORD` - Gmail App Password

---

## How to Force Redeploy

If you need to force a redeploy:

**Option 1: Manual Deploy**
1. Go to Web Service in Render
2. Click "Manual Deploy"
3. Select "Deploy latest commit"

**Option 2: Clear Build Cache**
1. Go to Web Service Settings
2. Scroll to "Build & Deploy"
3. Click "Clear Build Cache"
4. Trigger a new deploy

**Option 3: Push Empty Commit**
```bash
git commit --allow-empty -m "Force redeploy"
git push origin main
```

---

## Still Having Issues?

1. **Check the logs** in Render dashboard
2. **Review this troubleshooting guide**
3. **Check Render status**: https://status.render.com
4. **Review documentation**: See RENDER_DEPLOYMENT_GUIDE.md
5. **Open GitHub issue**: https://github.com/SyedAshraf49/RBAC-Dashboard/issues

---

## Useful Commands for Debugging

**View recent logs:**
- In Render Dashboard → Logs tab

**Check environment variables:**
- In Render Dashboard → Environment tab

**Check build history:**
- In Render Dashboard → Events tab

---

## Contact Support

- **Render Support**: https://render.com/docs/support
- **Community Forum**: https://community.render.com
- **Status Page**: https://status.render.com

---

**Last Updated:** 2025
**Repository:** https://github.com/SyedAshraf49/RBAC-Dashboard
