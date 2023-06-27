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
- [Technologies Used](#technologies-used)
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

## Project Structure

The overall structure of the project was made with the help of Code Institute walthrough project [drf-api](https://github.com/Code-Institute-Solutions/drf-api) including models, views and serializers.

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

23. As a site owner/developer I can view a list of followers so that I can view who is following whom
24. As a site owner/developer I can create follow so that I can follow another user
25. As a site owner/developer I can delete a follow so that I can unfollow another user

## Technologies Used

### Languages & Frameworks

- Python 3.10.2
- Django Rest Framework

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) to store images for profile and events
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files.
- [Lucidcharts](https://lucid.app/) has been used in project to design and document data model architecture.
- [CodeAnyWhere](https://app.codeanywhere.com/) was IDE used for writing code and to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code

### All libraries for deployment in Heroku

- All libraries is stored in requirements.txt for deployment in heroku

<details><summary>All libraries</summary>
<img src="images/docs/requirements.png">
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

<details><summary>See Profile List Page</summary>

![Profile List Page](images/pages/profilelists.png)

</details>

### Profile Detail Page

- This page consists of profile detail page
- If user is owner he can edit and delete his profile

<details><summary>See Profile Detail Page</summary>

![Profile Detail Page](images/pages/profiledetail.png)

</details>

<details><summary>See Profile Owner Detail Page</summary>

![Profile Owner Detail Page](images/pages/profileloggedindetail.png)

</details>

### Event List Page

- This page consists of event list of all events which have been posted
- This page also consist a event create form for logged in user

<details><summary>See Event List Page</summary>

![Event List Page](images/pages/eventlist.png)

</details>

<details><summary>See Event List - Create Form </summary>

![Event List - Create Form](images/pages/eventcreatelist.png)

</details>

### Event Detail Page

- This page consists of event detail
- If user is owner he can edit and delete his event what he has posted

<details><summary>See Event Detail Page</summary>

![Event Detail Page](images/pages/eventdetail.png)

</details>

<details><summary>See Event Owner Edit Form</summary>

![Event Owner Edit Form](images/pages/evendetailform.png)

</details>

### Comment List Page

- This page consists of comment list of all comments posted for events
- This page also consist a comment create form for logged in user with event options

<details><summary>See Comment List Page</summary>

![Comment List Page](images/pages/commentlist.png)

</details>

<details><summary>See Comment List - Create Form </summary>

![Comment List - Create Form](images/pages/commentlistcreate.png)

</details>

### Comment Detail Page

- This page consists of comment detail
- If user is owner he can edit and delete his comments what he has posted

<details><summary>See Comment Detail Page with Edit form</summary>

![Comment Detail Page](images/pages/commentdetail.png)

</details>

### Interested List Page

- This page consists of interested list of all interests shown for events
- This page also consist a interested create form for logged in user with event options
- If user want to show interest again a validation error is thrown

<details><summary>See Interested List Page with Create Form</summary>

![Interested List Page with Create Form](images/pages/interestedlistloggedin.png)

</details>

<details><summary>See Interested List Page with Error</summary>

![Interested List Page with Error](images/pages/interestedlisterror.png)

</details>

### Interested Detail Page

- This page consists of interested detail
- If user has shown interest he can delete his interest

<details><summary>See Interested Detail Page</summary>

![Interested Detail Page](images/pages/interesteddetail.png)

</details>

### Join List Page

- This page consists of join list of all join request sent for events
- This page also consist a join create form for logged in user with event options
- If user want to send join request again a validation error is thrown

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

<details><summary>See Join Detail Page</summary>

![Join Detail Page](images/pages/joindetail.png)

</details>

### Followers List Page

- This page consists of followers list of all user following each other
- This page also consist a followers create form for logged in user with other users options
- If user want to follow a followed user again a validation error is thrown

<details><summary>See Follower List Page with Create Form</summary>

![Follower List Page with Create Form](images/pages/followerlistform.png)

</details>

<details><summary>See Follower List Page with Error</summary>

![Follower List Page with Error](images/pages/followerlisterror.png)

</details>

### Followers Detail Page

- This page consists of followers detail
- If user has followed another user he can delete his follow

<details><summary>See Followers Detail Page</summary>

![Follow Detail Page](images/pages/followerdetail.png)

</details>
