import time
from tzlocal import get_localzone
from datetime import datetime, timedelta
from ..models import MessageListResult
from ..models import Message
from ..models import MailosaurException

class MessagesOperations(object):
    """MessagesOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.timezone = get_localzone()
        self.handle_http_error = handle_http_error

    def get(self, server, criteria, timeout=10000, received_after=(datetime.today() - timedelta(hours=1))):
        """Retrieve a message using search criteria.

        Returns as soon as a message matching the specified search criteria is
        found. This is the most efficient method of looking up a message.

        :param server: The identifier of the server hosting the message.
        :type server: str
        :param criteria: The search criteria to use in order to find a match.
        :type criteria: ~mailosaur.models.SearchCriteria      
        :param timeout: Specify how long to wait for a matching result (in milliseconds).
        :type timeout: int
        :param received_after: Limits results to only messages received after this date/time.
        :type received_after: datetime
        :return: Message
        :rtype: ~mailosaur.models.Message
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Defaults timeout to 10s, receivedAfter to 1h
        if len(server) != 8:
            raise MailosaurException("Must provide a valid Server ID.", "invalid_request")

        result = self.search(server, criteria, 0, 1, timeout, received_after, True)
        return self.get_by_id(result.items[0].id)

    def get_by_id(self, id):
        """Retrieve a message.

        Retrieves the detail for a single email message. Simply supply the
        unique identifier for the required message.

        :param id: The identifier of the email message to be retrieved.
        :type id: str        
        :return: Message
        :rtype: ~mailosaur.models.Message
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/messages/%s" % (self.base_url, id)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Message(data)

    def delete(self, id):
        """Delete a message.

        Permanently deletes a message. This operation cannot be undone. Also
        deletes any attachments related to the message.

        :param id: The identifier of the message to be deleted.
        :type id: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/messages/%s" % (self.base_url, id)
        response = self.session.delete(url)
        
        if response.status_code not in [204]:
            self.handle_http_error(response)
            return

    def list(self, server, page=None, items_per_page=None, received_after=None):
        """List all messages.

        Returns a list of your messages in summary form. The summaries are
        returned sorted by received date, with the most recently-received
        messages appearing first.

        :param server: The identifier of the server hosting the messages.
        :type server: str
        :param page: Used in conjunction with `itemsPerPage` to support
         pagination.
        :type page: int
        :param items_per_page: A limit on the number of results to be returned
         per page. Can be set between 1 and 1000 items, the default is 50.
        :type items_per_page: int   
        :param received_after: Limits results to only messages received after this date/time.
        :type received_after: datetime
        :return: MessageListResult
        :rtype: ~mailosaur.models.MessageListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/messages" % (self.base_url)

        if received_after is not None:
            if received_after.tzinfo is None or received_after.tzinfo.utcoffset(received_after) is None:
                received_after = self.timezone.localize(received_after)
            received_after = received_after.isoformat()

        params = {'server': server, 'page': page, 'itemsPerPage': items_per_page, 'receivedAfter': received_after}
        response = self.session.get(url, params=params)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return MessageListResult(data)

    def delete_all(self, server):
        """Delete all messages.

        Permanently deletes all messages held by the specified server. This
        operation cannot be undone. Also deletes any attachments related to
        each message.

        :param server: The identifier of the server to be emptied.
        :type server: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/messages" % (self.base_url)
        params = {'server': server}
        response = self.session.delete(url, params=params)
        
        if response.status_code not in [204]:
            self.handle_http_error(response)
            return

    def search(self, server, criteria, page=None, items_per_page=None, timeout=None, received_after=None, error_on_timeout=True):
        """Search for messages.

        Returns a list of messages matching the specified search criteria, in
        summary form. The messages are returned sorted by received date, with
        the most recently-received messages appearing first.

        :param server: The identifier of the server hosting the messages.
        :type server: str
        :param criteria: The search criteria to match results against.
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
        :param error_on_timeout: When set to false, an error will not be throw if timeout 
         is reached (default: true).
        :type error_on_timeout: bool
        :return: MessageListResult
        :rtype: ~mailosaur.models.MessageListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/messages/search" % (self.base_url)

        if received_after is not None:
            if received_after.tzinfo is None or received_after.tzinfo.utcoffset(received_after) is None:
                received_after = self.timezone.localize(received_after)
            received_after = received_after.isoformat()

        params = {'server': server, 'page': page, 'itemsPerPage': items_per_page, 'receivedAfter': received_after}

        poll_count = 0
        start_time = datetime.today()

        while True:
            response = self.session.post(url, params=params, json=criteria.toJSON())

            if response.status_code not in [200]:
                self.handle_http_error(response)
                return
            
            data = response.json()

            result = MessageListResult(data)

            if timeout is None or timeout == 0 or len(result.items) != 0:
                return result
            
            # List conversion necessary for Python 3 compatibility
            # https://stackoverflow.com/questions/36982858/object-of-type-map-has-no-len-in-python-3
            delay_pattern = list(map(int, (response.headers.get('x-ms-delay') or '1000').split(',')))

            delay = delay_pattern[len(delay_pattern) - 1] if poll_count >= len(delay_pattern) else delay_pattern[poll_count]
            
            poll_count += 1

            ## Stop if timeout will be exceeded
            if ((1000 * (datetime.today() - start_time).total_seconds()) + delay) > timeout:
                if not error_on_timeout:
                    return result
                else:
                    raise MailosaurException("No matching messages found in time. By default, only messages received in the last hour are checked (use receivedAfter to override this).", "search_timeout")

            time.sleep(delay / 1000)