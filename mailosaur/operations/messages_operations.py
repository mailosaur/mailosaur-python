import time
from datetime import datetime, timedelta
from ..models import MessageListResult
from ..models import Message
from ..models import PreviewListResult
from ..models import MailosaurException


class MessagesOperations(object):
    """Operations for finding, retrieving, creating, forwarding, replying to, and
    deleting the email and SMS messages received by your Mailosaur inboxes (servers).
    Accessed via ``client.messages``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def get(self, server, criteria, timeout=10000, received_after=(datetime.today() - timedelta(hours=1)), dir=None):
        """Waits for a message to be found, returning as soon as a message matching the
        specified search criteria is found.

        **Recommended:** This is the most efficient method of looking up a message,
        therefore we recommend using it wherever possible.

        :param server: The unique identifier of the containing inbox (server).
        :type server: str
        :param criteria: The criteria with which to find messages during a search.
        :type criteria: ~mailosaur.models.SearchCriteria
        :param timeout: Specify how long to wait for a matching result (in milliseconds).
        :type timeout: int
        :param received_after: Limits results to only messages received after this date/time.
        :type received_after: datetime
        :param dir: Optionally limits results based on the direction (`Sent` or `Received`),
         with the default being `Received`.
        :type dir: str
        :return: The first message matching the criteria.
        :rtype: ~mailosaur.models.Message
        :raises: :class:`MailosaurException<mailosaur.models.MailosaurException>`
         with error type ``no_messages_found`` if no matching message exists, or
         ``search_timeout`` if no matching message arrives before the timeout elapses.
        """
        # Defaults timeout to 10s, receivedAfter to 1h
        if len(server) != 8:
            raise MailosaurException(
                "Must provide a valid Server ID.", "invalid_request")

        result = self.search(server, criteria, 0, 1,
                             timeout, received_after, True, dir)
        return self.get_by_id(result.items[0].id)

    def get_by_id(self, id):
        """Retrieves the detail for a single message.

        Must be used in conjunction with either list or search in order to get the
        unique identifier for the required message.

        :param id: The unique identifier of the message to be retrieved.
        :type id: str
        :return: The full message.
        :rtype: ~mailosaur.models.Message
        """
        url = "%sapi/messages/%s" % (self.base_url, id)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Message(data)

    def delete(self, id):
        """Permanently deletes a message.

        Also deletes any attachments related to the message. This operation cannot
        be undone.

        :param id: The identifier for the message.
        :type id: str
        :return: None
        :rtype: None
        """
        url = "%sapi/messages/%s" % (self.base_url, id)
        response = self.session.delete(url)

        if response.status_code not in [204]:
            self.handle_http_error(response)
            return

    def list(self, server, page=None, items_per_page=None, received_after=None, dir=None):
        """Returns a list of your messages in summary form.

        The summaries are returned sorted by received date, with the most
        recently-received messages appearing first.

        :param server: The unique identifier of the required inbox (server).
        :type server: str
        :param page: Used in conjunction with `itemsPerPage` to support
         pagination.
        :type page: int
        :param items_per_page: A limit on the number of results to be returned
         per page. Can be set between 1 and 1000 items, the default is 50.
        :type items_per_page: int
        :param received_after: Limits results to only messages received after this date/time.
        :type received_after: datetime
        :param dir: Optionally limits results based on the direction (`Sent` or `Received`),
         with the default being `Received`.
        :type dir: str
        :return: A result containing the message summaries.
        :rtype: ~mailosaur.models.MessageListResult
        """
        url = "%sapi/messages" % (self.base_url)

        if received_after is not None:
            received_after = received_after.astimezone().replace(microsecond=0).isoformat()

        params = {'server': server, 'page': page,
                  'itemsPerPage': items_per_page, 'receivedAfter': received_after, 'dir': dir}
        response = self.session.get(url, params=params)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return MessageListResult(data)

    def delete_all(self, server):
        """Permanently delete all messages within an inbox (server).

        This operation cannot be undone.

        :param server: The unique identifier of the inbox (server).
        :type server: str
        :return: None
        :rtype: None
        """
        url = "%sapi/messages" % (self.base_url)
        params = {'server': server}
        response = self.session.delete(url, params=params)

        if response.status_code not in [204]:
            self.handle_http_error(response)
            return

    def search(self, server, criteria, page=None, items_per_page=None, timeout=None, received_after=None, error_on_timeout=True, dir=None):
        """Returns a list of messages matching the specified search criteria, in summary form.

        The messages are returned sorted by received date, with the most
        recently-received messages appearing first.

        :param server: The unique identifier of the inbox (server) to search.
        :type server: str
        :param criteria: The criteria with which to find messages during a search.
        :type criteria: ~mailosaur.models.SearchCriteria
        :param page: Used in conjunction with `itemsPerPage` to support
         pagination.
        :type page: int
        :param items_per_page: A limit on the number of results to be returned
         per page. Can be set between 1 and 1000 items, the default is 50.
        :type items_per_page: int
        :param timeout: Specify how long to wait for a matching result (in milliseconds).
        :type timeout: int
        :param received_after: Limits results to only messages received after this date/time.
        :type received_after: datetime
        :param error_on_timeout: When set to false, an error will not be thrown if timeout
         is reached (default: true).
        :type error_on_timeout: bool
        :param dir: Optionally limits results based on the direction (`Sent` or `Received`),
         with the default being `Received`.
        :type dir: str
        :return: A result containing the matching message summaries.
        :rtype: ~mailosaur.models.MessageListResult
        :raises: :class:`MailosaurException<mailosaur.models.MailosaurException>`
         with error type ``search_timeout`` if no matching message is found before
         the timeout elapses, unless ``error_on_timeout`` is set to false.
        """
        url = "%sapi/messages/search" % (self.base_url)

        if received_after is not None:
            received_after = received_after.astimezone().replace(microsecond=0).isoformat()

        params = {'server': server, 'page': page,
                  'itemsPerPage': items_per_page, 'receivedAfter': received_after, 'dir': dir}

        poll_count = 0
        start_time = datetime.today()

        while True:
            response = self.session.post(
                url, params=params, json=criteria.to_json())

            if response.status_code not in [200]:
                self.handle_http_error(response)
                return

            data = response.json()

            result = MessageListResult(data)

            if timeout is None or timeout == 0 or len(result.items) != 0:
                return result

            # List conversion necessary for Python 3 compatibility
            # https://stackoverflow.com/questions/36982858/object-of-type-map-has-no-len-in-python-3
            delay_pattern = list(
                map(int, (response.headers.get('x-ms-delay') or '1000').split(',')))

            delay = delay_pattern[len(
                delay_pattern) - 1] if poll_count >= len(delay_pattern) else delay_pattern[poll_count]

            poll_count += 1

            # Stop if timeout will be exceeded
            if ((1000 * (datetime.today() - start_time).total_seconds()) + delay) > timeout:
                if not error_on_timeout:
                    return result
                else:
                    raise MailosaurException(
                        "No matching messages found in time. By default, only messages received in the last hour are checked (use receivedAfter to override this). The search criteria used for this query was [%s] which timed out after %sms" % (criteria.to_json(), timeout), "search_timeout")

            time.sleep(delay / 1000)

    def create(self, server, options):
        """Creates a new message that can be sent to a verified email address.

        This is useful in scenarios where you want an email to trigger a workflow
        in your product.

        :param server: The unique identifier of the required inbox (server).
        :type server: str
        :param options: Options to use when creating a new message.
        :type options: ~mailosaur.models.MessageCreateOptions
        :return: The newly-created message.
        :rtype: ~mailosaur.models.Message
        """
        url = "%sapi/messages" % (self.base_url)
        params = {'server': server}
        response = self.session.post(
            url, params=params, json=options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Message(data)

    def forward(self, id, options):
        """Forwards the specified message to a verified email address.

        This is useful for simulating a user forwarding one of your email messages.

        :param id: The unique identifier of the message to be forwarded.
        :type id: str
        :param options: Options to use when forwarding a message.
        :type options: ~mailosaur.models.MessageForwardOptions
        :return: The forwarded message.
        :rtype: ~mailosaur.models.Message
        """
        url = "%sapi/messages/%s/forward" % (self.base_url, id)
        response = self.session.post(url, json=options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Message(data)

    def reply(self, id, options):
        """Sends a reply to the specified message.

        This is useful for when simulating a user replying to one of your email
        or SMS messages.

        :param id: The unique identifier of the message to be replied to.
        :type id: str
        :param options: Options to use when replying to a message.
        :type options: ~mailosaur.models.MessageReplyOptions
        :return: The reply message.
        :rtype: ~mailosaur.models.Message
        """
        url = "%sapi/messages/%s/reply" % (self.base_url, id)
        response = self.session.post(url, json=options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Message(data)

    def generate_previews(self, id, options):
        """Generates screenshots of an email rendered in the specified email clients.

        :param id: The identifier of the email to preview.
        :type id: str
        :param options: The options with which to generate previews.
        :type options: ~mailosaur.models.PreviewRequestOptions
        :return: A result containing the generated previews.
        :rtype: ~mailosaur.models.PreviewListResult
        """
        url = "%sapi/messages/%s/screenshots" % (self.base_url, id)
        response = self.session.post(url, json=options.to_json())

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return PreviewListResult(data)
