#!/bin/sh

# Clean output directory and rebuild generated code
rm -rf mailosaur/*
autorest

# Rename MailosaurErrorException to MailosaurException
# Rename from_property to sender (from is a reserved word)
for f in `find mailosaur -type f -name "*.py"`
do
  sed -i "" s/MailosaurErrorException/MailosaurException/g "$f"
  sed -i "" s/from_property/sender/g "$f"
done

# Customise mailosaur/__init__.py with items such as MailosaurClient class
# and generate_email_address method. Remove generated code comment.
sed -i '' '/import\ VERSION/ a\
  import os\
  import random\
  import string\
  from msrest.authentication import BasicAuthentication\
  from .operations.servers_operations import ServersOperations\
  ' mailosaur/__init__.py

echo "
def generate_email_address(self, server):
  host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
  randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  return \"%s.%s@%s\" % (randomString, server, host)

class MailosaurClient(MailosaurBaseClient):
  def __init__(self, api_key, base_url=None):
    credentials = BasicAuthentication(api_key, '')
    ServersOperations.generate_email_address = generate_email_address
    super(MailosaurClient, self).__init__(credentials, base_url)" >> mailosaur/__init__.py

sed -i '' -e '1,7d' mailosaur/__init__.py

# Update dependencies
pip install -r requirements.txt