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
