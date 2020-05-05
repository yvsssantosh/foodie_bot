import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(email_id_list, restaurant_data):
    email = Mail(to_emails=email_id_list)
    email.from_email = os.getenv("FROM_EMAIL")
    email.template_id = os.getenv("SENDGRID_TEMPLATE_ID")
    email.dynamic_template_data = {"restaurants": restaurant_data}

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(email)
        return response.status_code
    except Exception as exception:
        print(exception)
