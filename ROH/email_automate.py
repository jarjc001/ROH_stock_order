import smtplib
from email.message import EmailMessage

from .login_info import *
from .file_dates import *


def create_email(wine_order: str) -> None:
    """
    creates an email containing pre order list, will send to AUTOMATE_EMAIL
    will also cc to additional emails
    :param wine_order: wine order str
    :return:
    """
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
    message_subject: str = f'Crush cellar order {date_of_order.strftime(date_format_full)}'
    message_content_start: str = (f"Hey,\n\nCan I order these for crush and"
                                  f" dorfman for the {date_of_order.strftime(date_format_day)}{suffix(date_of_order.day)} please :)\n\n")

    msg = EmailMessage()
    msg.set_content(message_content_start + wine_order)

    msg['Subject'] = message_subject
    msg['From'] = AUTOMATE_EMAIL
    msg["To"] = AUTOMATE_EMAIL
    msg["cc"] = SEND_TO_EMAIL

    s.send_message(msg)

    # # sending the mail
    # s.sendmail(AUTOMATE_EMAIL, AUTOMATE_EMAIL, message)

    # terminating the session
    s.quit()
