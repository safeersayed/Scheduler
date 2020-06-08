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
2. Install requirements `pip install -r requirements.txt`
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`

## Deployment

Currently cofigured to run it on local machine - `http://localhost:8000/`. 

## Demo

1. Register User API

* URL: `http://localhost:8000/user/add-user/`

* TYPE: POST

* INPUT DATA:

`email: <email-id><br/>
user_category: <user type>[values: INTERVIEWER/CANDIDATE]<br/>
available_date: <available date>[Format: YYYY-MM-DD]<br/>
available_time_from: <time that user available from> [ 24hr time format eg: 13:30]<br/>
available_time_to: <time that user available to> [ 24hr time format eg: 10:00]`

* OUTPUT
`{
    "status": 201,<br/>
    "message": "New post added successfully",<br/>
    "data": {<br/>
        "email": "",<br/>
        "user_category": "INTERVIEWER/CANDIDATE",<br/>
        "available_date": "",<br/>
        "available_time_from": "",<br/>
        "available_time_to": ""<br/>
    }
}`

2. Get the time-slots API

* URL : `http://localhost:8000/scheduler/schedule-list/?interviewer_id=&candidate_id=`

* TYPE: GET

* INPUT PARAMS:

`interviewer_id: interviewer email address <br/>
candidate_id: candidate email address`


* OUTPUT:

`{
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
}`
