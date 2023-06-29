# **Humaitas Events PP5 API**

**Developer: Shubham Sinha**

💻 [Live link](https://pp5-api-ref.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the Humanitas Events front-end application

## Table of Contents

- [Project Structure](#project-structure)
  - [Code Structure](#code-structure)
- [User Stories](#user-stories)
  - [Profiles](#profiles)
  - [Events](#events)
  - [Comments](#comments)
  - [Interested](#interested)
  - [Join](#join)
  - [Followers](#followers)
- [Technologies Used](#technologies-used)
- [Agile Design](#agile-design)
- [Database Design](#database-design)
  - [Models](#models)
    - [User Model](#user-model)
    - [Profile Model](#profile-model)
    - [Event Model](#event-model)
    - [Comment Model](#comment-model)
    - [Interested Model](#interested-model)
    - [Join Model](#join-model)
    - [Followers Model](#followers-model)
- [Features](#features)
- [Validation](#validation)
  - [Python](#python)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Thank You](#thank-you)

## Project Structure

The overall structure of the project was made with the help of Code Institute walkthrough project [drf-api](https://github.com/Code-Institute-Solutions/drf-api) including models, views and serializers.

### Code Structure

Project code structure is organized and divided into various application folders and constructed using Django Rest Framework

#### Project Apps

- **profile app**: This app contains model, views, serializers, tests and urls for profile
- **events app**: This app contains model, views, serializers, tests and urls for events
- **comments app**: This app contains model, views, serializers, tests and urls for comments
- **interested app**: This app contains model, views, serializers, tests and urls for interested
- **join app**: This app contains model, views, serializers, tests and urls for join
- **followers app**: This app contains model, views, serializers, tests and urls for followers

#### Other django apps

- **settings.py**: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- **Procfile**: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- **requirements.txt**: This file lists the dependencies required for the Django project to run.
- **env.py**: This file is used to store environment variables for a Django project or application, such as database connection details or API keys.

## User Stories

### Profiles

1. As a site owner/developer I can view lists of profiles so that I can can see how many profiles has been created
2. As a site owner/developer I can view the details of a profile so that I can see individual profile data
3. As a site owner/developer I can update my profile so that I can change data when I want
4. As a site owner/developer I can delete profile so that I can delete profile which I don't want to continue with

### Events

5. As a site owner/developer I can view a list of all events so that I can see all events at once
6. As a site owner/developer I can view a single event so that I can view the detail of event including comment counts, interested_count and join_request
7. As a site owner/developer I can create an event so that I can share what events are upcoming
8. As a site owner/developer I can edit an event so that I can change the data with correct information
9. As a site owner/developer I can delete event so that I can remove the event not valid or cancelled

### Comments

10. As a site owner/developer I can view list of all comments so that I can see all comments for the events
11. As a site owner/developer I can retrieve a comment by its id so that I can edit/delete the comment
12. As a site owner/developer I can add comments to events so that I can interact with various people regarding an event
13. As a site owner/developer I can edit/update comment so that I can change what I have commented
14. As a site owner/developer I can delete comments on events so that I can delete unwanted comments or my written comments

### Interested

15. As a site owner/developer I can view the list of interested shown on events so that I can see all the interested created in the API for the events
16. As a site owner/developer I can retrieve interested by id so that I can be able to make changes to it
17. As a site owner/developer I can add interested functionality for events so that I can show interest for the event
18. As a site owner/developer I can delete interested functionality to event so that I can delete my interested instance if not interested anymore

### Join

19. As a site owner/developer I can view a list of join request for an event so that I can view how many request has been requested
20. As a site owner/developer I can retrieve join request so that I can make changes to it
21. As a site owner/developer I can create a join request for an event so that I can join an event
22. As a site owner/developer I can delete join request so that I can delete join request which is not approved anymore

### Followers

23. As a site owner/developer I can view a list of followers so that I can view who is following
24. As a site owner/ developer I can retrieve followers by id so that I can make changes to it
25. As a site owner/developer I can create follow so that I can follow another user
26. As a site owner/developer I can delete a follow so that I can unfollow another user

## Technologies Used

### Languages & Frameworks

- Python 3.10.2
- Django
- Django Rest Framework

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) to store images for profile and events
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files.
- [Lucidcharts](https://lucid.app/) has been used in project to design and document data model architecture.
- [CodeAnyWhere](https://app.codeanywhere.com/) was IDE used for writing code and to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku](https://heroku.com) - Cloud platform. Justification: I used this was used to deploy the project into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) - API toolkit. Justification: I used this to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) - API Module. Justification: I used this for user authentication
- [Psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adaptor. Justification: This was used as a PostgreSQL database adapter for Python
- [ElephantSQL](https://www.elephantsql.com/) - Database hosting service – Justification: This was used as the deployed project on Heroku uses an ElephantSQL database

### All libraries for deployment in Heroku

- All libraries is stored in requirements.txt for deployment in heroku

<details><summary>All libraries</summary>
<img src="images/docs/requirements.png">
</details>

##### Back to [top](#table-of-contents)

## Agile design

### About

- Agile development is the most effective way to development of any website
- This was my second attempt in agile development but I feel I made a tremendous improvement
- I was able to follow the steps and add milestones in this project

### User Story Template

- Using Github issues first I created the template for a user story that was later used to create user stories. I created four labels: must have, could have, should have.

<details><summary>See User story template</summary>
<img src="images/docs/userstorytemplate.png">
</details>

### Kanban Board

- As a visual representation of the project's status, showing what tasks are to be done, in progress and completed.Each task is represented as a card on the board, and the cards can be moved from one column to another to show progress.

[Link to project Kanban board.](https://github.com/users/Sinha5714/projects/6)

<details><summary>See Kanban board</summary>
<img src="images/docs/kanban.png">
</details>

### Moscow Prioritisation

- The Moscow prioritization technique is used to prioritize project requirements based on their importance.

<details><summary>See Image</summary>
<img src="images/docs/moscow.png">
</details>

### Milestones

- Milestones are created with a aim of finishing a task on a certain date. I have created 7 milestones for this project and linked them with issues related.

<details><summary>See Image</summary>
<img src="images/docs/milestones1.png">
</details>
<details><summary>See Image</summary>
<img src="images/docs/milestone2.png">
</details>

## Database Design

### Data Models

#### User Model

- User model as part of the Django Rest Framework dj-rest-auth library contains basic information about authenticated user and contains folowing fields:
  Username, Password, Email

#### Profile model

- Profile model is created for user to add their details and image for better interaction with the website

| Name           | Database Key   | Field Type    | Validation                                      |
| -------------- | -------------- | ------------- | ----------------------------------------------- |
| user           | user           | OneToOneField | User, on_delete=models.CASCADE                  |
| profile_pic    | profile_pic    | ImageField    | upload_to='images/', default='../avatar_zavejy' |
| name           | name           | CharField     | max_length=255 blank=True                       |
| about_me       | about_me       | TextField     | blank=True                                      |
| email          | email          | EmailField    | max_length=255 blank=True                       |
| instagram_link | instagram_link | URLField      | max_length=200 blank=True                       |
| facebook_link  | facebook_link  | URLField      | max_length=200 blank=True                       |
| phone_number   | phone_number   | IntegerField  | null=True blank=True                            |
| created_on     | created_on     | DateTimeField | auto_now_add=True                               |
| updated_on     | updated_on     | DateTimeField | auto_now_add=True                               |

#### Event model

- Event model is created for user to add events in the website
- Following categories choices were added for user to select for an event

  - EVENT_CATEGORIES = (
    ("Discrimination", "Descrimination"),
    ("LGBTQ", "LGBTQ"),
    ("Equal-Rights", "Equal Rights"),
    ("Marraige-Rights", "Marraige Rights"),
    ("Work-Rights", "Work Rights"),
    ("Education-Rights", "Education Rights"),
    )

  - EVENT_SUB_CATEGORIES = (
    ("Seminars", "Seminars"),
    ("Meet-ups", "Meet-ups"),
    ("Retreats", "Retreats"),
    )

- Following image filter choices were added for user to filter image

  - image_filter_choices = [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

| Name             | Database Key     | Field Type    | Validation                                                        |
| ---------------- | ---------------- | ------------- | ----------------------------------------------------------------- |
| user             | user             | ForeignKey    | User, on_delete=models.CASCADE                                    |
| title            | title            | CharField     | max-length=255                                                    |
| content          | content          | TextField     | max-length=255                                                    |
| image            | image            | ImageField    | upload_to='images/', default='../equal-rights_o1owqr', blank=True |
| image_filter     | image_filter     | CharField     | max_length=32, choices=image_filter_choices, default='normal'     |
| event_start_date | event_start_date | DateTimeField | blank=True, null=True                                             |
| event_end_date   | event_end_date   | DateTimeField | blank=True, null=True                                             |
| category         | category         | CharField     | max_length=50, choices=EVENT_CATEGORIES, default='Equal-Rights'   |
| sub_category     | sub_category     | CharField     | max_length=50, choices=EVENT_SUB_CATEGORIES, default='Seminars'   |
|                  |
| created_on       | created_on       | DateTimeField | auto_now_add=True                                                 |
| updated_on       | updated_on       | DateTimeField | auto_now_add=True                                                 |

#### Comment model

- Comment model was created for user to comment on an event

| Name       | Database Key | Field Type    | Validation                      |
| ---------- | ------------ | ------------- | ------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE  |
| event      | event        | ForeignKey    | Event, on_delete=models.CASCADE |
| created_on | created_on   | DateTimeField | auto_now_add=True               |
| updated_on | updated_on   | DateTimeField | auto_now_add=True               |
| content    | content      | TextField     | blank=False                     |

#### Interested model

- Interested model was created for user to show interest for an event

| Name       | Database Key | Field Type    | Validation                                                 |
| ---------- | ------------ | ------------- | ---------------------------------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE                             |
| event      | event        | ForeignKey    | Event, related_name='interested', on_delete=models.CASCADE |
| created_on | created_on   | DateTimeField | auto_now_add=True                                          |

#### Join model

- Join model was created for user to send join request for an event

| Name       | Database Key | Field Type    | Validation                                           |
| ---------- | ------------ | ------------- | ---------------------------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE                       |
| event      | event        | ForeignKey    | Event, related_name='join', on_delete=models.CASCADE |
| created_on | created_on   | DateTimeField | auto_now_add=True                                    |

#### Followers model

- Join model was created for user to send join request for an event

| Name       | Database Key | Field Type    | Validation                                                |
| ---------- | ------------ | ------------- | --------------------------------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE , related_name='following' |
| followed   | followed     | ForeignKey    | User, on_delete=models.CASCADE ,related_name='followed'   |
| created_on | created_on   | DateTimeField | auto_now_add=True                                         |

## Features

### Home Page

- This is the welcoming page for all users
- Once user opens the API site, this page appears in front of him.

<details><summary>See API Site Homepage</summary>

![API Site Homepage](images/pages/homepage.png)

</details>

- When user opens the deployed API site, this page appears in front of him.

<details><summary>See Deployed API Site Homepage</summary>

![Deployed API Site Homepage](images/pages/homepagedeployed.png)

</details>

### Profile List Page

- This page consists of profile list of all users
- **User Story Covered**: 1

<details><summary>See Profile List Page</summary>

![Profile List Page](images/pages/profilelists.png)

</details>

### Profile Detail Page

- This page consists of profile detail page
- If user is owner he can edit and delete his profile
- **User Story Covered**: 2, 3, 4

<details><summary>See Profile Detail Page</summary>

![Profile Detail Page](images/pages/profiledetail.png)

</details>

<details><summary>See Profile Owner Detail Page</summary>

![Profile Owner Detail Page](images/pages/profileloggedindetail.png)

</details>

### Event List Page

- This page consists of event list of all events which have been posted
- This page also consist a event create form for logged in user
- **User Story Covered**: 5, 7

<details><summary>See Event List Page</summary>

![Event List Page](images/pages/eventlist.png)

</details>

<details><summary>See Event List - Create Form </summary>

![Event List - Create Form](images/pages/eventcreatelist.png)

</details>

### Event Detail Page

- This page consists of event detail
- If user is owner he can edit and delete his event what he has posted
- **User Story Covered**: 6, 8, 9

<details><summary>See Event Detail Page</summary>

![Event Detail Page](images/pages/eventdetail.png)

</details>

<details><summary>See Event Owner Edit Form</summary>

![Event Owner Edit Form](images/pages/evendetailform.png)

</details>

### Comment List Page

- This page consists of comment list of all comments posted for events
- This page also consist a comment create form for logged in user with event options
- **User Story Covered**: 10, 12

<details><summary>See Comment List Page</summary>

![Comment List Page](images/pages/commentlist.png)

</details>

<details><summary>See Comment List - Create Form </summary>

![Comment List - Create Form](images/pages/commentlistcreate.png)

</details>

### Comment Detail Page

- This page consists of comment detail
- If user is owner he can edit and delete his comments what he has posted
- **User Story Covered**: 11, 13, 14

<details><summary>See Comment Detail Page with Edit form</summary>

![Comment Detail Page](images/pages/commentdetail.png)

</details>

### Interested List Page

- This page consists of interested list of all interests shown for events
- This page also consist a interested create form for logged in user with event options
- If user want to show interest again a validation error is thrown
- **User Story Covered**: 15, 17

<details><summary>See Interested List Page with Create Form</summary>

![Interested List Page with Create Form](images/pages/interestedlistloggedin.png)

</details>

<details><summary>See Interested List Page with Error</summary>

![Interested List Page with Error](images/pages/interestedlisterror.png)

</details>

### Interested Detail Page

- This page consists of interested detail
- If user has shown interest he can delete his interest
- **User Story Covered**: 16, 18

<details><summary>See Interested Detail Page</summary>

![Interested Detail Page](images/pages/interesteddetail.png)

</details>

### Join List Page

- This page consists of join list of all join request sent for events
- This page also consist a join create form for logged in user with event options
- If user want to send join request again a validation error is thrown
- **User Story Covered**: 19, 21

<details><summary>See Join List Page</summary>

![Join List Page](images/pages/joinlist.png)
![Join List Page with Create Form](images/pages/joinlistloggedin.png)

</details>

<details><summary>See Join List Page with Error</summary>

![Join List Page with Error](images/pages/joinlisterror.png)

</details>

### Join Detail Page

- This page consists of join detail
- If user has sent request he can delete his request
- **User Story Covered**: 20, 22

<details><summary>See Join Detail Page</summary>

![Join Detail Page](images/pages/joindetail.png)

</details>

### Followers List Page

- This page consists of followers list of all user following each other
- This page also consist a followers create form for logged in user with other users options
- If user want to follow a followed user again a validation error is thrown
- **User Story Covered**: 23, 25

<details><summary>See Follower List Page with Create Form</summary>

![Follower List Page with Create Form](images/pages/followerlistform.png)

</details>

<details><summary>See Follower List Page with Error</summary>

![Follower List Page with Error](images/pages/followerlisterror.png)

</details>

### Followers Detail Page

- This page consists of followers detail
- If user has followed another user he can delete his follow
- **User Story Covered**: 24, 26

<details><summary>See Followers Detail Page</summary>

![Follow Detail Page](images/pages/followerdetail.png)

</details>

## Validation

### Python

- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files.
- NOTE: The validation was done to all custom python files written by me. Settings.py and env.py was excluded because it contains important data which is longer than 79 lines and cannot be changed.

#### pp5_api Project

<details><summary>Views</summary>
<img src="images/python-test/pp5-views.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/pp5-urls.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/pp5-serializers.png" >
</details>

<details><summary>Permissions</summary>
<img src="images/python-test/pp5-permissions.png" >
</details>

##### Profiles App

<details><summary>Models</summary>
<img src="images/python-test/profile-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/profile-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/profile-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/profile-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/profile-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/profile-tests.png" >
</details>

##### Events App

<details><summary>Models</summary>
<img src="images/python-test/events-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/events-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/events-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/events-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/events-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/events-tests.png" >
</details>

##### Comments App

<details><summary>Models</summary>
<img src="images/python-test/comment-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/comment-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/comment-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/comment-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/comment-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/comment-tests.png" >
</details>

##### Interested App

<details><summary>Models</summary>
<img src="images/python-test/interested-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/interested-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/interested-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/interested-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/interested-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/interested-test.png" >
</details>

##### Join App

<details><summary>Models</summary>
<img src="images/python-test/join-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/join-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/join-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/join-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/join-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/join-test.png" >
</details>

##### Followers App

<details><summary>Models</summary>
<img src="images/python-test/follower-model.png" >
</details>

<details><summary>Views</summary>
<img src="images/python-test/follower-views.png" >
</details>

<details><summary>Admin</summary>
<img src="images/python-test/follower-admin.png" >
</details>

<details><summary>Serializers</summary>
<img src="images/python-test/follower-serializers.png" >
</details>

<details><summary>Urls</summary>
<img src="images/python-test/follower-urls.png" >
</details>

<details><summary>Tests</summary>
<img src="images/python-test/follower-test.png" >
</details>

## Testing

- Testing of the website can be [seen here](https://github.com/Sinha5714/pp5-api-ref/blob/main/TESTING.md)

## Deployment

### Creating Database using ElephantSQL

1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.

<details><summary>See Image</summary>

![Create Instance](images/docs/create-instance.png)

</details>

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

<details><summary>See Image</summary>

![ElephantSQL Tiny-Turtle](images/docs/tiny-turtlr.png)

</details>

3. Select your preferred region and create the database instance.

- After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.

<details><summary>See Image</summary>

![ElephantSQL](images/docs/postgreSQL-url.png)

</details>

### Deploying the website in Heroko

- Before deploying in Heroku following files were created:
  1. env.py : stores confidential data eg. API keys, passwords etc.

<details><summary>See Image</summary>

![env.py](images/docs/env-py.png)

</details>

2. Procfile : Very important for deployment and must be added with capital P

<details><summary>See Image</summary>

![Procfile](images/docs/procfile.png)

</details>
  
  3. Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project

<details><summary>See Image</summary>

![Requirements.txt](images/docs/requirements.png)

</details>

- The website was deployed to Heroko using following steps:

#### Login or create an account at Heroku

- Make an account in Heroko and login

<details>
    <summary>Heroko Login Page</summary>
    <img src="images/docs/heroku_login.png" alt="Heroko login page">
</details>

#### Creating an app

- Create new app in the top right of the screen and add an app name.
- Select region
- Then click "create app".

<details>
    <summary>Create App</summary>
    <img src="images/docs/createapp.png" alt="Heroko create app screenshot">
</details>

#### Open settings Tab

##### Click on config var

- Store CLOUDINARY_URL file from in key and add the values
- Store DATABASE_URL file from in key and add the values
- Store SECRET_KEY file from in key and add the values
- Store ALLOWED_HOST in key and add the value
- Store DISABLE_COLLECTSTATIC in key and add the value

NOTE: For initial deployment DISABLE_COLLECTSTATIC was also added

<details>
    <summary>Config var</summary>
    <img src="images/docs/config-var.png" alt="Config var screenshot">
</details>

##### Add Buildpacks

- Add python buildpack first
- Add Nodejs buildpack after that

<details>
    <summary>Buildpacks</summary>
    <img src="images/docs/buildpacks.png" alt="Buildpacks screenshot">
</details>

#### Open Deploy Tab

##### Choose deployment method

- Connect GITHUB
- Login if prompted

<details>
    <summary>Deployment method</summary>
    <img src="images/docs/method.png" alt="Deployment method screenshot">
</details>

##### Connect to Github

- Choose repositories you want to connect
- Click "Connect"

<details>
    <summary> Repo Connect</summary>
    <img src="images/docs/repo-connect.png" alt="Repo connect screenshot">
</details>

##### Automatic and Manual deploy

- Choose a method to deploy
- After Deploy is clicked it will install various file

<details>
    <summary> Deploy methods</summary>
    <img src="images/docs/deploy.png" alt="deploy method screenshot">
</details>

##### Deployment

- Project was deployed in Heroku

<details>
    <summary>Deployed Website</summary>
    <img src="images/pages/homepagedeployed.png" alt="deployed">
</details>

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
4. [GitHub Repository](https://github.com/Sinha5714/pp5-api-ref)

### Cloning the repository in GitHub

1. Visit the GitHub page of the website's repository
2. Click the “Clone” button on top of the page
3. Click on “HTTPS”
4. Click on the copy button next to the link to copy it
5. Open your IDE
6. Type `git clone <copied URL>` into the terminal

## Credits

### Code

- The code was written with the help of Code Institute walkthrough project [drf-api](https://github.com/Code-Institute-Solutions/drf-api)

## Thank You

- to my mentor Mo Shami for supporting me with his feedback through the entire project
- special thanks to my husband Remo Liebetrau to help me in manual testing of the user stories
- to Code Institute and Slack community for helping me when I was getting stuck with some challenges.
