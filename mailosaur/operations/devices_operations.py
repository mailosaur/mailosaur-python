import os
import random
import string

from mailosaur.models.otp_result import OtpResult
from ..models import DeviceListResult
from ..models import Device
from ..models import OtpResult
from ..models import MailosaurException


class DevicesOperations(object):
    """DevicesOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def generate_email_address(self, server):
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.net')
        randomString = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(10))
        return "%s@%s.%s" % (randomString, server, host)

    def list(self):
        """List all devices.

        Returns a list of your virtual security devices.

        :return: DeviceListResult
        :rtype: ~mailosaur.models.DeviceListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/devices" % (self.base_url)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return DeviceListResult(data)

    def create(self, device_create_options):
        """Create a device.

        Creates a new virtual security device and returns it.

        :param device_create_options:
        :type device_create_options: ~mailosaur.models.DeviceCreateOptions
        :return: Device
        :rtype: ~mailosaur.models.Device
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/devices" % (self.base_url)
        response = self.session.post(url, json=device_create_options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Device(data)

    def otp(self, query):
        """Retrieves the current one-time password for a saved device, or given base32-encoded shared secret.

        Retrieves the detail for a single server. Simply supply the unique
        identifier for the required server.

        :param query: Either the unique identifier of the device, or a base32-encoded shared secret.
        :type query: str        
        :return: OtpResult
        :rtype: ~mailosaur.models.OtpResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
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
        """Delete a device.

        Permanently delete a virtual security device. This operation cannot be undone.

        :param id: The identifier of the device to be deleted.
        :type id: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/devices/%s" % (self.base_url, id)
        response = self.session.delete(url)

        if response.status_code not in [204]:
            self.handle_http_error(response)
            return
