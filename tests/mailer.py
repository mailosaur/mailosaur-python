import os
import time
import string
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class Mailer(object):
    html = open(os.path.join(os.path.dirname(__file__), 'resources', 'testEmail.html'), 'r').read()
    text = open(os.path.join(os.path.dirname(__file__), 'resources', 'testEmail.txt'), 'r').read()

    @staticmethod
    def send_emails(client, server, quantity):
        for i in range(0, quantity):
            Mailer.send_email(client, server)

        # Allow 2 seconds for any SMTP processing
        time.sleep(2)

    @staticmethod
    def send_email(client, server, send_to_address = None):
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
        port = os.getenv('MAILOSAUR_SMTP_PORT', '25')
        
        message = MIMEMultipart('related')

        randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        message['Subject'] = "%s subject" % (randomString)

        random_to_address = send_to_address
        if (random_to_address == None):
            random_to_address = client.servers.generate_email_address(server)

        message['From'] = "%s %s <%s>" % (randomString, randomString, client.servers.generate_email_address(server))
        message['To'] = "%s %s <%s>" % (randomString, randomString, random_to_address)
        
        alt = MIMEMultipart('alternative')
        message.attach(alt)

        # Text body
        alt.attach(MIMEText(Mailer.text.replace("REPLACED_DURING_TEST", randomString)))

        # Html body
        alt.attach(MIMEText(Mailer.html.replace("REPLACED_DURING_TEST", randomString), 'html'))

        fp = open(os.path.join(os.path.dirname(__file__), 'resources', 'cat.png'), 'rb')
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', 'ii_1435fadb31d523f6')
        img.add_header('Content-Disposition', 'inline', filename='cat.png')
        message.attach(img)
        fp.close()

        fp = open(os.path.join(os.path.dirname(__file__), 'resources', 'dog.png'), 'rb')
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename='dog.png')
        message.attach(img)
        fp.close()

        smtp = smtplib.SMTP()
        smtp.connect(host, port)
        smtp.sendmail(message['From'], message['To'], message.as_string())
        smtp.quit()
