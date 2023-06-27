# TESTING

## Table of Contents

1. [Manual Testing](#manual-testing-of-user-stories)
2. [Automated Testing]()
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

## Bugs

### CI Python Linter

- No bug was found during Python Validation

### Heroku Deployment

- No error found during deployment

## Unfixed Bugs

- No unfixed bugs from developer side
