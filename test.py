import os, smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
load_dotenv()
 
SMTP_HOST = "smtp.mx.cloudflare.net"   # Cloudflare outbound SMTP, implicit TLS (no starttls)
SMTP_PORT = 465
TOKEN = os.getenv("CLOUDFLARE_EMAIL_TOKEN")   # from .env
if not TOKEN:
    raise RuntimeError("CLOUDFLARE_EMAIL_TOKEN missing from .env")
 
SENDER    = "demo.test@csulbai.com"                     # your verified domain
RECIPIENT = "achal.mohandas01@student.csulb.edu"      # <-- your OWN inbox, or the MXToolbox address
 
msg = MIMEMultipart()
msg["From"] = f"Pseudo Demo <{SENDER}>"   # display name deceptive, domain authenticated
msg["To"] = RECIPIENT
msg["Subject"] = "Test mail one"
msg.attach(MIMEText("Test site : www.csulbai.com", "plain"))
 
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=20) as server:
    server.login("api_token", TOKEN)   # username is literally "api_token", password is the token
    server.send_message(msg)
 
print("Sent. Open the message, 'Show original', screenshot Authentication-Results.")