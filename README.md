# Hawk-a-Delight

Full Stack Frameworks with Django Milestone Project

## Index

1. Project Purpose
2. UX
3. Features
4. Technologies Used
5. Testing
6. Deployment
7. Credits

## Project Purpose

The premise of Hawk-a-Delight is:
1. To allow users to order and pay for food dishes online
2. To allow users to submit their own recipes to be included as part of the menu
3. To allow users to comment and vote on the user submitted recipes

## UX

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


## Features

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
   

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment


===

In the terminal, type in the following:

sudo apt install libpq-dev python3-dev

Install the following using pip3:

sudo pip3 install gunicorn
sudo pip3 install psycopg2
sudo pip3 install whitenoise

Add Whitenoise to the middleware inside settings.py



MIDDLEWARE = [
'whitenoise.middleware.WhiteNoiseMiddleware'
]


Make sure to include the following settings for static files and uploads, if they are not there already:



STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


Create a static folder in the workspace (where manage.py is) and create an empty text file inside there.


Create a staticfiles folder in the workspace and create an empty text file inside there


Create a media folder in the workspace and create an empty text file inside there.


Remove media/ from the .gitignore file temporarily. (If you have added /media inside there).

Create a static folder in the workspace (where manage.py is) and create an empty text file inside there.


Create a staticfiles folder in the workspace and create an empty text file inside there


Create a media folder in the workspace and create an empty text file inside there.


Remove media/ from the .gitignore file temporarily. (If you have added /media inside there).

Create the requirements.txt file using bash



pip3 freeze --local > requirements.txt


Create a local git repo for your project and connect it to a GitHub repo. Include the relevant .gitignore file.  


sudo git init 
sudo git add .
sudo git commit -m "First commit"
sudo git remote add origin <GITHUB REMOTE URL>
sudo git push origin master

Put staticfiles/  and media/ inside .gitignore


Log into heroku by typing in heroku login and pressing ENTER



Put staticfiles/  and media/ inside .gitignore

Create an app ( do it via the command line, don't do it via the Heroku webpage). If you opt for the command line and the push to Heroku


heroku create <PROJECT NAME> 
git remote -v

Type in:



heroku addons:create heroku-postgresql



Install with pip3:



sudo pip3 install dj_database_url


Add the URL to the database configurations inside settings.py



# import at the top
import dj_database_url
# then...
DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}






===

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X

Uploadcare
whitenoise


 1. Django Tips: https://medium.com/@DoorDash/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5 
 2. Website Design Theme: https://colorlib.com/wp/template/vegefoods/ 
 3. Website dishes: https://www.authenticfoodquest.com/food-in-singapore
 4. Fonts and icons were taken from FontAwesome
 5. Photos were taken from Pexels, a stock image library.
 5. Responsive Contact Us: https://codepen.io/anupkumar92/pen/PLLzNb
 6. Menu Items are taken from: https://www.authenticfoodquest.com/food-in-singapore/
 7. No photo available image: By en:User:Cburnett - Own work (Original text: Own work in Inkscape), Public Domain, https://commons.wikimedia.org/w/index.php?curid=1841287