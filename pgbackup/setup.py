# Writing Our setup.py
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='jgyy',
    author_email='jgyy@linux.com',
    packages=find_packages('pgbackup'),
    package_dir={'': 'pgbackup'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)
