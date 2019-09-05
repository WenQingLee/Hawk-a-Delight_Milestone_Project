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
* I want

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement
Another feature idea
Technologies Used
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

 1. Django Tips: https://medium.com/@DoorDash/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5 
 2. Website Design Theme: https://colorlib.com/wp/template/vegefoods/ 
 3. Website dishes: https://www.authenticfoodquest.com/food-in-singapore
 4. Fonts and icons were taken from FontAwesome
 5. Photos were taken from Pexels, a stock image library.
 5. Responsive Contact Us: https://codepen.io/anupkumar92/pen/PLLzNb
 6. Menu Items are taken from: https://www.authenticfoodquest.com/food-in-singapore/
 7. No photo available image: By en:User:Cburnett - Own work (Original text: Own work in Inkscape), Public Domain, https://commons.wikimedia.org/w/index.php?curid=1841287