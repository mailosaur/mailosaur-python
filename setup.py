from setuptools import setup

setup(name='mailosaur',
      version='5.0.0',
      description='Python client library for Mailosaur',
      url='https://mailosaur.com',
      author='Mailosaur Ltd',
      author_email='code@mailosaur.com',
      keywords='email automation testing selenium robot framework',
      license='MIT',
      packages=['mailosaur'],
      install_requires=[
          'msrestazure'
      ],
      zip_safe=False, requires=['msrestazure'])

