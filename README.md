# Hawk-a-Delight

Full Stack Frameworks with Django Milestone Project

## Index

1. [Project Purpose](#project-purpose)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## <a name="project-purpose">Project Purpose</a>

The premise of Hawk-a-Delight is:
1. To allow users to order and pay for food dishes online
2. To allow users to submit their own recipes to be included as part of the menu
3. To allow users to comment and vote on the user submitted recipes

## <a name="ux">UX</a>

The goal in the design is to present data in a systematic approach that encourages first time learning

The user stories considered are:
* I want to register for the website
* I want to browse the available menu items available
* I want to be able to order the menu items, view the items in a cart and purchase it online
* I want users to be able to submit their recipes and suggest it in the menu
* I want the users to be able to rate the recipes by adding reviews and to upvote the recipes

A tree structure information architecture is used for the website as it reduces complexity and only reveals information as the user navigate and transverse up and down the tree.

The color orange is predominately used in this website as it is an appetizing and trendy color. The logo is symmetrical to provide a sense of balance and blue for the users

To reduce cognitive overload, the user will also not be required to go beyond 5 clicks to get to their destination.

The ER diagram, scope and wireframe can be found under the scope and skeleton folder.


## <a name="features">Features</a> 

### Existing Features

1. Home/Index Page
   * Mobile Responsive Bar that allows easy navigation with different navigation links depending on whether the user is logged in or not for all the pages.
   * Display image and registration form to prompt the user to create an account if they do not have one
   * Mobile Responsive Testimonials by other users
   * Footer that shows the company's address, email and opening hours in all pages
 
2. Register/Login/Forgot your password pages (Links available in the nav bar when the user is not logged in)
   * Relevant forms for the user to register, login and request for a new password

3. Profile and Logout pages (only available when user is logged in)
   * Allows the user to check their user details in profile and log out 
   * A message will be shown if the user is successfully logged out

4. Menu page
   * Displays a list of menu dishes that are available to order
   * Clicking the menu dishes will reveal more details such as description, prices and allow the users to add it to cart
   * Breadcrumb links are provided below the nav bar for easy navigation
   * A search field is provided for the user to search the existing menu dishes
   * Adding the menu item to cart will show the total amount of items in the cart on the navigation bar
   * Messages will be shown if the item has been successfully added to the cart or if there is an error.
 
5. Suggest a dish > Submit Recipe page
   *  A form will be shown for the user to submit the recipe, if successful, a message will be shown
   *  Breadcrumb links are provided below the nav bar for easy navigation

6. Suggest a dish > List of submitted recipes page
   * It will show a list of user suggested recipes with a summary of the times viewed and the number of votes it has
   * A search field is provided for the user to search the user submitted recipes
   * It allows the user to click on the recipe for more details

7. Recipe Details Page
   * Breadcrumb links are provided below the nav bar for easy navigation
   * It will show the recipe details such as the name, user that submitted, cooking time, date it was suggested, etc.
   * It allows only the user who submitted the recipe to edit and delete the recipe
   * Other users may upvote or review/comment on the recipe
   * It will also show the reviews/comments by other users and is shown as a title, comment and commented by.
   * A show/hide button to show or hide the reviews/comments by other users
   * It allows only the user who submitted the review to edit and delete the review.

8. Shopping Cart Page
   * Breadcrumb links are provided below the nav bar for easy navigation
   * It lists down the items added to the cart, quantity and total amount
   * It allows the user to change the quantity of the menu items ordered
   * It allows the user to check out the shopping cart
   * Messages will be shown if the item quantity has been successfully adjusted or if there is an error.

9. Check out Page
   *  Breadcrumb links are provided below the nav bar for easy navigation
   *  Billing information such as the items ordered, subtotals and total
   *  Form for user to perform an online transaction using Stripe
   *  Messages will be shown if user has successfully in making payment or if there is an error.

### Features left to implement

Due to scope creep and insufficient time, the following features have yet to be implemented:
1. To be able to send a reset password email to the user when the user submits the form for forgot password.
2. To limit the number of votes per user to only 1
   

## <a name="technologies-used">Technologies Used</a>

1. HTML (https://www.w3schools.com/html/html_intro.asp)
2. CSS (https://www.w3schools.com/css/)
3. Bootstrap (https://getbootstrap.com/): The frontend was built using Bootstrap framework
4. Javascript (https://www.javascript.com/)
5. JQuery (https://jquery.com/): The project uses JQuery to simplify DOM manipulation.
6. Python (https://www.python.org/)
7. Whitenoise (https://pypi.org/project/whitenoise/): Used to serve static files
8. UploadCare (https://uploadcare.com/): To upload images
9. PostgreSQL (https://www.postgresql.org/)
10. Django (https://www.djangoproject.com/)

## <a name="testing">Testing</a>

Automated testing is conducted for the models found in "checkout_app" and "submitrecipe_app"

The automated tests can be run by typing "python3 manage.py test"

Manual Testing:

1. Home/Index Page
   * Test that the navigation bar is mobile responsive and the links are working.
   * Check that the links on the navigation bars are correct depending on whether the user is logged in or not
   * Test that Registration form is working
   * Check that the testimonials are mobile responsive and the footer shows the company's address, email and opening hours in all pages
 
2. Register/Login/Forgot your password pages (Links available in the nav bar when the user is not logged in)
   * Test that the relevant forms work. (Note: an email will not be sent for Forgot your password as it is yet to be implemented)

3. Profile and Logout pages (only available when user is logged in)
   * Check tjat the user is able to check their user details in profile and log out 
   * Check that a message will be shown if the user is successfully logged out

4. Menu page
   * The list of menu dishes available to order are shown and mobile responsive
   * Clicking the menu dishes will reveal more details such as description, prices and allow the users to add it to cart
   * Check that Breadcrumb links are working
   * Test that the search field is working
   * Adding the menu item to cart will show the total amount of items in the cart on the navigation bar
   * Messages will be shown if the item has been successfully added to the cart or if there is an error.
 
5. Suggest a dish > Submit Recipe page
   *  Test that the suggest a recipe page is working, if successful, a message will be shown
   *  Breadcrumb links are working

6. Suggest a dish > List of submitted recipes page
   * A list of user suggested recipes with a summary of the times viewed and the number of votes it has
   * Test that the search field is working
   * It shows recipe details when the user clicks on the recipe

7. Recipe Details Page
   * Breadcrumb links are working
   * Recipe details such as the name, user that submitted, cooking time, date it was suggested, etc are shown.
   * It allows only the user who submitted the recipe to edit and delete the recipe
   * Other users may upvote or review/comment on the recipe
   * It will also show the reviews/comments by other users and is shown as a title, comment and commented by.
   * The show/hide button to show or hide the reviews/comments is working
   * It allows only the user who submitted the review to edit and delete the review.

8. Shopping Cart Page
   * Breadcrumb links are working
   * It lists down the items added to the cart, quantity and total amount
   * It allows the user to change the quantity of the menu items ordered
   * It allows the user to check out the shopping cart
   * Messages will be shown if the item quantity has been successfully adjusted or if there is an error.

9. Check out Page
   *  Breadcrumb links are working
   *  Billing information such as the items ordered, subtotals and total
   *  Form for user to perform an online transaction using Stripe
   *  Messages will be shown if user has successfully in making payment or if there is an error.

## <a name="deployment">Deployment</a>

The website has been deployed at https://hawkadelight.herokuapp.com/

### Heroku Deployment

#### Installing dependencies and folders

1. Type in "sudo apt install libpq-dev python3-dev" in the terminal
2. Install the following using pip3:
   * sudo pip3 install gunicorn
   * sudo pip3 install psycopg2
   * sudo pip3 install whitenoise

3. Add whitenoise, 'whitenoise.middleware.WhiteNoiseMiddleware', to the middleware inside settings.py
4. Make sure the following are the settings for static files and uploads
   * STATIC_URL = '/static/'
   * STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
   * STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   * MEDIA_URL = '/media/'
   * MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
5. Create the requirements.txt "pip3 freeze --local > requirements.txt"
6. Create a repository for the project and connect it to GitHub Include the relevant gitignore files
7. Log into heroku by typing in heroku login and pressing ENTER
8. Create an app via a command line:
   * heroku create <PROJECT NAME>

#### Installing Postgres SQL

9. Type in "heroku addons:create heroku-postgresq"
10. Install with pip3 "sudo pip3 install dj_database_url"
11. Add the URL to the database configurations inside settings.py
12. Migrate the database

#### Setting the environment variables

13. Set the Stripe and UploadCare environment variables
14. Log into Heroku using CLI
15. Set the environment variables using the CLI in this format:
    * heroku config:set STRIPE_PUBLISHABLE_KEY= <INSERT KEY HERE>
    * heroku config:set STRIPE_SECRET_KEY= <INSERT KEY HERE>
    * ...
16. Get the latest requirements.txt file
17. Create the Procfile, "touch Procfile"
18. Enter "web: gunicorn <PROJECT_FOLDER>.wsgi:application" in the Procfile
19. Add the URL of the heroku app into the ALLOWED_HOST inside settings.py
20. Add and commit, and create the superuser on the Heroku app:
    * sudo git add .
    * sudo git push heroku master
    * heroku run python manage.py createsuperuser

#### To re-generate requirements.txt after installing more packages
1. pip3 freeze --local > requirements.txt
2. git add .
3. git commit -m ​"Updated requirements.txt"
4. git push heroku master

#### Running the application locally
1. Create a new workspace in C9 with a workspace name and description
2. Clone the github repository at https://github.com/WenQingLee/Hawk-a-Delight_Milestone_Project.git
3. Install requirements
4. The secret key and session key has to be created in the environment
5. In the project settings set debug to True.
6. To run the application locally type "python3 manage.py runserver localhost:8080"


## <a name="credits">Credits</a>

### Content
1. The menu items were compiled from the website: https://www.authenticfoodquest.com/food-in-singapore
2. The user submitted recipes are compiled from: https://www.blueapron.com/cookbook

### Media
The media used in this site were obtained from:
1. Pexels, a stock image library. (Photos)
2. Photos of the menu items are from: https://www.authenticfoodquest.com/food-in-singapore (Photos)
3. Fonts and icons were taken from FontAwesome
4. No photo available image: By en:User:Cburnett - Own work (Original text: Own work in Inkscape), Public Domain, https://commons.wikimedia.org/w/index.php?curid=1841287
5. The photos for the recipes are taken from: https://www.blueapron.com/cookbook

### Acknowledgements
I received inspiration for Responsive Contact Us: https://codepen.io/anupkumar92/pen/PLLzNb