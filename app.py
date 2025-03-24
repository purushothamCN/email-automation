import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from schedule import every, run_pending

class EmailAutomation:
    """
    A simple class to send emails using SMTP with email scheduling.
    """

    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailAutomation object.

        Args:
            smtp_server (str): The SMTP server address (e.g., smtp.gmail.com).
            smtp_port (int): The SMTP server port (e.g., 587 for Gmail).
            username (str): Your email address.
            password (str): Your email password or app password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body, is_html=True):  # Set is_html=True by default
        """
        Send an email to a single recipient.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.
            is_html (bool): Whether the body is HTML. Defaults to True.
        """
        # Add footer/signature to the body
        footer = """
        <h2 style="font-size: 18px; font-weight: bold;">
            Best Regards,<br>
            Purushotham CN<br>
            Automated Mail<br>
        </h2>
        """
        body_with_footer = body + footer

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body as HTML
        msg.attach(MIMEText(body_with_footer, 'html'))

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_bulk_emails(self, emails, subject, body, is_html=True): 
        """
        Send emails to multiple recipients.

        Args:
            emails (list): A list of recipient email addresses.
            subject (str): The subject of the email.
            body (str): The body of the email.
            is_html (bool): Whether the body is HTML. Defaults to True.
        """
        for email in emails:
            self.send_email(email, subject, body, is_html)

    def schedule_email(self, to_email, subject, body, send_time, is_html=True):
        """
        Schedule an email to be sent at a specific time.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.
            send_time (str): Time to send the email (e.g., "10:30").
            is_html (bool): Whether the body is HTML. Defaults to True.
        """
        try:
            # Schedule the email
            every().day.at(send_time).do(
                self.send_email, to_email=to_email, subject=subject, body=body, is_html=is_html
            )
            print(f"Email scheduled to be sent at {send_time}")

            # Keep the script running
            while True:
                run_pending()
                time.sleep(1)
        except Exception as e:
            print(f"Failed to schedule email: {e}")


# Example usage
if __name__ == "__main__":
    # Replace these with your email credentials
    smtp_server = "smtp.gmail.com"  # For Gmail
    smtp_port = 587
    username = "purushothamputtu9@gmail.com"
    password = "jxrw qqnv oqnc wamt"

    # Initialize the EmailAutomation object
    email = EmailAutomation(smtp_server, smtp_port, username, password)

    #Single
    email.send_email(
        to_email="purushothamcn20@gmail.com",
        subject="Hello from Purushotham CN",
        body="Hi, this is my Email automation mail for testing."
    )

    # Bulk
    email.send_bulk_emails(
        emails=["rohinimetri141@gmail.com", "vishuvishwas622@gmail.com", "abhishek.shek3456@gmail.com"],
        subject="Hello Everyone!",
        body="This is a bulk email sent using Python."
    )

    # Schedule 
    email.schedule_email(
        to_email="purushothamcn20@gmail.com",
        subject="Scheduled Email",
        body="This email was scheduled.",
        send_time="09:46" 
    )