from setuptools import setup, find_packages

setup(name='mailosaur',
      version='7.0.0',
      description='Python client library for Mailosaur',
      url='https://mailosaur.com',
      author='Mailosaur Ltd',
      author_email='code@mailosaur.com',
      keywords='email automation testing selenium robot framework',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'python-dateutil',
          'tzlocal',
          'requests',
          'requests[security]'
      ],
      zip_safe=False, requires=['requests'])

