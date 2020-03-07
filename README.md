# Sima's Recipes
## Practical Python and Data-Centric Development Milestone Project

I have chosen to create a cook book from project ideas suggested by Code Institute to test myself, that would I be able to fulfil all the requirements as requested and test my knowledge from previous two modules. Also, I am not a good cook, but with this cookbook I might be able to ask my friends and family to add some recipes which I can try and learn some yummy recipes and keep record of it rather than flipping cookery book pages or searching online.

My idea is to keep design simple using well known website template, which help user(s) or customer(s) navigate through website easily with confident. Also, I have kept in mind that having website full of content and loads of information on single page will make it look tawdry. My intention is to have simple yet information rich webpages with modern and attractive design.

## Access my project on GitHub

https://github.com/hidayatmansuri/simas-recipes

or Deployed version (Published version) on HEROKU

http://simas-recipes.herokuapp.com

## Technologies

1. HTML
2. CSS
3. JavaScript
4. jQuery
5. Bootstrap (4.3.1)
6. Fontawesome
7. Google Fonts
8. Balsamiq Mockups 3
9. ScreenToGif
10. emailjs
11. Materializecss
12. Snipping Tools

## UX

This project is for those people who like to have their recipes on one place and can be able to find them easily as and when they like to cook something. Also, for those users who is learning from their friends and family but not able to get hold them as and when they need help with recipe they like to cook.

For Example: If I would like to cook Chicken Madras curry over the weekend with help of my friend who is not available on that particular day. I can ask my friend to add that recipe into my cookbook as when she have sometime before weekend. That is how I can cook Chicken Madras curry with help of my friend without disturbing her on weekend. Once I get recipe in my cookbook and having administrative rights, I can place that recipe in particular category or place where is most suitable and easier for me to find in future.

I have kept design simple with Dashboard where all recipes will be shown in different category and type as well as cooking time. That means all the recipes will be taps away. Also, on the recipe page, all recipes will be sorted category and cuisine wise in stackable manner which I have manage to achieve with help of materializecss collapsible design.

Let's say, If I have managed to get 3 different recipes for Lamb with all Ingredient and Methods. Recipes page will be mile long and scrolling up and down to find beginning and end of recipe will be mayhem. That is why I have used collapsible element, where only name of the recipes will be shown as heading, by clicking on recipe name it will roll down to reveal ingredient, method and other content.

## User Stories

### How Recipe can be added?

This will begin with clicking or taping on Admin option from Menu which will bring you to Login page, where you can either use existing username and password or create new user.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/LoginPage.JPG

Once you are Logged in, you will be presented with Admin page with your username displayed on top with option to Add, Delete or Update Recipe, Category or Cuisine. By clicking on Add New Recipe heading it will display form where you can add all required detail and press Add Recipe at bottom will add new recipe to database.

#### Wireframes
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Admin_page.png

#### Desktop View
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/LoggedIn.JPG

### How can I edit Recipe?

Edit recipe can be done on Admin page. Which work almost similar way as Add New Recipe by Logging in. Once user logged in they can scroll down to List of Recipes, once user get to the list, user can click on recipe name which they like to Edit, which will collapse whole recipe with Edit and Delete button on top. Click on Edit button which will bring Edit page with all recipes data, where user can make amendment. Once amendment is done, they can simply click on Edit Recipe button which they can check on same admin page by visiting same recipe again.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/EditRecipe.JPG

### How can I Edit Category or Cuisine?

All Editing can be done on Admin page. Once user logged in they can scroll down to either list of categories or List of Cuisines at towards bottom of the page. Same as Edit recipe, user can click/tap on category or cuisine list which will bring list with Edit and Delete button displayed before each category and cuisine. By clicking Edit button user make amendment.
#### Edit Delete Category
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/EditDeleteCategory.gif

#### Edit Delete Cuisine
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/EditDeleteCuisine.gif

### How Dashboard works?

Dashboard is overview of all the recipes and categories added so far. Dashboard represent all content added or stored in database. I have created clickable or tapeable cards on Dashboard which can take user to list of category or recipes they are interested in.

For Example, if user only interested in Chicken recipes, they could tap on chicken card which will present them with list of all Chicken recipes we have. If user only interested in recipes which can be ready in under 30 mins, user could tap on under 30 mins card and it will take user to list of recipes which can be ready in under 30 mins. Also, if user only interested in European Cuisine, user could tap on European card which will bring list of European cuisines recipes.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/Dashboard-Category.gif

### How Recipes page works?

Recipe page can be reached by clicking on Recipes option from Menu or once user have come to the particular category or cuisine view from there user can click on Recipes which can also bring user to Recipes page. Recipes page have list of category and list cuisine on top of the page followed by list of recipes category wise and List of recipes cuisine wise. Whole page is accessible by scrolling down, but also can be reached to particular category or cuisine by simply clicking/tapping on options provided. 

For Example, if you like to see list of recipes which are South Asian Cuisines. Click on 'List of Cuisines' which will collapse and represent you with list, from where click on 'South Asian Cuisine' and it will take you to list of south Asian cuisines recipes.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/CategoryList-Recipes.gif
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/CuisineList-Recipes.gif

### What is the best way to come to the top of the page?

On this project there 3 pages which are long and can even get more longer as and when new content will be added which are Dashboard, Recipes and Admin. This page can be access via scrolling up and down, but for convenience there is 'TOP' floating button on right bottom of the screen. By clicking on that floating button will bring you top of the page.
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/TopButton.gif

##### Mobile
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Recipe_page_iPhone.png

##### Project
!https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/stackable_design.JPG

## Features

### Dashboard

I have created index page as Dashboard for this project where all the information will be available on single display. With one tape it will land you on particular recipe list which include Category wise, cooking time wise as well as cuisine wise. I have divided cuisines in 12 different regions.

#### Wireframes
##### Desktop
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard.png

##### Tablet
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard_iPad.png

##### Mobile
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard_iPhone.png

##### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/Dashboard-Category.gif

### Contact Us & Chat

I have also added Contact Us and chat functions for this project where someone can get in touch as well as can chat with me as well. Chat functionality is very basic, and it is kind of Group chatting rather than one to one chat.

#### Wireframe

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/ContactUs_Page.png

### Admin

Import part of this project where I have demonstrated knowledge, I have gain during this module which is to carry out CRUD (Create, Read, Update, Delete) functions. Where I have started with creating login page which also allow user to create new user themselves. I have used crypting functionality for password. Once successfully created or logged in, user will be able to carry out CRUD functions.

#### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/CreateNewUser.JPG
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/LoginPage.JPG

With CRUD function, user can Add, Update and Delete Recipes, Categories and Cuisines. Too keep admin page tidy and clean I have used materializecss collapsible element. In which I have added whole 'Create New Recipes' form in collapsible element as well as Add new Category and Cuisines

##### Wireframe
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Admin_page.png

##### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/NewRecipes.JPG
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/NewCategory%26Cuisine.JPG

### Recipes

I have used collapsible element from materializecss for modern attractive design as well as for clutter free page. Collapsible element hides all content under as heading which can be accessed by clicking or taping on heading. I have also used floating button element on Recipes page as well on Dashboard and Admin page to navigate top of the page with only a click or tap.

##### Wireframe
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Recipe_page_contentview.png
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Recipe_page_iPad.png
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Recipe_page_iPhone.png

##### Project View
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/Collapsible.gif
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/img/RecipeView.JPG

## Feature left to Implement

### Chat

I have included chat functionality to this project, where chatting can take place between users. But this functionality works as group chatting rather than one to one. I am planning to implement in future where one to one chat will be possible

### Admin

Also, with Admin functionality all the recipes are available to amendment and edit to all the users regardless who added recipe. I will be adding this functionality in future where user can amend, edit and view only recipes which was added by them once they logging with right credentials. I am also planning to add some more functions such as favourite, serve for etc.

### Edit & Delete

I have included Edit and Delete functionality to this project where user can make amendment to recipe, category or cuisine. But as and when Edit or Delete button pressed there is no prompt alert that you are going make amendment to particular field, which I would like to improve in future. This will reduce accidental deletion to the content.

## Testing

I have tested this project on number or devices and different browser. I have come across to issues which are loading main image on slow connection and if you have firewall installed it will prompt you with warning that this website is not safe.

Issue with loading main image in heeder background, I will either change image and have lower resolution small image or make take it off completely in future

For firewall issue I will advise user to carry on with unsafe mode as for now but will in future will improve to have secure environment.

Also, devices with screen width of 601px to 767px having problem with missing menu background, which set to transparent. I have tried to rectify this problem but having so many CSS dependencies such as materialize.css and bootastrap.css on top my own version of style.css. It is almost impossible to come over this issue, changing one element creating another hugh problem.

I have tested this project on
##### Mobile Devices
Pixel 3xl, HTC U12+, iPhone 11 Pro, Microsoft Lumia 920, HTC M8, One Plus Two, One Plus 7T, iPhone 8, Poco Phone

##### Browsers
Google Chrome, Firefox Mozilla, Brave, Opera, Vivaldi, Internet Explorer, Microsoft Edge browser

##### Tablet
iPad 6th Gen, Samsung Tab 2, Acer Iconic, iPad Air 2

## Deployment

### Github Deployment Process

1.  Sign in / Sign up on pages.github.com
2.  Create a repository with available name
3.  from AWS Cloud 9 bash run following commands
4.  git init
5.  git add . - to add file(s) to staging area
6.  git commit -m "with message" - commit file(s)
7.  git remote add origin followed by URL (from github website for first time)
8.  git push - followed by username and password to upload file(s) to github

### Deployment to HEROKU

1.  Sign in / Sign up on www.heroku.com
2.  On heroku website create new app with right region
3.  from AWS Cloud 9 bash run following commands
4.  heroku login - which will prompt with username and password created on heroku website
5.  git status - for status of file(s)
6.  git init
7.  git add . - Add file to staging area
8.  git commit -m "Message" - to commit files with meaningful message which help you in future to understand what changes have been made
9.  heroku git:remote -a project name (for first time)
10. git remote add heroku URL (Can be achieve from heroku settings)
11. Add requirement.txt with following command
12. sudo pip3 freeze --local > requirements.txt - for list of dependacy of our project
13. Add procfile with following command
14. echo web: python run.py > Procfile - Python file which help application mechanism on what command should run
15. heroku ps:scale web=1 - to scall your web to one running dynos
16. on heroku website go to APP and SETTINGS
17. click on reveal config vars where IP and PORT needs to be added or if you are MongoDB URL should be added in this field
18. from AWS cloud 9 bash run following command to deploy whole app on heroku
19. git push heroku master
20. Finally, on heroku website go to MORE and Click on RESTART ALL DYNOS
21. All these steps will make your app available on website which is "appname.herokuapp.com"

## Credit

### Content

All text content for this project is copied from BBC Good Food, where I have had prior acknowledgement in written to use as for this academic project.

### Media

Most of the recipe images have been taken from BBC Good Food as well with prior written acknowledgement to use on this academic project

### Acknowledgements

I have also used Medium website for some inspiration and ideas for this project as well as Stack Overflow for understanding some functions

My Login page idea is taken from Pretty Printed https://prettyprinted.com

https://www.youtube.com/watch?v=vVx1737auSE