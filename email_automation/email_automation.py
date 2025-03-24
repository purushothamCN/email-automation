# email_automation/email_automation.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailAutomation:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the email automation with SMTP settings and sender credentials.

        :param smtp_server: The SMTP server (e.g., 'smtp.gmail.com')
        :param smtp_port: The port to use (usually 587 for TLS)
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body, attachments=None):
        """
        Send an email with optional attachments.

        :param receiver_email: Receiver's email address
        :param subject: Email subject
        :param body: Email body
        :param attachments: List of file paths to attach to the email (default is None)
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Attach files if any
        if attachments:
            for file in attachments:
                attachment = MIMEBase('application', 'octet-stream')
                with open(file, 'rb') as f:
                    attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={file}')
                msg.attach(attachment)

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.sender_email, self.sender_password)  # Log in
                server.sendmail(self.sender_email, receiver_email, msg.as_string())  # Send email
                print(f"Email sent to {receiver_email}")
        except Exception as e:
            print(f"Error sending email: {e}")
