import smtplib
from .login_info import *
from email.message import EmailMessage
from .file_dates import *


def create_email(wine_order: str) -> None:
    if wine_order == "":
        return

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(AUTOMATE_EMAIL, AUTOMATE_EMAIL_PASSWORD)

    # message to be sent
    message_subject: str = f'Crush cellar order {tomorrow.strftime(date_format_full)}'
    message_content_start: str = (f"Hey,\n\nCan I order these for crush and"
                                  f" dorfman for the {tomorrow.strftime(date_format_day)}{suffix(tomorrow.day)} please :)\n\n")

    message_content_end: str = "\n\n\n\nChristian Jarjat"

    msg = EmailMessage()
    msg.set_content(message_content_start + wine_order + message_content_end)

    msg['Subject'] = message_subject
    msg['From'] = AUTOMATE_EMAIL
    msg["To"] = AUTOMATE_EMAIL
    msg["cc"] = ["jarjatc@gmail.com", "theonebatman1999@gmail.com"]

    s.send_message(msg)

    # # sending the mail
    # s.sendmail(AUTOMATE_EMAIL, AUTOMATE_EMAIL, message)

    # terminating the session
    s.quit()
