# Sima's Recipes
## Practical Python and Data-Centric Development Milestone Project

I have chosen to create a cook book from project ideas suggested by Code Institute to test myself, that would I be able to fullfill all the requirements as requested and test my knowledge from previous two modules. Also, I am not a good cook, but with this cookbook I might be able to ask my friends and family to add some recipes which I can try and learn some yummy recipes and keep record of it rather than flipping cookery book pages or searching online.

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
9. Google Maps JavaScript API
10. emailjs
11. Materializecss

## UX

This project is for those people who like to have their recipes on one place and can be able to find them easily as and when they like to cook something. Also, for those users who is learning from their friends and family but not able to get hold them as and when they need help with recipe they like to cook.

For Example: If I would like to cook Chicken Madras curry over the weekend with help of my friend who is not available on that perticular day. I can ask my friend to add that recipe into my cook book as when she have sometime before weekend. That is how I can cook Chicken Madras curry with help of my friend without disturbing her on weekend. Once I get recipe in my cookbook and having administrative rights, I can place that recipe in perticular category or place where is most suitable and easier for me to find in future.

I have kept design simple with Dashboard where all recipes will be shown in different category and type as well as cooking time. That means all the recipes will be taps away. Also, on the recipe page, all recipes will be sorted category and cuisine wise in stackable manner which I have manage to achieve with help of materializecss collapsible design.

Let's say, If I have manage to get 3 different recipes for Lamb with all Ingredient and Methods. Recipes page will be mile long and scrolling up and down to find beggining and end of recipe will be mayhem. That is why I have used collapsible element, where only name of the recipes will be shown as heading, by clicking on recipe name it will roll down to reveal ingredient, method and other content.

## User Stories

### How Recipe can be added?

This will begin with clicking or taping on Admin option from Menu which will bring you to Login page, where you can either use existing username and password or creat new user.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/LoginPage.JPG

Once you are Logged in, you will be presented with Admin page with your username displayed on top with option to Add, Delete or Update Recipe, Category or Cuisine. By clicking on Add New Recipe heading it will display form where you can add all required detail and press Add Recipe at bottom will add new recipe to database.

#### Wireframes
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Admin_page.png

#### Desktop View
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/LoggedIn.JPG

### How can I edit Recipe?

Edit recipe can be done on Admin page. Which work almost similar way as Add New Recipe by Logging in. Once user logged in they can scroll down to List of Recipes, once user get to the list, user can cllick on recipe name which they like to Edit, which will collapse whole recipe with Edit and Delete button on top. Click on Edit button which will bring Edit page with all recipes data, where user can make amendment. Once amendment is done they can simply click on Edit Recipe button which they can check on same admin page by visiting same recipe again.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/EditRecipe.JPG

### How can I Edit Category or Cuisine?

All Editing can be done on Admin page. Once user logged in they can scroll down to either list of categories or List of Cuisins at towards bottom of the page. Same as Edit recipe, user can click/tap on category or cuisine list which will bring list with Edit and Delete button displayed before each category and cuisine. By clicking Edit button user make amendement.
#### Edit Delete Category
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/EditDeleteCategory.gif

#### Edit Delete Cuisine
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/EditDeleteCuisine.gif

### How Dashboard works?

Dashboard is overview of all the recipes and categories added so far. Dashboard represent all content added or stored in database. I have created clickable or tapable cards on Dashboard which can take user to list of category or recipes they are interested in.

For Example, if user only interested in Chicken recipes, they can tap on chicken card which will present them with list of all Chicken recipes we have. If user only interested in recipes which can be ready in under 30 mins, user can tap on under 30 mins card and it willtake user to list of recipes which can be ready in uder 30 mins. Also, if user only interested in European Cuisine, user can tap on European card which will bring list of european cuisines recipes.

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard-Category.gif

### How Recipes page works?

Recipe page can be reached by clicking on Recipes option from Menu or once user have come to the perticular category or cuisine view from there user can click on Recipes which can also bring user to Recipes page. Recipes page have list of category and list cuisine on top of the page followed by list of recipes category wise and List of recipes cuisine wise. Whole page is accessible by scrolling down, but also can be reached to perticular category or cuisine by simply clicking/tapping on options provided. 

For Example if you like to see list of recipes which are South Asian Cuisines. Click on 'List of Cuisines' which will collapse and represent you with list, from where click on 'South Asian Cuisine' and it will take you to list of south asian cusines recipes.


##### Mobile
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Recipe_page_iPhone.png

##### Project
!https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/stackable_design.JPG



### Dashboard

I have created index page as Dashboard for this project where all the information will be available on single display. Even with one tape it will land you on perticular recipe list which include Category wise, cooking time wise as well as cuisine wise. I have devided cuisines in 12 different region.

#### Wireframes
##### Desktop
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard.png

##### Tablet
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard_iPad.png

##### Mobile
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard_iPhone.png

##### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Dashboard-Category.gif

### Contact Us & Chat

I have also added Contact Us and chat functions for this project where someone can get in touch as well as can chat with me as well. Chat functionality is very basic and it is kind of Group chatting rather than one to one chat.

#### Wireframe

https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/ContactUs_Page.png

### Admin

Import part of this project where I have demonstrate knowledge I have gain during this module which is to carry out CRUD (Create, Read, Update, Delete) functions. Where I have started with creating login page which also allow user to create new user themselve. I have used crypting functionality for password. Once succesfully created or logged in, user will be able to carry out CRUD functions.

#### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/CreateNewUser.JPG
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/LoginPage.JPG

With CRUD function, user can Add, Update and Delete Recipes, Categories and Cuisines. Too keep admin page tidy and clean I have used materializecss collapsible element. In which I have added whole 'Create New Recipes' form in collapsible element as well as Add new Category and Cuisines

##### Wireframe
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/Admin_page.png

##### Project
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/NewRecipes.JPG
https://github.com/hidayatmansuri/simas-recipes/blob/master/static/wireframe/NewCategory%26Cuisine.JPG

