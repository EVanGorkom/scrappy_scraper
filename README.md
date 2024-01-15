# Scrappy Scraper

## Introduction
The purpose of this application is to be a able to scrape data from a website. In version 1 the goal is to consume a single website's data and store it for later use. 

---
## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Author](#author)
<!-- - [RESTful Endpoints](#restful-endpoints)
  - [Markets](#markets)
  - [Customers](#customers)
  - [Vendors](#vendors)
  - [Items](#items)
  - [Preorders](#preorders) -->
---


## Tech Stack
<a href="https://www.python.org/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" height="50" /></a>
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" height="50" /></a>

- **Python:** The primary programming language offering simplicity and versatility.
- **Django:** Used for building the framework of the application so it can later be deployed.

## Key Features 
-

---
## Getting Started
1. **Clone the Repository:** Get started with 'Scrappy Scraper' by cloning the repository to your local machine.
2. **Install Requirements:** Navigate into the cloned repository and install necessary dependencies
3. **Start the Server:** Start the Django server.
Note: Please ensure you have Python and pip installed on your machine before running these commands.

<!-- ## RESTful Endpoints

Base url to reach the endpoints listed below:
```
https://quiet-depths-54407-77a00505f51e.herokuapp.com/
``` -->

<!-- ### Markets
```
Get /markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
]
```

</details>
<br>

```
Post /markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 1,
    "market_name": "Denver Saturday Market",
    "location": "Denver, CO",
    "details": "All the vendors!!",
    "start_date": "2023-12-06",
    "end_date": "2023-12-06",
    "date_created": "2023-12-06T18:02:28.458557Z",
    "updated_at": "2023-12-06T18:02:28.458571Z"
}
```

</details> -->


### Author

<table>
  <tr>
    <th>Ethan Van Gorkom</th>
  </tr>

<tr>
  <td><img src="https://avatars.githubusercontent.com/u/132889569?v=4" width="135" height="135"></td>
</tr>


  <tr>
    <td>
      <a href="https://github.com/EVanGorkom" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/evangorkom/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
  </tr>
</table>