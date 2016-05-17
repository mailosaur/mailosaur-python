import time
import uuid
import requests

from email import Email


# Main class to access Mailosaur.com api.
class Mailosaur:
    # Pass in your mailbox id and api key to authenticate
    def __init__(self, mailbox, api_key, base_url='https://mailosaur.com/api', smtp_host='mailosaur.io'):
        self.mailbox = mailbox
        self.api_key = api_key
        self.base_url = base_url
        self.smtp_host = smtp_host

    # Retrieves all emails which have the searchPattern text in their body or subject.
    def get_emails(self, search_criteria=None, retries=10):
        if not search_criteria:
            search_criteria = dict()
        params = dict()
        if isinstance(search_criteria, basestring):
            params['search'] = search_criteria
        else:
            params = search_criteria
        params['key'] = self.api_key

        emails = None

        response = requests.get(self.base_url + '/mailboxes/' + self.mailbox + '/emails', params=params)
        response.raise_for_status()
        data = response.json()
        emails = [Email(k) for k in data]

        return emails

    # Retrieves all emails sent to the given recipient.
    def get_emails_by_recipient(self, recipient_email):
        params = dict()
        params['recipient'] = recipient_email
        return self.get_emails(params,2)

    # Retrieves the email with the given id.
    def get_email(self, email_id):
        params = dict()
        params['key'] = self.api_key

        response = requests.get(self.base_url + '/emails/' + email_id, params=params)
        data = response.json(response.text)
        email = Email(data)
        return email

    # Deletes all emails in a mailbox.
    def delete_all_email(self):
        params = dict()
        params['key'] = self.api_key

        requests.post(self.base_url + '/mailboxes/' + self.mailbox + '/empty', None, params=params)

    # Deletes the email with the given id.
    def delete_email(self, email_id):
        params = dict()
        params['key'] = self.api_key
        requests.post(self.base_url + '/emails/' + email_id + '/delete', None, params=params)

    # Retrieves the attachment with specified id.
    def get_attachment(self, attachment_id):
        params = dict()
        params['key'] = self.api_key
        response = requests.get(self.base_url + '/attachments/' + attachment_id, params=params)
        return response.text

        # Retrieves the complete raw EML file for the rawId given. RawId is a property on the email object.

    def get_raw_email(self, raw_id):
        params = dict()
        params['key'] = self.api_key

        response = requests.get(self.base_url + '/raw/' + raw_id, params=params)
        return response.text

        # Generates a random email address which can be used to send emails into the mailbox.

    def generate_email_address(self):
        return "%s.%s@%s" % (uuid.uuid4(), self.mailbox, self.smtp_host)
