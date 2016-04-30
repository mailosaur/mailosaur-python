# Mailosaur Python client library

Mailosaur allows you to automate tests that require email. You can also use it for manual testing as it gives you unlimited test email addresses or use it as a fake/dummy SMTP service.

For more info go to [mailosaur.com](https://mailosaur.com/)


## Installation

  pip install mailosaur

## Usage
```python
from mailosaur.mailosaur import Mailosaur
from unittest import TestCase

mailbox = Mailosaur(mailbox_id, api_key)

emails = mailbox.get_emails_by_recipient('anything.1eaaeef6@mailosaur.in')

assertEqual('something', emails[0].subject, 'The subject should be something')
```
##Api

*functions:*

- **Email[] get_emails(search_pattern)** - Retrieves all emails which have the searchPattern text in their body or subject.

- **Email[] get_emails_by_recipient(recipientEmail)** -
Retrieves all emails sent to the given recipient.

- **Email get_email(email_id)** -
Retrieves the email with the given id.

- **delete_all_email()** -
Deletes all emails in a mailbox.

- **delete_email(email_id)** -
Deletes the email with the given id.

- **get_attachment(attachment_id)** -
Retrieves the attachment with specified id as a byte array.

- **get_raw_email(raw_id)** -
Retrieves the complete raw EML file for the rawId given as a byte array. raw_id is a property on the email object.

- **generate_email_address()** -
Generates a random email address which can be used to send emails into the mailbox.

*structures*

- **Email** - The core object returned by the Mailosaur API
  - **id** - The email identifier
  - **creation_date** - The date your email was received by Mailosaur
  - **sender_host** - The host name of the machine that sent the email
  - **raw_id** - Reference for raw email data
  - **html** - The HTML content of the email
    - **links** - All links found within the HTML content of the email
    - **images** - All images found within the HTML content of the email
    - **body** - Unescaped HTML body of the email
  - **text** - The text content of the email
    - **links** - All links found within the text content of the email
    - **body** - Text body of the email
  - **headers** - Contains all email headers as object properties
  - **subject** - Email subject
  - **priority** - Email priority
  - **from** - Details of email sender(s)
    - **address** - Email address
    - **name** - Email sender name
  - **to** - Details of email recipient(s)
    - **address** - Email address
    - **name** - Email recipient name
  - **attachments** - Details of any attachments found within the email
    - **id** - Attachment identifier
    - **file_name** - Attachment file name
    - **length** - Attachment file size (in bytes)
    - **content_type** - Attachment mime type (e.g. "image/png")
