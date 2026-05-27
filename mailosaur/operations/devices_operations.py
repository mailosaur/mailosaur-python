import os
import random
import string

from mailosaur.models.otp_result import OtpResult
from ..models import DeviceListResult
from ..models import Device
from ..models import OtpResult
from ..models import MailosaurException


class DevicesOperations(object):
    """Operations for managing virtual security devices and retrieving their current
    one-time passwords (OTPs), used to automate testing of app-based multi-factor
    authentication. Accessed via ``client.devices``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def generate_email_address(self, server):
        """Generates a random email address by appending a random string in front of
        the domain name of the inbox (server).

        :param server: The identifier of the inbox (server).
        :type server: str
        :return: A random email address ending in the domain of the inbox (server).
        :rtype: str
        """
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.net')
        randomString = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(10))
        return "%s@%s.%s" % (randomString, server, host)

    def list(self):
        """Returns a list of your virtual security devices.

        :return: A result containing your devices.
        :rtype: ~mailosaur.models.DeviceListResult
        """
        url = "%sapi/devices" % (self.base_url)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return DeviceListResult(data)

    def create(self, device_create_options):
        """Creates a new virtual security device.

        :param device_create_options: Options used to create a new Mailosaur virtual security device.
        :type device_create_options: ~mailosaur.models.DeviceCreateOptions
        :return: The newly-created device.
        :rtype: ~mailosaur.models.Device
        """
        url = "%sapi/devices" % (self.base_url)
        response = self.session.post(url, json=device_create_options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Device(data)

    def otp(self, query):
        """Retrieves the current one-time password for a saved device, or given
        base32-encoded shared secret.

        :param query: Either the unique identifier of the device, or a base32-encoded shared secret.
        :type query: str
        :return: A result containing the current one-time password.
        :rtype: ~mailosaur.models.OtpResult
        """
        if "-" in query:
            url = "%sapi/devices/%s/otp" % (self.base_url, query)
            response = self.session.get(url)

            if response.status_code not in [200]:
                self.handle_http_error(response)
                return

            data = response.json()

            return OtpResult(data)

        url = "%sapi/devices/otp" % (self.base_url)
        response = self.session.post(url, json={'sharedSecret': query})

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return OtpResult(data)

    def delete(
            self, id):
        """Permanently delete a virtual security device.

        This operation cannot be undone.

        :param id: The unique identifier of the device.
        :type id: str
        :return: None
        :rtype: None
        """
        url = "%sapi/devices/%s" % (self.base_url, id)
        response = self.session.delete(url)

        if response.status_code not in [204]:
            self.handle_http_error(response)
            return
