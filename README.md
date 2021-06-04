# Django Survey App
![Django survey app](docs/django_survey_app.jpg?raw=true)

[Click here to test Django Survey App](https://limitless-retreat-14624.herokuapp.com/)!

A survey app where users can create surveys and send them out to other people.
When the survey is complete, the survey's creator can see what percentage of people answered each question.
Written in Django. Based on this [blog post](https://mattsegal.dev/django-survey-project.html) by Matt Segal.
# User journeys
**Survey creator user journey:**
![Survey creator user journey](docs/survey_creator_user_journey.jpg?raw=true) 

**Survey taker user journey:**
![Survey taker user journey](docs/survey_taker_user_journey.jpg?raw=true)
# Setup
Requires Docker.  
#### Setup database
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py runserver
```
####Setup Github OAuth:
To configure a new OAuth application on Github, go to https://github.com/settings/applications/new.`
Then:  
- Go to your admin page (yoursite.com/anyminutenow/)  
- Go to the "Sites" portion and set your correct domain name
- Go back to the admin homepage and click on the add button for Social Applications
- Select "Github", add a name then the "Client ID" and "Secret ID" from Github
- Add your site to the "Chosen sites"
