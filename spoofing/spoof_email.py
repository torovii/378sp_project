
import smtplib
from email.message import EmailMessage

# SMTP server configuration
SMTP_HOST = "127.0.0.1"
SMTP_PORT = 1025

# Email information
actual_sender = "student@test.local"
spoofed_sender = "recruiting@example.com"
recipient = "participant@test.local"

# Create email
message = EmailMessage()

message["From"] = (
    f"Internship Recruiting <{spoofed_sender}>"
)
message["To"] = recipient
message["Subject"] = (
    "Software Engineering Internship Opportunity"
)

message.set_content("""
Hello,

Congratulations!

We would like to invite you to apply
for our Software Engineering Internship Program.

This is a controlled cybersecurity experiment.

Best regards,
Internship Recruiting Team
""")

# Connect to SMTP server and send email
try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(
            message,
            from_addr=actual_sender,
            to_addrs=[recipient]
        )

    print("Email successfully sent!")
    print("Actual sender:", actual_sender)
    print("Spoofed sender:", spoofed_sender)

except Exception as error:
    print("Error:", error)
