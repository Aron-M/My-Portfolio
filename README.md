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

- [PostgreSQL](https://www.postgresql.org/) Database storing all schemas and data.

- [ElephantSQL](https://www.elephantsql.com/) For hosting all PostgreSQL data on cloud.

- [Cloudinary](https://cloudinary.com/) Image storage.

- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) HTTP server interface.

- [Bootstrap](https://getbootstrap.com/) Bootstrap 5 was used in this project.



## Other Technologies Used:

- [Balsamiq](https://balsamiq.com/) Wireframes.

- [Draw.io](https:/draw.io/) For creating flowcharts.

- [Favicon](https://favicon.io/favicon-generator/) Favicon generator.

- [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.

- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) For administrator authentication.

- [Devicon](https://www.devicon.dev/) All icons used in 'Skills' section.

- [Flaticon](https://www.flaticon.com/) For icons used in website.


# Features

- Responsive on all devices.
- Interactive buttons.
- Updatable information displayed in each relevant section
- Google Map and Email Form for location and contact
- Downloadable CV.
- Custom front-end admin panel.
- Cloudinary picture storage.

## Design

This site was designed mainly by making use of bootstrap. I downloaded a specific template from [Bootswatch.com](https://bootswatch.com/) called 'Superhero.

Colors schema for this site is blue, white and dark grey.

# Data Structure

## Database 

- Personal Details:

    | Object | Field |
    |---|---|
    | ID | is automatically generated |
    | full_name | CharField |
    | nationality | CharField |
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

<img src="media/readme-images/homepage-workflow.png" style="max-width: 40rem;">

<br>

<img src="media/readme-images/portfolio-flowchart.png" style="max-width: 40rem;">


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

<br>

## CRUD FUNCTIONALITY (Create, Read, Update, Delete)
<br>

The pages below demonstrate how the user (if admin) can access the admin-dashboard on the fron-end make use of seperate pages included with forms to add, update/edit and/or delete information. This was done by making contructing various forms, views and models to handle full CRUD-capabilities on the front-end.

<br>

PLEASE NOTE: Below I will use one example for each section to demostrate CRUD capabilities. This is to prevent mass repetitiveness and to not flood the section with multiple images of each seperate page doing the exact same function. However, feel free to read the code files to explore more if you wish, specifically 'views.py' to see how each CRUD function is operating.

<br>

SUMMARY OF HOW EACH MODEL CAN BE AUGMENTED:
<br>
- Headings: Edit/Update
- Skills: Add, Edit/Update, Delete
- Projects: Add, Edit/Update, Delete
- Personal Details: Edit/Update

<br>

### CREATE

<br>

<details>
  <summary>Add (Skills)</summary>

 DESCRIPTION | ADD SKILL | NEW SKILL ADDED
  :---:|:---:|:--:
A form is included in the page displaying all inout fields of the 'skills model'. Upon completion of the form, the user can then click to add a new skill| ![](media/readme-images/add-skill-pc.png)| ![](media/readme-images/add-skill-new.png)

</details>

<br>

### READ
<br>

The 'Read' functionality is already performed and demostrated above by the user's ability to read/view all pages on multiple devices, and will therefore be omitted from this section. The READ capability is demonstrated in the 'Page Navigation' section above.

<br>

### EDIT/UPDATE

<br>

<details>
  <summary>Edit/Update (Headings)</summary>

 DESCRIPTION | EDIT HEADING | UPDATED
  :---:|:---:|:--:
  A form is included in the page displaying all input fields of the 'headings model'. Upon updating the chosen information within the form, the user can then click to edit a part of the section| ![](media/readme-images/edit-headings.png)| ![](media/readme-images/edit-heading-edited.png)

</details>

<br>

### DELETE 

<br>

<details>
  <summary>Delete (Project)</summary>

 DESCRIPTION | DELETE PROJECT | DELETED
  :---:|:---:|:--:
  A form is included in the page displaying all input fields of the 'projects model'. Upon completion of the form, the user can then click to add a new project| ![](media/readme-images/delete-project-pc.png)| ![](media/readme-images/delete-project-done.png)


</details>

<br>

# Deployment

## Programs needed:


### Cloudinary

1. Create an account [here](https://cloudinary.com/).
2. Log in.
<details><summary>Go to Dashboard for info</summary>
<img src="media/readme-images/cloudinary-2.png" alt="cloudinary"/>

</details>
<br>


### Heroku

3. Create an account [here](https://www.heroku.com/)

### GitHub

4. Login to your [GitHub](https://github.com/)


### ElephantSQL

5. Create an account [here](https://www.elephantsql.com/).
6. Log in and set up instance
<details><summary>Start creating an instance</summary>
<img src="media/readme-images/elephant-1.png" alt="create database"/>
</details>
<br>
<details><summary>Select Plan</summary>
<img src="media/readme-images/elephant-2.png" alt="create database"/>
</details>
<br>
<details><summary>Choose Region</summary>
<img src="media/readme-images/elephant-3.png" alt="create database"/>
</details>
<br>
<details><summary>Crete Instance</summary>
<img src="media/readme-images/elephant-4.png" alt="create database"/>
</details>
<br>
<details><summary>Select new Instance</summary>
<img src="media/readme-images/elephant-5.png" alt="create database"/>
</details>
<br>
<details><summary>Copy instance URL</summary>
<img src="media/readme-images/elephant-6.png" alt="create database"/>
</details>
<br>


## Local Development

7. Go to Github repo [here](https://github.com/Aron-M/Project-4-Portfolio) and click the **< CODE >** button, then click **COPY**.
<details><summary>Picture</summary>
<img src="docs/deployment/1.png" alt="deployment github"/>
</details>
<br>

2. Go to your github repositories and create your own new repo. You can call it whatever you like. Press **Create Repository** and it will lead you to a new page. Press **Gitpod**  and it should open a new workspace for you. 
 ***If you are using VSCODE, then just open a new workspace***
    <details><summary>Steps to deploy new workspace</summary>
    <img src="media/readme-images/deploy-repo-1.png" alt="github"/>
    <img src="media/readme-images/deploy-repo-2.png" alt="github"/>
    <img src="media/readme-images/deploy-repo-3.png" alt="github"/>
    </details>
    <br>

3. When eitherGitpod or VSCODE is open, type in 'git bash' following "**git clone https://github.com/Aron-M/Project-4-Portfolio.git**" without using any quotation marks, and press enter. It will clone my repository.
    <details><summary>Picture</summary>
    <img src="media/readme-images/deploy-git-clone-1.png" alt="github"/>
    <img src="media/readme-images/deploy-git-clone-2.png" alt="github"/>
    </details>
    <br>

4. Very good! Now you should have your own local repository with all the neccessary code templates to run the game. In the terminal you can type "python3 run.py" to test the game within your local terminal. Next up we have to deploy it on Heroku.


5. Download all libraries and frameworks to use in this project.
```
pip3 install -r requirements.txt
```

6. Create **env.py** in main folder and add cloudinary api key, elephantSQL and your own secret key. See image below. (DO NOT name the **env.py** file anything differen, or your password will be leaked to your repository.)
```
os.environ['DATABASE_URL'] = " url from elephantsql"
os.environ['SECRET_KEY'] = "secret_key"
os.environ['CLOUDINARY_URL'] = "api key from, remove 'CLOUDINARY_URL=' FROM BEGINING"
```
<details><summary>env.py</summary>
<img src="media/readme-images/env.png" alt="deployment github"/>
</details>
<br>

7. Now type in this command into terminal, this will migrate all models to database.
```
python3 manage.py migrate
```
<details><summary>Migrating files</summary>
<img src="media/readme-images/env.png" alt="deployment github"/>
</details>
<br>

8. Now we have to create 'superuser' for django admin panel from within the terminal by typing command:

```
python3 manage.py createsuperuser
```
<details><summary>Create Superuser in CLI</summary>
<img src="media/readme-images/env.png" alt="deployment github"/>
</details>
<br>

9. Go to pp4_portfolio folder and open **settings.py** and add this code to **ALLOWED_HOST**
```
.herokuapp.com, localhost
```


10. Now we push our code to GitHub by typing:
```
git add .
git commit -m "your own commit"
git push
```
11. Go to [Heroku](https://id.heroku.com/login) and login to your account.

12. At the top right corner click the **New** button and then **Create new app**, next you will
- Name your app whatever you like, then 
- Pick server depending which region you are in: For me it was Europe 
- Then click **Create app**
    <details><summary>Picture</summary>
    <img src="media/readme-images/heroku-1.png" alt="heroku"/>
    <img src="media/readme-images/heroku-2.png" alt="heroku"/>
    </details>
    <br>

13. Go to **Settings** and press **Reveal Config Vars**. In the **KEY** block type in **PORT** and for **VALUE** type in **8000**.
    <details><summary>Picture</summary>
    <img src="media/readme-images/heroku-3.png" alt="heroku"/>
    </details>
    <br>

Additonally, aslo add the following config variables
```
DATABASE_URL - url as is in env.py
SECRET_KEY - your secret key
CLOUDINARY_URL - API key as is in env.py
```

14. Now scroll down until you see **Buildpacks**, press **Add buildpack** and select **python** and **save changes**. Afterwards, again **Add buildpack** but this time pick **nodejs** and **save change**. heroku/python should be above nodejs. If its not, then drag it with the hamburger menu on the left of the image or remove with x and add again in the correct order.
    <details><summary>Picture</summary>
    <img src="media/readme-images/heroku-4.png" alt="heroku"/>
    </details>
    <br>

15. Go back to top of the page and click **Deploy**, and click on **GitHub** and connect to it. Next below type in name of your repository and click search, it should automaticaly find the repo. Then click **Connect**
    <details><summary>Picture</summary>
    <img src="media/readme-images/heroku-5.png" alt="heroku"/>
    <img src="media/readme-images/heroku-6.png" alt="heroku"/>
    </details>
    <br>

16. Now in address bar type in after our website url **/accounts/login** and input your superuser password. If everything works you should see frontend admin panel.
```
https://........herokuapp.com/accounts/login/
```
<details><summary>Django Admin Panel</summary>
<img src="media/readme-images/django-admin.png" alt="deployment heroku"/>
</details>
<br>

16. Project is now ready to be used.

# Credits:

