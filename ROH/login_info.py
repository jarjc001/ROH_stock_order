import os

USERNAME: str = os.environ.get('RESDIARY_EMAIL')
PASSWORD: str = os.environ.get('RESDIARY_EMAIL_PASSWORD')

AUTOMATE_EMAIL: str = os.environ.get('AUTOMATE_EMAIL')
AUTOMATE_EMAIL_PASSWORD: str = os.environ.get("AUTOMATE_EMAIL_PASSWORD")

SEND_TO_EMAIL: list[str] = []

FILE_LOCATION: str = os.path.abspath(os.getcwd()) +r'\data_export'

