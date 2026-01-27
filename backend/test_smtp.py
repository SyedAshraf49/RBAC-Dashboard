import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT', 587))
smtp_email = os.getenv('SMTP_EMAIL')
smtp_password = os.getenv('SMTP_PASSWORD')

print(f"Testing SMTP connection to {smtp_server}:{smtp_port}...")
print(f"User: {smtp_email}")

try:
    print("Testing SMTP_SSL connection to smtp.gmail.com:465...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)
    print("SSL connection established.")
    server.login(smtp_email, smtp_password)
    print("Login successful.")
    
    msg = MIMEMultipart()
    msg['From'] = smtp_email
    msg['To'] = smtp_email # Send to self
    msg['Subject'] = "SMTP Test"
    msg.attach(MIMEText("This is a test email.", 'plain'))
    
    server.send_message(msg)
    print("Test email sent successfully.")
    server.quit()
    
    with open("smtp_result.txt", "w") as f:
        f.write("SUCCESS")
        
except Exception as e:
    print(f"ERROR: {e}")
    with open("smtp_result.txt", "w") as f:
        f.write(f"ERROR: {e}")
