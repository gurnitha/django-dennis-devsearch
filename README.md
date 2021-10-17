# django-dennis-devsearch
This is my exercise based on tutorials by Dennis on Udemy


###-----------------
### 1. INITIAL SETUP
###-----------------


#### 1.1 Create Github repository

        modified:   .gitignore
        modified:   README.md


#### 1.2 Create virtualenv

       modified:   README.md


#### 1.3 Install django v3.2

       modified:   README.md


#### 1.4 Upgrade pip

       modified:   README.md


###------------------------
### 2. DJANGO PROJECT & APP
###------------------------


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


###------------
### 3. DATABASE
###------------


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


###----------
### 4. MODELS
###----------


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
