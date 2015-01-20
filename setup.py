from setuptools import setup, find_packages

setup(
      name='validate_email',
      version = '1.2',
      download_url = 'git@github.com:mathieurodic/validate_email.git',
      py_modules = ('validate_email',),
      author = 'Mathieu Rodic',
      author_email = 'mathieu@rodic.Fr',
      description = 'Validate_email verify if an email address is valid and really exists.',
      long_description=open('README.rst').read(),
      keywords = 'email validation verification mx verify',
      url = 'https://github.com/mathieurodic/validate_email',
      license = 'GPL',
      install_requires=[
            'dnspython3',
      ],
)
