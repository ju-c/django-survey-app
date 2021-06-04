# Django Survey App

A survey app where users can create surveys and send them out to other people.
When the survey is complete, the survey's creator can see what percentage of people answered each question.
Written in Django. Hosted at Heroku : [Click here to test Django Survey App.](https://limitless-retreat-14624.herokuapp.com/)


# User journeys

**Survey creator user journey:**

```mermaid
graph LR
A(Home)
A--> B(Sign Up)
A --> C(Log In)
B --> D{List of surveys}
C --> D
D --> E(Create Survey)
E --> F(Add Question)
F --> G(Add Option)
G --> H(Send out survey)
D --> I(Edit Survey)
I --> F
D --> J(Delete survey)
D --> K(View results)
```
**Survey taker user journey:**

```mermaid
graph LR
A(Start survey)
A --> B(Answer questions)
B --> C(Submit answers)
```
