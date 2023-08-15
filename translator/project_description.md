** Project Description: Translate API using Django Rest Framework

This project involves the creation of a REST API using Django Rest Framework for text translation. The API utilizes the Google Translate library to enable the translation of words, phrases, and paragraphs between different languages. The translated data is stored in a PostgreSQL database to allow quick retrieval and minimize translation redundancy.
___________________________________________________________________

** Requirements:

Python 3.10.5
Django 4.2.4
Django Rest Framework 3.14.0
psycopg2-binary 2.9.7
googletrans==3.1.0a0

_____________________________________________________________________

** Installation and Setup

1 Clone the Project Repository:

git clone <repository-url>

2 Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate

3 Install Required Packages:

pip install -r requirements.txt

4 Configure PostgreSQL Database and Apply migrations :

Update database settings in settigs.py (name,user,password,host,port)
python manage.py makemigrations
python manage.py migrate

5 Run server

python manage.py runserver

____________________________________________________________________________

** Project API usage

To translate text, make a POST request to translator/translate/ with the following JSON data:
{
  "text": "Hello",
  "source": "en",
  "target": "fr"
}

To retrieve a specific translation, make a GET request to translator/translate/ with query parameters text, source, and target.

To retrieve all translations, make a GET request to translator/translate/ without any query parameters.

___________________________________________________________________________

** Testing API

Run test cases from tests.py using below command:

python manage.py test translator.tests

_____________________________________________________________________________