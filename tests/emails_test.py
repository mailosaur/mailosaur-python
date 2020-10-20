import os
from datetime import datetime, timedelta
from unittest import TestCase
from .mailer import Mailer
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria, MailosaurException

class EmailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')
        cls.server = os.getenv('MAILOSAUR_SERVER')

        if (api_key or cls.server) is None:
            raise Exception("Missing necessary environment variables - refer to README.md")

        cls.client = MailosaurClient(api_key, base_url)

        cls.client.messages.delete_all(cls.server)

        Mailer.send_emails(cls.client, cls.server, 5)

        cls.emails = cls.client.messages.list(cls.server).items

    def test_list(self):
        self.assertEqual(5, len(self.emails))

        for email in self.emails:
            self.validate_email_summary(email)
    
    def test_list_received_after(self):
        past_date = datetime.today() - timedelta(minutes=10)
        past_emails = self.client.messages.list(self.server, received_after=past_date).items
        self.assertTrue(len(past_emails) > 0)
        
        future_emails = self.client.messages.list(self.server, received_after=datetime.today()).items
        self.assertEqual(0, len(future_emails))

    def test_get(self):
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
        test_email_address = "wait_for_test.%s@%s" % (self.server, host)

        Mailer.send_email(self.client, self.server, test_email_address)

        criteria = SearchCriteria()
        criteria.sent_to = test_email_address
        email = self.client.messages.get(self.server, criteria)
        self.validate_email(email)

    def test_get(self):
        email_to_retrieve = self.emails[0]
        email = self.client.messages.get_by_id(email_to_retrieve.id)
        self.validate_email(email)
        self.validate_headers(email)

    def test_get_not_found(self):
        with self.assertRaises(MailosaurException):
            self.client.messages.get_by_id("efe907e9-74ed-4113-a3e0-a3d41d914765")

    def test_search_timeout_errors_suppressed(self):
        criteria = SearchCriteria()
        criteria.sent_from = "neverfound@example.com"
        results = self.client.messages.search(self.server, criteria, timeout=1, error_on_timeout=False).items
        self.assertEqual(0, len(results))

    def test_search_no_criteria_error(self):
        with self.assertRaises(MailosaurException):
            self.client.messages.search(self.server, SearchCriteria())
    
    def test_search_by_sent_from(self):
        target_email = self.emails[1]
        criteria = SearchCriteria()
        criteria.sent_from = target_email.sender[0].email
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(1, len(results))
        self.assertEqual(target_email.sender[0].email, results[0].sender[0].email)
        self.assertEqual(target_email.subject, results[0].subject)

    def test_search_by_sent_from_invalid_email(self):
        criteria = SearchCriteria()
        criteria.sent_from = ".not_an_email_address"

        with self.assertRaises(MailosaurException):
            self.client.messages.search(self.server, criteria)
        
    def test_search_by_sent_to(self):
        target_email = self.emails[1]
        criteria = SearchCriteria()
        criteria.sent_to = target_email.to[0].email
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(1, len(results))
        self.assertEqual(target_email.to[0].email, results[0].to[0].email)
        self.assertEqual(target_email.subject, results[0].subject)

    def test_search_by_sent_to_invalid_email(self):
        criteria = SearchCriteria()
        criteria.sent_to = ".not_an_email_address"

        with self.assertRaises(MailosaurException):
            self.client.messages.search(self.server, criteria)

    def test_search_by_body(self):
        target_email = self.emails[1]
        unique_string = target_email.subject[0:10]
        criteria = SearchCriteria()
        criteria.body = "%s html" % (unique_string)
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(1, len(results))
        self.assertEqual(target_email.to[0].email, results[0].to[0].email)
        self.assertEqual(target_email.subject, results[0].subject)

    def test_search_by_subject(self):
        target_email = self.emails[1]
        unique_string = target_email.subject[0:10]
        criteria = SearchCriteria()
        criteria.subject = unique_string
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(1, len(results))
        self.assertEqual(target_email.to[0].email, results[0].to[0].email)
        self.assertEqual(target_email.subject, results[0].subject)

    def test_search_with_match_all(self):
        target_email = self.emails[1]
        unique_string = target_email.subject[0:10]
        criteria = SearchCriteria()
        criteria.subject = unique_string
        criteria.body = "this is a link"
        criteria.match = "ALL"
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(1, len(results))
    
    def test_search_with_match_any(self):
        target_email = self.emails[1]
        unique_string = target_email.subject[0:10]
        criteria = SearchCriteria()
        criteria.subject = unique_string
        criteria.body = "this is a link"
        criteria.match = "ANY"
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(4, len(results))
    
    def test_search_with_special_characters(self):
        criteria = SearchCriteria()
        criteria.subject = "Search with ellipsis … and emoji 👨🏿‍🚒"
        results = self.client.messages.search(self.server, criteria).items
        self.assertEqual(0, len(results))

    def test_spam_analysis(self):
        target_id = self.emails[0].id
        result = self.client.analysis.spam(target_id)
        
        for rule in result.spam_filter_results.spam_assassin:
            self.assertIsNotNone(rule.rule)
            self.assertIsNotNone(rule.description)

    def test_delete(self):
        target_email_id = self.emails[4].id

        self.client.messages.delete(target_email_id)

        # Attempting to delete again should fail
        with self.assertRaises(MailosaurException):
            self.client.messages.delete(target_email_id)

    def validate_email(self, email):
        self.validate_metadata(email)
        self.validate_attachments(email)
        self.validate_html(email)
        self.validate_text(email)
        
    def validate_email_summary(self, email):
        self.validate_metadata(email)
        self.assertIsNotNone(email.summary)
        self.assertEqual(2, email.attachments)

    def validate_html(self, email):
        # Html.Body
        self.assertTrue(email.html.body.startswith("<div dir=\"ltr\">"))

        # Html.Links
        self.assertEqual(3, len(email.html.links))
        self.assertEqual("https://mailosaur.com/", email.html.links[0].href)
        self.assertEqual("mailosaur", email.html.links[0].text)
        self.assertEqual("https://mailosaur.com/", email.html.links[1].href)
        self.assertIsNone(email.html.links[1].text)
        self.assertEqual("http://invalid/", email.html.links[2].href)
        self.assertEqual("invalid", email.html.links[2].text)

        # Html.Images
        self.assertTrue(email.html.images[1].src.startswith('cid:'))
        self.assertEqual("Inline image 1", email.html.images[1].alt)

    def validate_text(self, email):
        # Text.Body
        self.assertTrue(email.text.body.startswith("this is a test"))

        # Text.Links
        self.assertEqual(2, len(email.text.links))
        self.assertEqual("https://mailosaur.com/", email.text.links[0].href)
        self.assertEqual(email.text.links[0].href, email.text.links[0].text)
        self.assertEqual("https://mailosaur.com/", email.text.links[1].href)
        self.assertEqual(email.text.links[1].href, email.text.links[1].text)

    def validate_headers(self, email):
        expected_from_header = "%s <%s>" % (email.sender[0].name, email.sender[0].email)
        expected_to_header = "%s <%s>" % (email.to[0].name, email.to[0].email)
        headers = email.metadata.headers
        
        # Invalid python3 syntax
        # print [h for h in headers if h.field.lower() == "from"]


        # self.assertEqual(expected_from_header, [h for h in headers if h.field.lower() == "from"][0].value)
        # self.assertEqual(expected_from_header, [h for h in headers if h.field.lower() == "to"][0].value)
        # self.assertEqual(email.subject, [h for h in headers if h.field.lower() == "subject"][0].value)

    def validate_metadata(self, email):
        self.assertEqual(1, len(email.sender))
        self.assertEqual(1, len(email.to))
        self.assertIsNotNone(email.sender[0].email)
        self.assertIsNotNone(email.sender[0].name)
        self.assertIsNotNone(email.to[0].email)
        self.assertIsNotNone(email.to[0].name)
        self.assertIsNotNone(email.subject)
        self.assertIsNotNone(email.server)
        
        self.assertEqual(datetime.strftime(datetime.now(), '%Y-%m-%d'), datetime.strftime(email.received, '%Y-%m-%d'))

    def validate_attachments(self, email):
        self.assertEqual(2, len(email.attachments))

        file1 = email.attachments[0]
        self.assertIsNotNone(file1.id)
        self.assertIsNotNone(file1.url)
        self.assertEqual(82138, file1.length)
        self.assertEqual("cat.png", file1.file_name)
        self.assertEqual("image/png", file1.content_type)
        
        file2 = email.attachments[1]
        self.assertIsNotNone(file2.id)
        self.assertIsNotNone(file2.url)
        self.assertEqual(212080, file2.length)
        self.assertEqual("dog.png", file2.file_name)
        self.assertEqual("image/png", file2.content_type)

if __name__ == '__main__':
    unittest.main()
