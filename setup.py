from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mailosaur',
    version='7.0.0',
    description='The Mailosaur Python library lets you integrate email and SMS testing into your continuous integration process.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mailosaur Ltd',
    author_email='code@mailosaur.com',
    url='https://github.com/mailosaur/mailosaur-python',
    license='MIT',
    keywords='email sms testing automation selenium robot framework',
    packages=find_packages(),
    zip_safe=False, requires=['requests'],
    install_requires=[
        'python-dateutil',
        'tzlocal',
        'requests',
        'requests[security]'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    tests_require=[
        'nose >= 1.3'
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/mailosaur/mailosaur-python/issues',
        'Documentation': 'https://mailosaur.com/docs/email-testing/python/',
        'Source Code': 'https://github.com/mailosaur/mailosaur-python',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
