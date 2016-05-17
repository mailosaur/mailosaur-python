from setuptools import setup

setup(name='mailosaur',
      version='3.0.1',
      description='Python client library for Mailosaur',
      url='https://mailosaur.com',
      author='Clickity Ltd',
      author_email='support@mailosaur.com',
      keywords='email automation testing selenium robot framework',
      license='MIT',
      packages=['mailosaur'],
      install_requires=[
          'python-dateutil',
          'requests',
          'requests[security]'
      ],
      zip_safe=False, requires=['requests'])

