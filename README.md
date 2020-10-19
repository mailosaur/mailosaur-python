# Mailosaur Python Client Library

[Mailosaur](https://mailosaur.com) lets you automate email and SMS tests, like account verification and password resets, and integrate these into your CI/CD pipeline.

[![](https://github.com/mailosaur/mailosaur-python/workflows/CI/badge.svg)](https://github.com/mailosaur/mailosaur-python/actions)

## Installation

```
pip install --upgrade mailosaur
```

## Documentation

Please see the [Python client reference](https://mailosaur.com/docs/email-testing/python/client-reference/) for the most up-to-date documentation.

## Usage

example.py

```python
from mailosaur import MailosaurClient
mailosaur = MailosaurClient("YOUR_API_KEY")

result = mailosaur.servers.list()

print("You have a server called: " + result.items[0]["name"])
```

## Development

You must have the following prerequisites installed:

* [pip](https://pip.pypa.io/en/stable/installing/)
* [nose](https://nose.readthedocs.io/en/latest/)

Install all development dependencies:

```sh
pip install -r requirements.txt
```

The test suite requires the following environment variables to be set:

```sh
export MAILOSAUR_BASE_URL=https://mailosaur.com/
export MAILOSAUR_API_KEY=your_api_key
export MAILOSAUR_SERVER=server_id
```

Run all tests:

```sh
nosetests
```

## Contacting us

You can get us at [support@mailosaur.com](mailto:support@mailosaur.com)
