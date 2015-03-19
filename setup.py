from setuptools import setup

setup(name='mailosaur',
      version='0.1',
      description='Package containing python bindings for the mailosaur.com mail testing API.',
      url='http://mailosaur.com/',
      author='Clickity Ltd',
      author_email='support@mailosaur.com',
      keywords='email automation testing selenium robot framework',
      license='MIT',
      packages=['mailosaur'],
      install_requires=[
          'requests',
          'requests[security]'
      ],
      zip_safe=False, requires=['requests'])

