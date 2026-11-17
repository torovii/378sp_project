import smtplib
from email.message import EmailMessage

# Ubuntu Postfix server
SMTP_HOST = "192.168.18.128"
SMTP_PORT = 25

# Authorized sender and test recipient
SENDER = "Samuel.lee08@student.csulb.edu"
SPOOFED_FROM = "CSULB.AIRecruiter@csulb.edu"
RECIPIENT = "Samuel.lee08@student.csulb.edu"

msg = EmailMessage()

msg["From"] = SPOOFED_FROM
msg["To"] = RECIPIENT
msg["Subject"] = "CECS 378 - Cross-Domain Spoofing Test"

msg.set_content(
    "This is an authorized cybersecurity experiment "
    "testing cross-domain sender-address spoofing."
)

#print("SMTP envelope sender:", SENDER)
#print("Visible From header:", msg["From"])
#print("Recipient:", msg["To"])
#print("\nGenerated email:")
#print(msg.as_string())

with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as server:
    server.send_message(
        msg,
        from_addr=SENDER,
        to_addrs=[RECIPIENT]
    )

print("Message accepted by Ubuntu Postfix.")