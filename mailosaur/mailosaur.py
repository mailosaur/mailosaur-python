"""
    mailosaur.com API library. Basic usage:

    >>> from mailosaur import Mailosaur
    >>> mailbox = Mailosaur("BOX_ID", "YOUR_API_KEY")
    >>> emails = mailbox.get_emails()

    More options at https://mailosaur.com/docs/email/
"""

import uuid
import requests

from .email import Email

class Mailosaur(object):
    """ Main class to access Mailosaur.com api. """

    def __init__(self, mailbox, api_key, base_url='https://mailosaur.com/api', smtp_host='mailosaur.io'):
        """ Pass in your mailbox id and api key to authenticate """
        self.mailbox = mailbox
        self.api_key = api_key
        self.base_url = base_url
        self.smtp_host = smtp_host

    def get_emails(self, search_criteria=None, retries=10):
        """ Retrieves all emails which have the searchPattern text
            in their body or subject. """

        if not search_criteria:
            search_criteria = dict()
        params = dict()
        if isinstance(search_criteria, str):
            params['search'] = search_criteria
        else:
            params = search_criteria
        params['key'] = self.api_key

        emails = None

        url = "%s/mailboxes/%s/emails" % (self.base_url, self.mailbox)
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        emails = [Email(k) for k in data]

        return emails

    def get_emails_by_recipient(self, recipient_email):
        """ Retrieves all emails sent to the given recipient. """
        params = dict()
        params['recipient'] = recipient_email
        return self.get_emails(params, 2)

    def get_email(self, email_id):
        """ Retrieves the email with the given id. """
        params = dict()
        params['key'] = self.api_key

        url = "%s/emails/%s" % (self.base_url, email_id)
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        email = Email(data)
        return email

    def delete_all_email(self):
        """  Deletes all emails in a mailbox. """
        params = dict()
        params['key'] = self.api_key

        url = "%s/mailboxes/%s/empty" % (self.base_url, self.mailbox)
        requests.post(url, None, params=params)

    def delete_email(self, email_id):
        """ Deletes the email with the given id. """
        params = dict()
        params['key'] = self.api_key
        url = "%s/emails/%s/delete" % (self.base_url, email_id)
        requests.post(url, None, params=params)

    def get_attachment(self, attachment_id):
        """ Retrieves the attachment with specified id. """
        params = dict()
        params['key'] = self.api_key

        url = "%s/attachments/%s" % (self.base_url, attachment_id)
        response = requests.get(url, params=params)
        return response.content

    def get_raw_email(self, raw_id):
        """ Retrieves the complete raw EML file for the rawId given. RawId is a property on the email object. """
        params = dict()
        params['key'] = self.api_key

        url = "%s/raw/%s" % (self.base_url, raw_id)
        response = requests.get(url, params=params)
        return response.text

    def generate_email_address(self):
        """ Generates a random email address which can be used to send emails into the mailbox. """
        return "%s.%s@%s" % (uuid.uuid4(), self.mailbox, "mailosaur.io")

