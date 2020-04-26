import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(email_id_list, restaurant_data):
    email = Mail(to_emails=email_id_list)
    email.from_email = "support@foodie.com"
    email.template_id = "d-59f3f40e8f5b4560bf2c325b643394d4"
    email.dynamic_template_data = {"restaurants": restaurant_data}

    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(email)
        return response.status_code
    except Exception as exception:
        print(exception)
