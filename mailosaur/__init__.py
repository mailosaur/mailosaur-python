from .mailosaur_base_client import MailosaurBaseClient
from .version import VERSION
import os
import random
import string
from msrest.authentication import BasicAuthentication
from .operations.servers_operations import ServersOperations

__all__ = ['MailosaurBaseClient']

__version__ = VERSION


def generate_email_address(self, server):
  host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
  randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  return "%s.%s@%s" % (randomString, server, host)

class MailosaurClient(MailosaurBaseClient):
  def __init__(self, api_key, base_url=None):
    credentials = BasicAuthentication(api_key, '')
    ServersOperations.generate_email_address = generate_email_address
    super(MailosaurClient, self).__init__(credentials, base_url)
