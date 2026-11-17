
import smtplib
from email.message import EmailMessage

SMTP_HOST = "127.0.0.1"
SMTP_PORT = 1025

# Actual SMTP envelope sender
ACTUAL_SENDER = "test-sender@lab.example"

# Forged sender displayed to recipient
SPOOFED_SENDER = "recruiting@csulbai.com"

# Controlled test recipient
RECIPIENT = "participant@lab.example"

msg = EmailMessage()

msg["From"] = f"CSULB AI Recruiting <{SPOOFED_SENDER}>"
msg["To"] = RECIPIENT
msg["Subject"] = "CECS 378 - Email Spoofing Experiment"

msg.set_content(
    "This is an authorized email spoofing experiment "
    "for CECS 378."
)

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.send_message(
        msg,
        from_addr=ACTUAL_SENDER,
        to_addrs=[RECIPIENT]
    )

print("Email successfully submitted to local SMTP server!")
print("Actual SMTP sender:", ACTUAL_SENDER)
print("Forged From address:", SPOOFED_SENDER)
