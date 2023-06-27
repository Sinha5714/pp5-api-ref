# **Humaitas Events PP5 API**

**Developer: Shubham Sinha**

💻 [Live link](https://pp5-api-ref.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the Humanitas Events front-end application

## Table of Contents

- [Project Structure](#project-structure)
  - [User Stories](#user-stories)
    - [Profiles](#profiles)
    - [Events](#events)
    - [Comments](#comments)
    - [Interested](#interested)
    - [Join](#join)
    - [Followers](#followers)

## User Stories

### Profiles

- As a site owner/developer I can view lists of profiles so that I can can see how many profiles has been created
- As a site owner/developer I can view the details of a profile so that I can see individual profile data
- As a site owner/developer I can update my profile so that I can change data when I want
- As a site owner/developer I can delete profile so that I can delete profile which I don't want to continue with

### Events

- As a site owner/developer I can view a list of all events so that I can see all events at once
- As a site owner/developer I can view a single event so that I can view the detail of event including comment counts, interested_count and join_request
- As a site owner/developer I can create an event so that I can share what events are upcoming
- As a site owner/developer I can edit an event so that I can change the data with correct information
- As a site owner/developer I can delete event so that I can remove the event not valid or cancelled

### Comments

- As a site owner/developer I can view list of all comments so that I can see all comments for the events
- As a site owner/developer I can retrieve a comment by its id so that I can edit/delete the comment
- As a site owner/developer I can add comments to events so that I can interact with various people regarding an event
- As a site owner/developer I can edit/update comment so that I can change what I have commented
- As a site owner/developer I can delete comments on events so that I can delete unwanted comments or my written comments

### Interested

- As a site owner/developer I can view the list of interested shown on events so that I can see all the interested created in the API for the events
- As a site owner/developer I can retrieve interested by id so that I can be able to make changes to it
- As a site owner/developer I can add interested functionality for events so that I can show interest for the event
- As a site owner/developer I can delete interested functionality to event so that I can delete my interested instance if not interested anymore

### Join

- As a site owner/developer I can view a list of join request for an event so that I can view how many request has been requested
- As a site owner/developer I can retrieve join request so that I can make changes to it
- As a site owner/developer I can create a join request for an event so that I can join an event
- As a site owner/developer I can delete join request so that I can delete join request which is not approved anymore

### Followers

- As a site owner/developer I can view a list of followers so that I can view who is following whom
- As a site owner/developer I can create follow so that I can follow another user
- As a site owner/developer I can delete a follow so that I can unfollow another user

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
    ("LQBTQ", "LGBTQ"),
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
| image_filter     | image_filter     | CharField     | max_length=32, choices=image_filter_choices, default='Normal'     |
| event_start_date | event_start_date | DateTimeField | blank=True, null=True                                             |
| event_end_date   | event_end_date   | DateTimeField | blank=True, null=True                                             |
| category         | category         | CharField     | max_length=50, choices=EVENT_CATEGORIES, default='Equal-Rights'   |
| sub_category     | sub_category     | CharField     | max_length=50, choices=EVENT_SUB_CATEGORIES, default='Seminars'   |
|                  |
| created_on       | created_on       | DateTimeField | auto_now_add=True                                                 |
| updated_on       | updated_on       | DateTimeField | auto_now_add=True                                                 |

#### Comments model

- Comments model was created for user to comment on an event

| Name       | Database Key | Field Type    | Validation                      |
| ---------- | ------------ | ------------- | ------------------------------- |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE  |
| event      | event        | ForeignKey    | Event, on_delete=models.CASCADE |
| created_on | created_on   | DateTimeField | auto_now_add=True               |
| updated_on | updated_on   | DateTimeField | auto_now_add=True               |
| content    | content      | TextField     | blank=False                     |
