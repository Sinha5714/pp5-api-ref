# TESTING

## Table of Contents

1. [Manual Testing](#manual-testing-of-user-stories)
2. [Automated Testing](#automated-testing)
3. [Bugs](#bugs)
4. [Unfixed Bugs](#unfixed-bugs)

### Manual testing of user stories

1. As a site owner/developer I can view lists of profiles so that I can can see how many profiles has been created

| **Step**                              | **Expected Result**             | **Actual Result** |
| ------------------------------------- | ------------------------------- | ----------------- |
| Add "/profiles" in deployed url       | profile list page opens         | Work as expected  |
| User scrolls through the profile list | profiles of users are displayed | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory1.png" >

</details>

2. As a site owner/developer I can view the details of a profile so that I can see individual profile data

| **Step**                           | **Expected Result**       | **Actual Result** |
| ---------------------------------- | ------------------------- | ----------------- |
| Add "/profiles/id" in deployed url | profile detail page loads | Work as expected  |

 <details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory2.png" >

</details>

3. As a site owner/developer I can update my profile so that I can change data when I want

| **Step**                                                  | **Expected Result**                      | **Actual Result** |
| --------------------------------------------------------- | ---------------------------------------- | ----------------- |
| User log in                                               | logged in status is shown in top right   | Work as expected  |
| Add "/profiles/id" in deployed url (id of user's profile) | profile detail page loads with edit form | Work as expected  |
| User update the data and click on put                     | updated data is shown in profile list    | Work as expected  |

 <details><summary>Screenshots</summary>
<img src="images/manualtesting/userstory3-1.png" >
<img src="images/manualtesting/userstory3-2.png" >

</details>

4. As a site owner/developer I can delete profile so that I can delete profile which I don't want to continue with

| **Step**                                                  | **Expected Result**                          | **Actual Result** |
| --------------------------------------------------------- | -------------------------------------------- | ----------------- |
| User log in                                               | logged in status is shown in top right       | Work as expected  |
| Add "/profiles/id" in deployed url (id of user's profile) | profile detail page loads with delete button | Work as expected  |
| User clicks on delete button                              | a modal confirming delete occurs             | Work as expected  |
| User clicks on delete button                              | profile is deleted                           | Work as expected  |

 <details><summary>Screenshots</summary>
<img src="images/manualtesting/userstory4-1.png" >
<img src="images/manualtesting/userstory4-2.png" >
<img src="images/manualtesting/userstory4-3.png" >

</details>

5. As a site owner/developer I can view a list of all events so that I can see all events at once

| **Step**                             | **Expected Result**    | **Actual Result** |
| ------------------------------------ | ---------------------- | ----------------- |
| Add "/events" in deployed url        | events list page opens | Work as expected  |
| User scrolls through the events list | events are displayed   | Work as expected  |

<details><summary>Screenshots</summary>
<img src="images/manualtesting/userstory5.png" >

</details>

6. As a site owner/developer I can view a single event so that I can view the detail of event including comment counts, interested_count and join_request

| **Step**                         | **Expected Result**      | **Actual Result** |
| -------------------------------- | ------------------------ | ----------------- |
| Add "/events/id" in deployed url | events detail page loads | Work as expected  |

 <details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory6.png" >

</details>

7. As a site owner/developer I can create an event so that I can share what events are upcoming

| **Step**                            | **Expected Result**                      | **Actual Result** |
| ----------------------------------- | ---------------------------------------- | ----------------- |
| User log in                         | logged in status is shown in top right   | Work as expected  |
| Add "/events" in deployed url       | events lists page loads with create form | Work as expected  |
| User add the data and click on post | new event is shown in events list        | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory7-1.png" >
<img src="images/manualtesting/userstory7-2.png" >

</details>

8. As a site owner/developer I can edit an event so that I can change the data with correct information

| **Step**                                              | **Expected Result**                    | **Actual Result** |
| ----------------------------------------------------- | -------------------------------------- | ----------------- |
| User log in                                           | logged in status is shown in top right | Work as expected  |
| Add "/events/id" in deployed url (id of user's event) | event detail page loads with edit form | Work as expected  |
| User update the data and click on put                 | updated data is shown in events list   | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory8-1.png" >
<img src="images/manualtesting/userstory8-2.png" >

</details>

9. As a site owner/developer I can delete event so that I can remove the event not valid or cancelled

| **Step**                                              | **Expected Result**                        | **Actual Result** |
| ----------------------------------------------------- | ------------------------------------------ | ----------------- |
| User log in                                           | logged in status is shown in top right     | Work as expected  |
| Add "/events/id" in deployed url (id of user's event) | event detail page loads with delete button | Work as expected  |
| User clicks on delete button                          | a modal confirming delete occurs           | Work as expected  |
| User clicks on delete button                          | event is deleted                           | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory9-1.png" >
<img src="images/manualtesting/userstory9-2.png" >
<img src="images/manualtesting/userstory9-3.png" >

</details>

10. As a site owner/developer I can view list of all comments so that I can see all comments for the events

| **Step**                               | **Expected Result**      | **Actual Result** |
| -------------------------------------- | ------------------------ | ----------------- |
| Add "/comments" in deployed url        | comments list page opens | Work as expected  |
| User scrolls through the comments list | comments are displayed   | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory10.png" >

</details>

11. As a site owner/developer I can retrieve a comment by its id so that I can edit/delete the comment

| **Step**                           | **Expected Result**       | **Actual Result** |
| ---------------------------------- | ------------------------- | ----------------- |
| Add "/comments/id" in deployed url | comment detail page loads | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory11.png" >

</details>

12. As a site owner/developer I can add comments to events so that I can interact with various people regarding an event

| **Step**                            | **Expected Result**                       | **Actual Result** |
| ----------------------------------- | ----------------------------------------- | ----------------- |
| User log in                         | logged in status is shown in top right    | Work as expected  |
| Add "/comments" in deployed url     | comment lists page loads with create form | Work as expected  |
| User add the data and click on post | comment is shown in comments list         | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory12-1.png" >
<img src="images/manualtesting/userstory12-2.png" >

</details>

13. As a site owner/developer I can edit/update comment so that I can change what I have commented

| **Step**                                                  | **Expected Result**                      | **Actual Result** |
| --------------------------------------------------------- | ---------------------------------------- | ----------------- |
| User log in                                               | logged in status is shown in top right   | Work as expected  |
| Add "/comments/id" in deployed url (id of user's comment) | comment detail page loads with edit form | Work as expected  |
| User update the data and click on put                     | updated data is shown in comments list   | Work as expected  |

<details><summary>Screenshots</summary>
<img src="images/manualtesting/userstory13-1.png" >
<img src="images/manualtesting/userstory13-2.png" >

</details>

14. As a site owner/developer I can delete comments on events so that I can delete unwanted comments or my written comments

| **Step**                                                  | **Expected Result**                          | **Actual Result** |
| --------------------------------------------------------- | -------------------------------------------- | ----------------- |
| User log in                                               | logged in status is shown in top right       | Work as expected  |
| Add "/comments/id" in deployed url (id of user's comment) | comment detail page loads with delete button | Work as expected  |
| User clicks on delete button                              | a modal confirming delete occurs             | Work as expected  |
| User clicks on delete button                              | comment is deleted                           | Work as expected  |

<details><summary>Screenshots</summary>
<img src="images/manualtesting/userstory14-1.png" >
<img src="images/manualtesting/userstory14-2.png" >
<img src="images/manualtesting/userstory14-3.png" >

</details>

15. As a site owner/developer I can view the list of interested shown on events so that I can see all the interested created in the API for the events

| **Step**                                 | **Expected Result**        | **Actual Result** |
| ---------------------------------------- | -------------------------- | ----------------- |
| Add "/interested" in deployed url        | interested list page opens | Work as expected  |
| User scrolls through the interested list | interested are displayed   | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory15.png" >

</details>

16. As a site owner/developer I can retrieve interested by id so that I can be able to make changes to it

| **Step**                             | **Expected Result**          | **Actual Result** |
| ------------------------------------ | ---------------------------- | ----------------- |
| Add "/interested/id" in deployed url | interested detail page loads | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory16.png" >

</details>

17. As a site owner/developer I can add interested functionality for events so that I can show interest for the event

| **Step**                            | **Expected Result**                          | **Actual Result** |
| ----------------------------------- | -------------------------------------------- | ----------------- |
| User log in                         | logged in status is shown in top right       | Work as expected  |
| Add "/interested" in deployed url   | interested lists page loads with create form | Work as expected  |
| User select event and click on post | interested is shown in interested list       | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory17-1.png" >
<img src="images/manualtesting/userstory17-2.png" >

</details>

18. As a site owner/developer I can delete interested functionality to event so that I can delete my interested instance if not interested anymore

| **Step**                                                       | **Expected Result**                             | **Actual Result** |
| -------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| User log in                                                    | logged in status is shown in top right          | Work as expected  |
| Add "/interested/id" in deployed url (id of user's interested) | interested detail page loads with delete button | Work as expected  |
| User clicks on delete button                                   | a modal confirming delete occurs                | Work as expected  |
| User clicks on delete button                                   | interested is deleted                           | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory18-1.png" >
<img src="images/manualtesting/userstory18-2.png" >
<img src="images/manualtesting/userstory18-3.png" >

</details>

19. As a site owner/developer I can view a list of join request for an event so that I can view how many request has been requested

| **Step**                           | **Expected Result**  | **Actual Result** |
| ---------------------------------- | -------------------- | ----------------- |
| Add "/join" in deployed url        | join list page opens | Work as expected  |
| User scrolls through the join list | join are displayed   | Work as expected  |

 <details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory19.png" >

</details>

20. As a site owner/developer I can retrieve join request so that I can make changes to it

| **Step**                       | **Expected Result**    | **Actual Result** |
| ------------------------------ | ---------------------- | ----------------- |
| Add "/join/id" in deployed url | join detail page loads | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory20.png" >

</details>

21. As a site owner/developer I can create a join request for an event so that I can join an event

| **Step**                            | **Expected Result**                    | **Actual Result** |
| ----------------------------------- | -------------------------------------- | ----------------- |
| User log in                         | logged in status is shown in top right | Work as expected  |
| Add "/join" in deployed url         | join list page loads with create form  | Work as expected  |
| User select event and click on post | join is shown in join list             | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory21-1.png">
<img src="images/manualtesting/userstory21-2.png" >

</details>

22. As a site owner/developer I can delete join request so that I can delete join request which is not approved anymore

| **Step**                                           | **Expected Result**                       | **Actual Result** |
| -------------------------------------------------- | ----------------------------------------- | ----------------- |
| User log in                                        | logged in status is shown in top right    | Work as expected  |
| Add "/join/id" in deployed url (id of user's join) | join detail page loads with delete button | Work as expected  |
| User clicks on delete button                       | a modal confirming delete occurs          | Work as expected  |
| User clicks on delete button                       | join is deleted                           | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory22-1.png" >
<img src="images/manualtesting/userstory22-2.png" >
<img src="images/manualtesting/userstory22-3.png" >

</details>

23. As a site owner/developer I can view a list of followers so that I can view who is following

| **Step**                                | **Expected Result**      | **Actual Result** |
| --------------------------------------- | ------------------------ | ----------------- |
| Add "/followers" in deployed url        | follower list page opens | Work as expected  |
| User scrolls through the followers list | follower are displayed   | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory23.png" >

</details>

24. As a site owner/ developer I can retrieve followers by id so that I can make changes to it

| **Step**                            | **Expected Result**        | **Actual Result** |
| ----------------------------------- | -------------------------- | ----------------- |
| Add "/followers/id" in deployed url | follower detail page loads | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory24.png" >

</details>

25. As a site owner/developer I can create follow so that I can follow another user

| **Step**                           | **Expected Result**                       | **Actual Result** |
| ---------------------------------- | ----------------------------------------- | ----------------- |
| User log in                        | logged in status is shown in top right    | Work as expected  |
| Add "/followers" in deployed url   | follower list page loads with create form | Work as expected  |
| User select user and click on post | follower is shown in followers list       | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory25-1.png" >
<img src="images/manualtesting/userstory25-2.png" >

</details>

26. As a site owner/developer I can delete a follow so that I can unfollow another user

| **Step**                                                     | **Expected Result**                           | **Actual Result** |
| ------------------------------------------------------------ | --------------------------------------------- | ----------------- |
| User log in                                                  | logged in status is shown in top right        | Work as expected  |
| Add "/followers/id" in deployed url (id of user's followers) | follower detail page loads with delete button | Work as expected  |
| User clicks on delete button                                 | a modal confirming delete occurs              | Work as expected  |
| User clicks on delete button                                 | follower is deleted                           | Work as expected  |

<details><summary>Screenshot</summary>
<img src="images/manualtesting/userstory26-1.png" >
<img src="images/manualtesting/userstory26-2.png" >
<img src="images/manualtesting/userstory26-3.png" >

</details>

### Automated Testing

- Automated testing was done using the Django Rest Framework APITestCase

<details><summary>Test Report</summary>
<img src="images/docs/automated-testing.png">
</details>

- Automated testing was also done using [Coverage python](https://coverage.readthedocs.io/)
- Coverage report for project was done and overall result was 97%

<details><summary>Test Report</summary>
<img src="images/docs/coverage-testing.png">
<img src="images/docs/coveragereport-1.png">
<img src="images/docs/coveragereport2.png">
<img src="images/docs/coveragereport3.png">
</details>

### Bugs

#### Code

- No error was found 

#### CI Python Linter

- No bug was found during Python Validation

#### Heroku Deployment

- No error found during deployment

### Unfixed Bugs

- No unfixed bugs from developer side

##### Back to [top](#table-of-contents)
