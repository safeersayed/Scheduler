# python == 3.7.7
# django == 3.0.3
# create a virtual environment [anaconda]
# install requirements from requirements.txt
# Make the table structure and migrate
# run the project
# For api details check api_details.txt file.

# Scheduler Demo App
An app for scheduling time-slots based on available time.

## Getting Started

The project includes django rest APIs.

## Built With
* [Python]() - 3.7.7
* [Django](https://docs.djangoproject.com/) - 3.0.3
* [Django-Rest-Framework](https://www.django-rest-framework.org/)

## Installation

1. Clone this Git repository
2. Install requirements `pip install -r requirements.txt'
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`

## Deployment

Currently cofigured to run it on local machine - `http://localhost:8000/. 

## Demo

1. Register User

URL: http://localhost:8000/user/add-user/

TYPE: POST

INPUT

FORM DATA:

email: <email-id>
user_category: <user type>[values: INTERVIEWER/CANDIDATE]
available_date: <available date>[Format: YYYY-MM-DD]
available_time_from: <time that user available from> [ 24hr time format eg: 13:30]
available_time_to: <time that user available to> [ 24hr time format eg: 10:00]

OUTPUT
{
    "status": 201,
    "message": "New post added successfully",
    "data": {
        "email": "",
        "user_category": "INTERVIEWER/CANDIDATE",
        "available_date": "",
        "available_time_from": "",
        "available_time_to": ""
    }
}

2. Get the time-slots

URL : http://localhost:8000/scheduler/schedule-list/?interviewer_id=&candidate_id=

TYPE: GET

INPUT

PARAMS:

interviewer_id: interviewer email address
candidate_id: candidate email address


OUTPUT

{
    "status": 200,
    "message": "Details fetched successfully",
    "interviewer_details": {
        "email": "",
        "user_category": "INTERVIEWER",
        "available_date": "2020-06-10",
        "time_slots": []
    },
    "candidate_details": {
        "email": "",
        "user_category": "CANDIDATE",
        "available_date": "",
        "time_slots": []
    }
}
