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


#### 16.8 Load user information to user-profile page Part 8 - showing all tags belong to the project own by the a user

        modified:   README.md
        modified:   users/templates/users/user-profile.html
        modified:   users/views.py


#### 16.9 Load user information to user-profile page Part 9 - linking owner name with the user-profile page

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   templates/main.html


#### 16.10 Load user information to user-profile page Part 10 - linking owner name with the user-profile page to re-load the page

        modified:   README.md
        modified:   users/templates/users/user-profile.html



### 17. DJANGO SIGNALS - EXERCISES
### -----------------------------------------------------


#### 17.1 Create signals (post_save) - modified  a profile in the db and save

        modified:   README.md
        modified:   users/models.py


#### 17.2 Create signals (post_save) - print out the instance Sender and Reciever

        modified:   README.md
        modified:   users/models.py


#### 17.3 Create signals (post_save) - create a new profile and print out the instance Sender and Reciever

        modified:   README.md
        modified:   users/models.py


#### 17.4 Create signals (post_delete) - DELETE a profile and print out the instance Sender and Reciever

        modified:   README.md
        modified:   users/models.py


#### 17.5 Create signals decorator (post_save) - modified  a profile in the db and save


        modified:   README.md
        modified:   users/models.py


#### 17.6 House keeping - modified README.md

        modified:   README.md



### 18. DJANGO SIGNALS - REAL PRACTICES
### -----------------------------------------------------


#### 18.1 Using django signals to create a profile when a new user is created

        modified:   README.md
        modified:   users/models.py


#### 18.2 Using django signals to delete a profile and his from users as well

        NOTE:

        Point 18.1 do like these:

        1. Delete a user, the user's profile also deleted
        2. Bu delete a profile, the user did not detele it


        modified:   README.md
        modified:   users/models.py


#### 18.3 Putting signals in seperate file

        modified:   README.md
        modified:   users/models.py
        new file:   users/signals.py


#### 18.4 Testing signals

        modified:   README.md
        modified:   users/signals.py

        NOTE: Nothing was triggered!


#### 18.5 Use ready() method to trigger signals

        Steps:

        1. Open users/apps.py
        2. def ready() method
        3. import signals
        4. Testing:
           - open a user
           - update it and save it
           - see the result in the terminal

        modified:   README.md
        modified:   users/apps.py



### 19. AUTHENTICATION
### -----------------------------------------------------


#### 19.1 Login Part 1 - Create login_register page VTUrls

        Steps:

        1. Create users/templates/users/login_register.html file
        2. Extends the main page
        3. Define login views method
        4. In menu add link
        
        modified:   README.md
        modified:   templates/main.html
        new file:   users/templates/users/login_register.html
        modified:   users/urls.py
        modified:   users/views.py


#### 19.2 Login Part 2 - Adding basic form

        Steps:

        1. Add basic html form
        2. See the resutl

        modified:   README.md
        modified:   users/templates/users/login_register.html


#### 19.3 Login Part 3 - Adding the basics logic

        Steps:

        1. Define the logic
        2. Test it out
        3. See the resutl

        modified:   README.md
        modified:   users/views.py


#### 19.4 Login Part 4 - Adding the authentication logic

        Steps:

        1. See 6 steps to authenticate user to login and test it out

        modified:   README.md
        modified:   users/views.py


#### 19.5 Login Part 5 - Showing logout menu to logged in user

        Steps:

        1. Add conditional to the menu
        2. See the result

        modified:   README.md
        modified:   templates/main.html


#### 19.6 Logout - Add logout functionality

        Steps:

        1. Import logout method
        2. Create logoutUser view method
        3. Create urls for logout
        4. In navbar, add link to logout
        5. Try it to see the result 

        modified:   README.md
        modified:   templates/main.html
        modified:   users/urls.py
        modified:   users/views.py


#### 19.7 User restriction - Don't show login page to LOGGED IN user

        Steps:

        1. Use is_authenticated method
        2. Test it out to see the result

        modified:   README.md
        modified:   users/views.py


#### 19.8 User restriction - Blocking user to required authentication pages

        Steps:

        1. Import login_required method
        2. Add login_required to createProject
        3. Add login_required to updateProject
        4. Add login_required to deleteProject
        5. Test it out to see the result

        modified:   README.md
        modified:   projects/views.py


#### 19.9 Hiding the Add Project menu from un-logged in user

        Steps:

        1. Move the Add Project menu to inside the request.user.is_authenticated conditional
        2. Check the resutl

        modified:   README.md
        modified:   templates/main.html


#### 19.10 MESSAGES - Adding flash error message to login and logout

        Steps:

        1. Import messages modules
        2. Use messages module with error method
        3. Add message tags to main page
        4. See the results

        modified:   README.md
        modified:   templates/main.html
        modified:   users/views.py


#### 19.11 REGISTER Part 1 - Create registerUser view method (VUrls)

        Steps:

        1. Create userRegister view
        2. Create path

        modified:   README.md
        modified:   users/urls.py
        modified:   users/views.py


#### 19.12 REGISTER Part 2 - Adding conditional to login-register form

        Steps:

        1. Add conditionals
        2. See the results

        modified:   README.md
        modified:   users/templates/users/login_register.html


#### 19.13 REGISTER Part 3 - using UserCreationForm

        Steps:

        1. Import UserCreationForm module
        2. Define the UserCreationForm in registerUser view
        3. Use the instance of the UserCreationForm
        4. See the result

        modified:   users/templates/users/login_register.html
        modified:   users/views.py



#### 19.14 REGISTER Part 4 - Add logic to register a user

        Steps:

        1. Add the logic
        2. Register a new user for a test

        modified:   users/views.py



#### 19.15 REGISTER Part 5 - Authomatically login user after Signing up

        Steps:

        1. Use login session to login the new created user
        2. Redirect him to profiles page
        3. Show failed message if registration failed
        4. Test it out

        modified:   users/views.py



#### 19.16 REGISTER Part 6 - Create CustomUserCreationForm

        Steps:

        1. Create file users/forms.py 
        2. CustomUserCreationForm
        3. Remove UserCreationForm
        4. Import and use it in the registerUser view method
        5. Test it out and see the result

        modified:   README.md
        new file:   users/forms.py
        modified:   users/views.py



#### 19.17 REGISTER Part 7 - Change reg form field from 'First name' to 'Name'

        modified:   README.md
        modified:   users/forms.py



#### 19.18 REGISTER - LOGIN Part 1 - Adding template theme to login_register.html

        modified:   README.md
        modified:   users/templates/users/login_register.html
        new file:   users/templates/users/login_register_ori.html



#### 19.19 REGISTER - LOGIN Part 2 - Adding conditional to show login or register form


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.20 REGISTER - LOGIN Part 3 - Adding links to login and register


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.21 REGISTER - LOGIN Part 4 - Loading icon images


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.22 REGISTER - LOGIN Part 5 - Adding functionality to login form


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.23 REGISTER - LOGIN Part 6.1 - Adding functionality to register form (arranged the layout)


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.24 REGISTER - LOGIN Part 6.2 - Removing some input fields


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.25 REGISTER - LOGIN Part 6.3 - Add method, csrf_token and redering the {{form.as_p}}


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.26 REGISTER - LOGIN Part 6.6 - Looping the form field Part 1


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.27 REGISTER - LOGIN Part 6.7 - Looping the form field Part 2 (rendering label and input field)


        modified:   README.md
        modified:   users/templates/users/login_register.html


#### 19.28 REGISTER - LOGIN Part 6.8 - Looping the form field Part 3 (styling)


        modified:   README.md
        modified:   users/forms.py


#### 19.29 REGISTER - LOGIN Part 6.9 - Adding help_text to register form


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.30 REGISTER - LOGIN Part 6.10 - Adding alert/error message to register form


        modified:   README.md
        modified:   users/templates/users/login_register.html



#### 19.31 REGISTER - LOGIN Part 6.11 - Adding style to flash messages


        modified:   README.md
        modified:   templates/main.html
        modified:   users/views.py



#### 19.32 REGISTER - LOGIN Part 6.12 - Removing the flash message


        modified:   static/uikit/app.js
        modified:   templates/main.html



### 20. LINK MODIFICATION
### -----------------------------------------------------


#### 20.1 Modified link - to eas error from going to specific urer profile, but to profiles


        NOTE:
        
        1. Page: profiles.html 
        2. The link: {% url 'users:user-profiles' project.owner.id %}
        3. The link intends to go to specific user's profile

        ERROR:

        1. When go to: http://127.0.0.1:8000/project/
           it creates error like this:
           
           Reverse for 'user-profile' with arguments '('',)' not found. 1 pattern(s) tried: ['profile/(?P<pk>[^/]+)/$']

        SOLUTION:

        Instead of going to specifik profile, but go to profiles (profile list)

        1. Change the link:

        From: {% url 'users:user-profiles' project.owner.id %}

        To: {% url 'users:profiles' %}

        modified:   README.md
        modified:   projects/templates/projects/projects.html



### 21. USER ACTIONS
### -----------------------------------------------------


#### 21.1 Create account page VTUrls + link in navbar

        modified:   README.md
        modified:   templates/main.html
        new file:   users/templates/users/account.html
        modified:   users/urls.py
        modified:   users/views.py


#### 21.2 Hiding account menu from un-logged in user

        modified:   README.md
        modified:   templates/main.html


#### 21.3 Adding template theme to account page

        modified:   README.md
        modified:   users/templates/users/account.html


#### 21.4 Loading user information

        modified:   README.md
        new file:   static/images/log-good.JPG
        new file:   static/images/logo-1.JPG
        new file:   static/images/logo-1_kqRgXsk.JPG
        new file:   static/images/logo_kincir.JPG
        modified:   users/templates/users/account.html
        modified:   users/views.py

        NOTE:

        1. Logged in to access account page
        2. Logged in user can create project, but
           MUST manually add the owner of the project in admin by superuser


#### 21.5 Create editAccount page VTUrls

        modified:   README.md
        new file:   users/templates/users/profile_form.html
        modified:   users/urls.py
        modified:   users/views.py


#### 21.6 Link Account page with the editAccount page

        modified:   README.md
        modified:   users/templates/users/account.html


#### 21.7 Add basic form to editAccout (profile_form) page

        modified:   README.md
        modified:   users/templates/users/profile_form.html



#### 21.8 Add form fields to editAccunt page by using the Profile model attributes

        modified:   README.md
        modified:   users/forms.py
        modified:   users/templates/users/profile_form.html
        modified:   users/views.py


#### 21.9 Create updateUser signals to update profile and automatically update user, but NOT the oversit

        modified:   README.md
        modified:   users/signals.py


#### 21.10 Limiting the form fields to show on the editAccount page

        modified:   README.md
        modified:   users/forms.py


#### 21.11 Update the profile_form to be able to update image

        modified:   README.md
        modified:   users/templates/users/profile_form.html


#### 21.12 Add logic to editAccount view to processing the form

        modified:   README.md
        modified:   users/views.py


#### 21.13 EXTRA ORDINARY - Fixing the Reverse for 'user-profile' with arguments not found

        modified:   README.md
        modified:   projects/templates/projects/projects.html


#### 21.14 Sign up for a new account and redirect a newly signed up user to edit-account page

        modified:   README.md
        new file:   static/images/profiles/Nakula.PNG
        new file:   static/images/profiles/ing.jfif
        modified:   users/views.py


#### 21.15 STYLING THE profile_form page Part 1

        modified:   README.md
        modified:   users/templates/users/profile_form.html


#### 21.16 STYLING THE profile_form page Part 2

        modified:   README.md
        modified:   users/forms.py
        modified:   users/templates/users/profile_form.html



### 22. CRUD USER-BASED PROJECT
### -----------------------------------------------------


#### 22.1 Add links to account page

        modified:   README.md
        modified:   users/templates/users/account.html


#### 22.2 CRUD - CREATE : Add logic to createProject method for a specific user to create project

        modified:   README.md
        modified:   projects/forms.py
        modified:   projects/views.py
        new file:   static/images/logo-jet.JPG
        new file:   static/images/logo_conblock.PNG


#### 22.3 CRUD - UPDATE :  Add logic to updateProject method for a specific user to update a project

        modified:   README.md
        modified:   projects/views.py


#### 22.4 CRUD - DELETE :  Add logic to deleteProject method for a specific user to delete a project

        modified:   README.md
        modified:   projects/views.py


#### 22.5 Testing - The CRUD :)

        modified:   README.md
        new file:   static/images/IG_DB_DIAGRAM.PNG
        new file:   static/images/logo-i_saw_the_dog.PNG
        new file:   static/images/profiles/bima.PNG
        new file:   static/images/profiles/bima_YeycPq0.PNG
        new file:   static/images/profiles/bima_eZL8aJ4.PNG
        new file:   static/images/profiles/ing_FtH9pMH.jfif

        NOTE:

        1. user: bima -> username: warkudara
        2. user: ing  -> username: ing-nyoman



### 23. CRUD USER-BASED SKILL
### -----------------------------------------------------


#### 23.1 CRUD-Create Part 1: Create skill_form VTUrls

        modified:   README.md
        new file:   static/images/profiles/bisma_wgPZt41.PNG
        modified:   users/templates/users/account.html
        new file:   users/templates/users/skill_form.html
        modified:   users/urls.py
        modified:   users/views.py


#### 23.2 CRUD-Create Part 2: Create SkillForm model

        modified:   README.md
        modified:   users/forms.py


#### 23.3 CRUD-Create Part 3: Use SkillForm within the createSkill method and render it to skill_form

        modified:   README.md
        modified:   users/templates/users/skill_form.html
        modified:   users/views.py


#### 23.4 CRUD-Create Part 4: Styling the skill_form

        modified:   README.md
        modified:   users/templates/users/skill_form.html


#### 23.5 CRUD-Create Part 5: Add logic to createSkill method to process the skill_form

        modified:   README.md
        modified:   users/templates/users/skill_form.html
        modified:   users/views.py


#### 23.6 CRUD-Create Part 6: Testing create skill

        NOTE:

        :)


#### 23.7 CRUD-UPDATE: create updateSkill method and test it out

        modified:   README.md
        modified:   users/templates/users/account.html
        modified:   users/urls.py
        modified:   users/views.py


#### 23.8 CRUD-UPDATE: Showing Create Skill and/or hidding Update Skill skill_form header 

        modified:   README.md
        modified:   users/templates/users/skill_form.html
        modified:   users/views.py


#### 23.9 CRUD-DELETE: create deleteSkill method and test it out

        modified:   README.md
        new file:   templates/delete_template.html
        modified:   users/templates/users/account.html
        modified:   users/urls.py
        modified:   users/views.py

        NOTE:

        Tested :)


### 24. FLASH MESSAGES
### -----------------------------------------------------


#### 24.1 Add flash message to createSkill, updateSkill and deleteSkill

        modified:   README.md
        modified:   templates/delete_template.html
        modified:   users/views.py


### 25. SEARCH
### -----------------------------------------------------


#### 25.1. SEARCH - Scenario and Preparation

        NOTE:

        In the home page or the profiles page, we are going to search developers by certain attributes like:
        - the name or 
        - description 
        - and also by developer skills.

        And then in the projects page, we want to search projects by: 
        - title, 
        - also by the description attributes like the 
          - tags associated with it and even the developers.

        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 25.2. SEARCH - Testing the search result to terminal

        modified:   README.md
        modified:   users/views.py


#### 25.3. SEARCH - Search by name

        modified:   README.md
        modified:   users/views.py


#### 25.4. SEARCH - Keeping the search value remains in the box search

        modified:   README.md
        modified:   users/templates/users/profiles.html
        modified:   users/views.py


#### 25.5. SEARCH - Using Q look up for search 

        NOTE:

        The problem using search by name_icontains was that
        we can not search by name and by short_intro. 

        Example: 

        Ref: the Profile model

        name: dennis
        short_intro: problem using javascript

        If name and short_intro did not have the same characters (n), then the result will be empty.

        Q look up search will solve the problem.

        modified:   README.md
        modified:   users/views.py


#### 25.6. SEARCH - Using distinct and icontains for multiple search and search for skill as well

        modified:   README.md
        modified:   users/views.py

























































































