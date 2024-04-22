
# this file contains the metadata and instructions for installing this project through pip

from setuptools import setup,find_packages
setup(
    name='telecom_user_analysis',
    version='1.0',
    author='Biniyam Teshome',
    author_email='se.biniyam.teshome@gmail.com',
    description='Telecommunication User Analysis Project',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'psycopg2',
        'pandas',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'telecom_user_analysis=app.app:main'
        ]
    }
)