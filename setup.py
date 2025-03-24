# setup.py

from setuptools import setup, find_packages

setup(
    name='email-automation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'smtplib',  # For email sending
        'email',  # For MIME support
    ],
    author='purushothamCN',
    author_email='purushothamputtu9@gmail.com',
    description='A simple email automation library for sending emails',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/purushothamCN/email_automation.git',  # Update with your GitHub link
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
