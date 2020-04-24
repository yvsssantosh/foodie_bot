# TODO: Write code to send email

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(email_id_list, restaurant_data):
    message = Mail(
        from_email="satosh@foodie.com",
        to_emails=email_id_list,
        subject="Foodie Search Query",
        html_content=restaurant_data,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
