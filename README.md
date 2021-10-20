# django-dennis-devsearch

This is my exercise based on tutorials by Dennis on Udemy

<a href="https://github.com/gurnitha/django-dennis-devsearch" target="_blank">Github repository</a>


### 1. INITIAL SETUP
### -----------------------------------------------------


#### 1.1 Create Github repository

        modified:   .gitignore
        modified:   README.md


#### 1.2 Create virtualenv

       modified:   README.md


#### 1.3 Install django v3.2

       modified:   README.md


#### 1.4 Upgrade pip

       modified:   README.md


### 2. DJANGO PROJECT & APP
### -----------------------------------------------------


#### 2.1 Create django project 'devsearch'

        modified:   README.md
        new file:   devsearch/__init__.py
        new file:   devsearch/asgi.py
        new file:   devsearch/settings.py
        new file:   devsearch/urls.py
        new file:   devsearch/wsgi.py
        new file:   manage.py


#### 2.1 Create djangp app 'projects'

        new file:   projects/__init__.py
        new file:   projects/admin.py
        new file:   projects/apps.py
        new file:   projects/migrations/__init__.py
        new file:   projects/models.py
        new file:   projects/tests.py
        new file:   projects/views.py


#### 2.3 Register the app 'projects' to the project 'devsearch'

        modified:   README.md
        modified:   devsearch/settings.py


### 3. DATABASE
### -----------------------------------------------------


#### 3.1 Create MySQL database

        modified:   README.md


#### 3.2 Install mysqliclient

        modified:   README.md


#### 3.3 Connect the project with the database

        modified:   README.md
        modified:   devsearch/settings.py


#### 3.4 Run migrate to create auth tables

        modified:   README.md
        modified:   devsearch/settings.py

        NOTE: Fixing the database setting


#### 3.5 Craete superuser and run the server

        modified:   README.md


#### 3.6 Admin panel and login


        modified:   README.md


### 4. MODELS
### -----------------------------------------------------


#### 4.1 Create Project model and run migration

        modified:   README.md
        new file:   projects/migrations/0001_initial.py
        modified:   projects/models.py

        (venv3932) λ python manage.py sqlmigrate projects 0001
        --
        -- Create model Project
        --
        CREATE TABLE `projects_project` (
                `title` varchar(200) NOT NULL, 
                `description` longtext NULL, 
                `demo_link` varchar(2000) NULL, 
                `source_link` varchar(2000) NULL, 
                `created` datetime(6) NOT NULL, 
                `id` char(32) NOT NULL PRIMARY KEY
        );


#### 4.2 Register Project model to admin.py

        modified:   README.md
        modified:   projects/admin.py


#### 4.3 Modified Project model

        modified:   README.md
        modified:   projects/models.py


#### 4.4 Create Review model

        modified:   README.md
        modified:   projects/models.py


#### 4.5 Register Review model to admin


        modified:   README.md
        modified:   projects/admin.py


#### 4.6 Create Tag model

        modified:   README.md
        modified:   projects/models.py


#### 4.5 Register Tag model to admin

        modified:   README.md
        modified:   projects/admin.py


#### 4.7 Added ManyToMany relationship Project and Tag models

        modified:   README.md
        modified:   projects/models.py


#### 4.8 Added OneToMany relationship Project and Review models

        modified:   README.md
        modified:   projects/models.py


#### 4.9 Run migrations

        modified:   README.md
        new file:   projects/migrations/0002_auto_20211017_1926.py


#### 4.10 Modified model, new file and modified README.md

        modified:   README.md
        new file:   django_orm.py
        new file:   projects/migrations/0003_remove_project_featured_image.py
        modified:   projects/models.py


### 5. TEMPLTES
### -----------------------------------------------------


#### 5.1 Using VTUrls to adding basic projects and single-project peges

        modified:   README.md
        modified:   devsearch/settings.py
        modified:   devsearch/urls.py
        new file:   projects/templates/projects/projects.html
        new file:   projects/templates/projects/single-project.html
        new file:   projects/urls.py
        modified:   projects/views.py
        new file:   templates/main.html
        new file:   templates/navbar.html


#### 5.2 Template inheritance

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/templates/projects/single-project.html
        modified:   templates/main.html
        modified:   templates/navbar.html 



### 6. RENDERING DUMY DATA TO TEMPLTES
### -----------------------------------------------------


#### 6.1 Rendering data to templates

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py


#### 6.2 Using context dic to rendering data to templates

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py


#### 6.6 Using logic to passing data to template

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py
        modified:   templates/main.html


#### 6.4 Using for loop rendering static data project list to template

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py


#### 6.5 Rendering single-project

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/templates/projects/single-project.html
        modified:   projects/urls.py
        modified:   projects/views.py
        modified:   templates/navbar.html

#### 6.6 House keeping - Modified README.md file

        modified:   README.md



### 7. RENDERING DATA FROM DATABASE TO TEMPLTES
### -----------------------------------------------------


#### 7.1 Rendering project list

        modified:   README.md
        modified:   projects/views.py


#### 7.2 Rendering single project

        modified:   README.md
        modified:   projects/views.py


#### 7.3 Rendering tags single project

        modified:   README.md
        modified:   projects/templates/projects/single-project.html
        modified:   projects/views.py


#### 7.4 Display projects in a table

        modified:   README.md
        modified:   projects/templates/projects/projects.html



### 8. CREATE, READ, UPDATE AND DELETE (CRUD)
### -----------------------------------------------------


#### 8.1 Create project_form page Part 1 - Basic VTUrl

        modified:   README.md
        new file:   projects/templates/projects/project_form.html
        modified:   projects/urls.py
        modified:   projects/views.py
        modified:   templates/navbar.html


#### 8.2 Create project_form page Part 2 - Django form

        modified:   README.md
        new file:   projects/forms.py
        modified:   projects/views.py


#### 8.3 Create project_form page Part 3 - Rendering Django form to project_form page

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


#### 8.4 Create project_form page Part 4 - Rendering Django form with title, label etc

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


#### 8.5 Create project_form page Part 4 - Looping Django form
        
        modified:   README.md
        modified:   projects/templates/projects/project_form.html


#### 8.6 CRUD - (C) Create project

        modified:   README.md
        modified:   projects/forms.py
        modified:   projects/templates/projects/project_form.html
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py


#### 8.7 CRUD - (U) Update project

        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py


#### 8.8 CRUD - (D) Delete project

        modified:   README.md
        new file:   projects/templates/projects/delete_template.html
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py


#### 8.9 House keeping - modified README.md file

        modified:   README.md



### 9. STATIC AND MEDIA FIELS
### -----------------------------------------------------


#### 9.1 Adding static and media files and their path

        modified:   devsearch/settings.py
        modified:   devsearch/urls.py
        new file:   static/images/codesniper.png
        ...
        new file:   static/images/default.jpg
        new file:   static/images/django-react-course.jpg
        new file:   static/images/icon.svg



### 10. DEBUG AND ALLOWED_HOSTS
### -----------------------------------------------------


#### 10.1 Setup DEBUG an ALLOWED_HOSTS

        modified:   README.md
        modified:   devsearch/settings.py
 

#### 10.2 Setup django whitenoice, add logo and modifien url

        modified:   README.md
        modified:   devsearch/settings.py
        modified:   projects/urls.py
        modified:   templates/main.html



### 11. TEMPLATE THEMES
### -----------------------------------------------------


#### 11.1 Adding template theme for the projects page

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   static/uikit/app.js
        modified:   static/uikit/styles/modules/_form.css
        new file:   templates/index.html
        modified:   templates/main.html


#### 11.2 Re-rendering projects from db to projects page

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        new file:   static/images/DevSearch Projects.jpg
        new file:   static/images/Devsearch Home.jpg
        new file:   static/images/Devsearch Inbox.jpg
        new file:   static/images/Devsearch Profile.jpg
        new file:   static/images/favicon.ico
        modified:   static/images/logo.svg
        new file:   static/images/project-a.png
        new file:   static/images/project-b.png
        new file:   static/images/project-c.png
        modified:   templates/main.html


#### 11.3 Adding template theme for the single project page

        modified:   README.md
        new file:   projects/migrations/0004_project_featured_image.py
        modified:   projects/models.py
        modified:   projects/templates/projects/projects.html
        modified:   projects/templates/projects/single-project.html
        new file:   static/images/favicon_EIIUZwF.ico
        new file:   static/images/project-a_OXtBCRw.png
        new file:   static/images/project-c_n7zvYI9.png


#### 11.4 PROJECT_FORM Part 1: Adding template theme 

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


#### 11.5 PROJECT_FORM Part 2: Loop the form field

        Steps:

        1. Keep 1 form field and the submit button and remove the rest
        2. Use for loop to loop the ONE of the form field
        3. Display form label: {{field.label}} 
        4. Replace all line of the input tag with: {{field}} 
        5. Check the result

        modified:   README.md
        modified:   projects/forms.py
        modified:   projects/templates/projects/project_form.html


#### 11.6 PROJECT_FORM Part 6: Change tags field from multiselect to radio button

        modified:   README.md
        modified:   projects/forms.py


#### 11.7 PROJECT_FORM Part 7: Adding class style to input field

        BEFORE:

        <!-- Input:Text -->
                    <div class="form__field">
                        <label 
                            for="formInput#text">Title
                        </label>
                        <input type="text" name="title" maxlength="200" 
                        required id="id_title">
                    </div>

        AFTER:

        <!-- Input:Text -->
                    <div class="form__field">
                        <label 
                            for="formInput#text">Title
                        </label>
                        <input type="text" name="title" maxlength="200" 
                        class="input" <<<-- here added
                        placeholder="Add title"  <<<-- here added
                        required id="id_title">
                    </div>

        modified:   README.md
        modified:   projects/forms.py

        
#### 11.8 PROJECT_FORM Part 8: Using for loop to replace techniques in 11.7


       BEFORE:

        <!-- Input:Text -->
                    <div class="form__field">
                        <label 
                            for="formInput#text">Title
                        </label>
                        <input type="text" name="title" maxlength="200" 
                        class="input" <<<-- here added
                        placeholder="Add title"  <<<-- here added
                        required id="id_title">
                    </div>

        AFTER:

        <!-- Input:Text -->
                    <div class="form__field">
                        <label 
                            for="formInput#text">Title
                        </label>
                        <input type="text" name="title" maxlength="200" 
                        class="input" <<<-- here added
                        required id="id_title">
                    </div>

        modified:   README.md
        modified:   projects/forms.py



### 12. USERS APP
### -----------------------------------------------------


#### 12.1 Create 'users' app

        modified:   README.md
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py


#### 12.2 Register the users app to settings.py

        modified:   README.md
        modified:   devsearch/settings.py
        modified:   users/apps.py



### 13. USERS PROFILES PAGE
### -----------------------------------------------------


#### 13.1 Create profiles page

        Steps

        1. Create templates folder: users/templates
        2. Create users folder    : users/templates/users
        3. Create profile page    : users/templates/users/profile.html

        modified:   README.md
        new file:   users/templates/users/profile.html


#### 13.2 Create profiles view

        Steps

        1. Open users/views.py file
        2. Define profiles views and render the profiles page

        modified:   README.md
        modified:   users/views.py      


#### 13.3 Create urls

        Steps

        1. Inside users app, create a new file: urls.py
        2. Define the urls
        3. Register the urls to the devsearch/urls.py
        4. Testing to see the resutl

        modified:   README.md
        modified:   devsearch/urls.py
        modified:   users/apps.py
        new file:   users/urls.py


#### 13.4 Extending the main layout to the profiles page

        Steps

        1. Extends the main layout
        2. Use the block tags
        3. Testing to see the result

        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 13.5 House keeping - Modified README.md file

        modified:   README.md
        deleted:    static/images/profiles/2021-06-27_16_29_50-Window.png
        deleted:    static/images/profiles/22437186.jpg
        deleted:    static/images/profiles/b3wSZKj4_400x400.jpg
        deleted:    static/images/profiles/dennis.jpg
        deleted:    static/images/profiles/dennis_Hepsy19.jpg
        deleted:    static/images/profiles/dennis_ee5zj3F.jpg
        deleted:    static/images/profiles/user-default.png
        deleted:    static/images/profiles/user-default_YS9Vr6e.png



### 14. USERS PROFILES MODEL
### -----------------------------------------------------


#### 14.1 Create Profile model

        Steps

        1. Go to users
        2. Open models.py
        3. Define the Profile model and its fields
        4. Go to static/images 
        5. Create a new folder: profiles
        6. Add a default image into profiles folder

        modified:   README.md
        new file:   static/images/profiles/user-default.png
        modified:   users/models.py


#### 14.2 Run migrations to create table

        Steps

        1. Run makemigrations 
        2. Run migrate
        3. The result

        modified:   README.md
        new file:   users/migrations/0001_initial.py


#### 14.3 Register the Profile model to admin.py to see it in admin panel

        Steps

        1. Open admin.py from users
        2. Import Profile model
        3. Register it to admin
        4. See the result

        modified:   README.md
        modified:   users/admin.py


#### 14.4 Adding OneToMany relationship between Profile and Project

        Steps

        1. Import Profile model
        2. Add a new field (owner) for its the relationship

        modified:   README.md
        new file:   projects/migrations/0005_project_owner.py
        modified:   projects/models.py
        new file:   static/images/profiles/AI-BABY.PNG
        new file:   static/images/profiles/bisma.PNG
        new file:   static/images/profiles/ing.PNG
        new file:   static/images/profiles/ing_cXEFvj1.PNG
        new file:   static/images/profiles/logo-jet.JPG
        new file:   users/migrations/0002_profile_username.py
        modified:   users/models.py


#### 14.5 Assign each project to user

        Steps

        1. Go admin panel
        2. Open projects > click on a project
        3. Add/select user

        modified:   README.md


#### 14.5 Display username to projects page

        Steps

        1. Open projects.html
        2. Load the owner of the project by its username

        modified:   README.md
        modified:   projects/templates/projects/projects.html



### 15. USERS PROFILES PAGE
### -----------------------------------------------------


#### 15.1 Add theme to the profiles.html file

        Steps

        1. Add theme to the page

        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 15.2 Preparing the page to display users from db


        Steps

        1. Remove some cards in the page

        modified:   README.md
        modified:   users/templates/users/profiles.html 



#### 15.3 Create Skill model


        Steps

        1. Analise the content
           -owner 
           -neme
           -description
           -created 
        2. Create the Skill model
        3. Add OneToMany rel with Profile 
        4. Run migration
        5. Register to admin 

        modified:   README.md
        modified:   users/admin.py
        new file:   users/migrations/0003_skill.py
        modified:   users/models.py
        modified:   users/templates/users/profiles.html



#### 15.4 Add location field to Profile model


        Steps

        1. Open the file: users/models.py
        2. Add the field
        3. Run migration

        modified:   README.md
        modified:   users/models.py


#### 15.5 Admin - Add skill to users, add location to profiles

        modified:   README.md


#### 15.6 Retrieve and display profile

        modified:   README.md
        modified:   users/templates/users/profiles.html
        modified:   users/views.py


#### 15.7 Retrieve and display skill

        modified:   README.md
        modified:   users/templates/users/profiles.html
        modified:   users/views.py



### 16. USER PROFILE PAGE
### -----------------------------------------------------

#### 16.1 Create user-profile page VTUrl

        modified:   README.md
        modified:   devsearch/urls.py
        modified:   projects/urls.py
        modified:   users/templates/users/profiles.html
        new file:   users/templates/users/user-profile.html
        modified:   users/urls.py
        modified:   users/views.py

#### 16.2 Load user information to user-profile page Part 1 - Aside

        modified:   README.md
        new file:   users/templates/users/user-profile.html


#### 16.3 Load user information to user-profile page Part 2 - social media

        new file:   users/migrations/0005_profile_social_stackoverflow.py
        modified:   users/models.py
        modified:   users/templates/users/user-profile.html


#### 16.4 Load user information to user-profile page Part 3 - about

        modified:   users/templates/users/user-profile.html


#### 16.5 Load user information to user-profile page Part 4 - skill with descripion

        modified:   README.md
        modified:   users/templates/users/user-profile.html
        modified:   users/views.py


#### 16.6 Load user information to user-profile page Part 5 - skill without descripion

        modified:   README.md
        modified:   users/templates/users/user-profile.html
        modified:   users/views.py


#### 16.7 Load user information to user-profile page Part 6 - limit the skill show in the profiles page

        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 16.8 Load user information to user-profile page Part 7 - showing all projects AS CHILD of profile

        modified:   README.md
        modified:   users/templates/users/user-profile.html


#### 16.7 Load user information to user-profile page Part 7 - showing all tags belong to the project own by the a user

        modified:   README.md
        modified:   users/templates/users/user-profile.html
        modified:   users/views.py
