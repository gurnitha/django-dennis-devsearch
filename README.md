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
