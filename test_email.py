import smtplib
from email.mime.text import MIMEText
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

msg = MIMEText("This is a test email from the Bank Fraud demo system.")
msg["From"] = SMTP_USER
msg["To"] = SMTP_USER
msg["Subject"] = "SMTP Test - Bank Fraud Demo"

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.send_message(msg)

print("✅ Email sent successfully")




def add(a,b):
    p=a+b

    
    return p  


CREATE OR REPLACE FUNCTION check_order_amount()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.order_amount <= 0 THEN
        RAISE EXCEPTION 'Order amount must be greater than zero';
    
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

