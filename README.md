# Aron's Personal Potfolio Webpage

Welcome to to Aron's Personal Portfolio Webpage! 


## Table of content:

- [Motivation](#motivation)

- [User Experience](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Website Goals](#website-goals)
    - [Requirements](#requirements)
    - [Expectations](#expectations)
    - [Design](#design)
    - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Tablet](#tablet)
        - [Mobile](#mobile)
- [Website Structure](#website-structure)
- [Technology, Frameworks and Programs used](#technology-frameworks-and-programs-used)
    - [Languages](#languages)
    - [Frameworks and programs used](#frameworks-and-programs-used)
- [Features](#features)
    - [Navigation bar](#navigation-bar)
- [Testing](#testing)
- [Testing user stories](#testing-user-stories)
- [Deployment](#deployment)
- [Credits](#credits)

# Motivation

The motivation behind creating this webpage is to introduce and showcase myself as a web developer to prospective employers and anyone the Web Development sector interested in learning more about my past and current programming knowledge & achievements.

# User Experience (UX)

## User Stories
- User Stories:
    - As a user, I want to be able to access a user-friendly main page showcasing an overview of the developer.
    - As a user, I want to be able to navigate to the About section.
    - As a user, I want to be able to navigate to the Skills section.
    - As a user, I want to be able to navigate to the Projects section.
    - As a user, I want to access the developer's past projects via provided links.
    - As a user, I want to be able to have access to relevant Social Media and GitHub account.
    - As a user, I want to be able to download the developer's CV.
    - As a user, I want to be able to contact the developer via a form.

- Admin Stories:
    - As an admin, I want to be able to access an 'admin-dashboard' panel/page.
    - As an admin, I want to be able to select various sections of the webpage to create, update and/or delete information
    - As an admin, I want to be able to securely log in to the admin dashboard pages.
    - As an admin, I want to be sure that no-ne of the general public will be allowed to access any of the admin pages.
    - As an admin, I want all the changes I make to display on the webpage accordingly for the public to view.

## Website Goals

This webpage aims to serve as an informational web application to showcase personal information, Software Development Skills & Languages as well as a list of prior projects done to the user (such as prospective employers) interested in finding out about me and my coding history. It will also give the user the ability to connect with the site owner (myself) via a form, get access to relevant Social Media and GitHub accounts as well as the ability to download a .PDF CV on request. Finally, the site will aim to provide the administrative front-en access to create, update and/or delete data within certain fields for the site administrator(s) securely access.


## Requirements

- Landing Page.
- About Section.
- Skills Section
- Projects showcase Sectio.
- Contact Section
- Download CV.
- Links to Social Media and GitHub
- Login Access for Admin in where to change/modify/update/delete data in certain fields.

## Expectations

- I expect my website to be easily accessible.
- I expect my website to attract future employers.
- I expect to showcase my projects and skills.
- I expect my website to be editable on the front-end via logging in to an admin account.

# Technology, Frameworks and Libraries used.

## Languages used:

- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Databases and Libraries used:

- [Django](https://www.djangoproject.com/) Python-based web framework that follows the model–template–views architectural pattern.

- [Heroku](https://www.heroku.com) Deployment of website.

- [ElephantSQL](https://www.elephantsql.com/) Database storing all schemas and data.

- [Cloudinary](https://cloudinary.com/) Image storage.

- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) HTTP server interface.

- [Bootstrap](https://getbootstrap.com/) Bootstrap 5 was used in this project.



## Other Technologies Used:

- [Balsamiq](https://balsamiq.com/) Wireframes.

- [Favicon](https://favicon.io/favicon-generator/) Favicon generator.

- [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.

- [Devicon](https://www.devicon.dev/) All icons used in 'Skills' section.


# Features

- Responsive on all devices.
- Interactive buttons.
- Updatable information displayed in each relevant section
- Google Map and Email Form for location and contact
- Downloadable CV
- Custom front-end admin panel.
- Cloudinary picture storage.


# Data Structure

## Database 

- Personal Details:

    | Object | Field |
    |---|---|
    | ID | is automatically generated |
    | full_name | CharField |
    | nationality | CharBigInteger |
    | residency | Charfield |
    | flag_nationality | ImageField |
    | flag_residency | ImageField |
    | languages | Charfield |
    | studying | CharField |
    | study_icon | ImageField |

- Headings:

    | Object | Field |
    |---|---|
    |  ID | is automatically generated |
    | big_heading | CharField |
    | sub_heading | CharField |
    | profile_image | ImageField |
    | par_1 | CharField |
    | par_2 | CharField |

- Project:

    | Object | Field |
    |---|---|
    |  ID | is automatically generated |
    | name | CharField |
    | desription | CharField |
    | image | ImageField |
    | github_url | URLField |

- SkillsCategory:
    | Object | Field |
    |---|---|
    | name | CharField|

- Skills:

    | Object | Field |
    |---|---|
    |  ID | is automatically generated |
    | name | CharField |
    | icon | URLField |
    | progress | ImageField |
    | category | ForeignKey (SkillsCategory) |


# Workflow

## Wireframes

- Home page Top.
    <details><summary>Picture</summary>
    <img src="media/readme-images/about-me-wireframe.png" alt="home page"/>
    </details>
    <br>

- About Me Section.
    <details><summary>Picture</summary>
    <img src="media/readme-images/about-me-wireframe.png" alt="about me page"/>
    </details>
    <br>

- Projects Section.
    <details><summary>Picture</summary>
    <img src="media/readme-images/about-me-wireframe.png" alt="projects page"/>
    </details>
    <br>


- Admin-Dashboard page.
    <details><summary>Picture</summary>
    <img src="docs/front-panel-details.png" alt="front panel details section"/>
    </details>
    <br>
    <details><summary>Picture</summary>
    <img src="docs/front-panel-skills.png" alt="front panel skills section"/>
    </details>
    <br>
    <details><summary>Picture</summary>
    <img src="docs/front-panel-projects.png" alt="front panel projects section"/>
    </details>
    <br>

## Home Page Workflow

<img src="media/readme-images/homepage-workflow.png">

<br>

<img src="media/readme-images/portfolio-flowchart.png">


<br>

# Navigation

<br>

## HOME PAGE

<details>
  <summary>Headings</summary>

  HEADINGS | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'Headings' Section which will be the first thing the user sees when opening the page | ![](media/readme-images/headings-home-page.png) | ![](media/readme-images/headings-home-page-tablet.png)| ![](media/readme-images/headings-home-page-phone.png)

</details>

<br>

<details>

  <summary>Skills</summary>

  SKILLS | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'Skill' Section which displays current skills and an info-modal | ![](media/readme-images/skills-section-pc.png) | ![](media/readme-images/skills-section-tablet.png)| ![](media/readme-images/skills-section-phone.png)

</details>

<br>

<details>
  <summary>Projects</summary>

  PROJECTS | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'Project' section displaying all my current projects | ![](media/readme-images/projects-section-pc.png) | ![](media/readme-images/projects-section-tablet.png)| ![](media/readme-images/projects-section-phone.png)

</details>

<br>

<details>
  <summary>Contact</summary>

CONTACT | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'Contact' section where user can find and contact me | ![](media/readme-images/contact-section-pc.png) | ![](media/readme-images/contact-section-tablet.png)| ![](media/readme-images/contact-section-phone.png)

</details>

<br>

## ABOUT ME PAGE
<br>

<details>
  <summary>About Me</summary>

ABOUT ME | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'About Me' page where user can get more personal info | ![](media/readme-images/about-section-pc.png) | ![](media/readme-images/about-section-tablet.png)| ![](media/readme-images/about-section-phone.png)

</details>

<br>

## ADMIN DASHBOARD
<br>

<details>
  <summary>Admin Dashboard</summary>

 PC | TABLET | PHONE
  :---:|:---:|:--:
 ![](media/readme-images/admin-dashboard-pc.png) | ![](media/readme-images/admin-dashboard-tablet.png)| ![](media/readme-images/admin-dashboard-phone.png)

</details>


## CRUD PAGES
<br>

<details>
  <summary>Edit </summary>

 PC | TABLET | PHONE
  :---:|:---:|:--:
 ![](media/readme-images/admin-dashboard-pc.png) | ![](media/readme-images/admin-dashboard-tablet.png)| ![](media/readme-images/admin-dashboard-phone.png)

</details>

