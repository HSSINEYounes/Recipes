Project Report
Description :
The website will allow users to discover cooking recipes, make comments and also rate them.
Features defining the Site:
Templates: For storing recipe information, ingredients, comments and notes.
At the Python code level, the Django framework is used to define a database model for a recipe application.

The class recipedefines a recipe template that contains fields such as title, difficulty, URL, image, and ingredients needed. The method __str__()is defined to return the title of the recipe.

The class RecipeRatingdefines a note template for a recipe. It uses a foreign key to link a note to a recipe and user, and an integer note field between 1 and 5.

The class Userinherits from Django's class AbstractUserand adds group and permission relationships for users.

The class commentdefines a comment template for a recipe. It uses a foreign key to link a comment to a recipe and a user, as well as a body text field and a creation date.

Finally, the class favouritesdefines a favorite template for a recipe. It uses a foreign key to link a recipe to a user.

Overall, this code defines a database model for storing user recipes, ratings, comments, and favorites information for a recipe app.

Views: To view the home page, recipe pages, ingredient pages, review pages, and profile pages.
The code contains several functions:

The function profile(request): displays the profile of the connected user with a list of his favorite recipes.
The function search(request): allows you to search for recipes from a given keyword.
The Function get_recipe_blocks(): This function uses the BeautifulSoup library to pull recipe data from a recipe website. The extracted data is stored in a database.
The function recipe_list(request): this function displays a list of all the recipes present in the database. It also allows you to navigate between the different pages of the list. If a user is logged in, the function also displays the recipes he has marked as favourites.
The function recipe_detail(request, pk): this function displays the details of a specific recipe selected by the user. It also displays the average rating given by users to this recipe, as well as comments left by users.
The code uses several libraries and modules such as requests, beautifulsoup4and Paginatorfrom Django. HTML templates are also included to render app content.

Templates: To display data in an attractive layout.
database.html:
This is an HTML template base for a web application that allows you to search, view and add culinary recipes. It includes a navigation bar with a search form, links to login or register and a drop-down menu to access the user profile and logout. The code is written using the Bootstrap framework for styling and layout and also uses JavaScript to make the search form interactive. The code is well structured using content blocks (blocks) which allow to add specific content in each page of the application.

login.html:
This code represents an HTML login page that uses the Bulma CSS framework. The code also uses the Django tag {% load static %}to load static files (such as CSS and JS files) from the staticapplication directory. The page displays a login form that contains input fields for username and password. The form is submitted using the POST method, which means the login information is sent securely to the server. The page also contains two links, one to create a new user account ( Create account), and the other to access the list of recipes without logging in ( Continue without logging in).

profile.html:
This code represents a Django template that extends a base template called 'base.html' and defines specific content for the 'content' block. The template includes tags to display the profile of the logged in user, their favorite recipes and the pagination of these recipes. It also uses conditional tags to handle cases where the user has no favorite recipes. The code also contains links that allow the user to delete recipes from their favorites or view a recipe without logging in.

recipe_details.html:
The code provided is an HTML page that displays the details of a cooking recipe, including ingredients, instructions, and comments. It also allows logged in users to rate the recipe and displays similar recipes at the end of the page.

recipe_list.html:
This code is an HTML template using the Django template language. The HTML file extends another base file base.htmland uses a series of Django-specific tags and filters to display a list of recipes.

The code starts by checking whether the user is logged in or not. If the user is logged in, the variable lfinalcontaining the user's recipes with additional recipe information is used to display the recipes. Otherwise, the variable recipescontaining all the recipes is used.

The loop foris used to loop through all the recipes in the appropriate variable ( lfinalor recipes) and display each recipe's information, including an image, preparation time and difficulty, and a link to the recipe's detail page .

Finally, the code uses a pagination system to display recipes on multiple pages.

register.html:
It is a web page written in HTML with the use of CSS Bulma library. This is a registration page containing a form with fields to enter username, email and two password fields for confirmation. There is also a "Submit" button to submit the form and a link to return to the login page. The form uses a CSRF token to protect against CSRF type attacks.

Authentication and authorization: For users and an authorization system for comments and ratings.
Search: For recipes and ingredients.
Pagination: For recipe and ingredient lists.
Web scraping: To grab recipe and ingredient information from other cooking sites and import it into the site.
requirements.txt:
This code is a list of Python dependencies with their versions. These dependencies are required to run a Django application. Here are the dependencies included in the list:

asgiref==3.6.0: a module that provides utilities for Python applications that use ASGI (Asynchronous Server Gateway Interface).
distlib==0.3.6: a library for the Python distribution.
Django==4.1.7: A Python web framework used for web application development.
filelock==3.9.0: a Python library that provides file locking mechanisms.
platformdirs==3.1.1: A Python library for managing platform-specific configuration and data directories.
sqlparse==0.4.3: an SQL query parser for Python.
tzdata==2022.7: A time zone database for Python.
virtualenv==20.21.0: a tool for creating isolated Python runtime environments.
urls.py:
This code defines the URLs for a Django application, importing the corresponding views from a views.py. URLs include:

recipe_list: displays a list of recipes
recipe_detail: displays the details of a particular recipe
search: perform a search for recipes
profile: displays the profile of the connected user
rate_recipe: allows a user to rate a recipe
register: displays a registration form for new users
login: displays a login form for existing users
logout: allows a user to log out
add_comment: allows a user to leave a comment on a recipe
addToFavourites: allows a user to add a recipe to their favorites
removeFromFavourites: allows a user to delete a recipe from his favorites
removeFromFavouritesAcceuil: allows a user to delete a recipe from his favorites from the homepage.
Additionally, media configuration is provided to allow storage of media files such as recipe images.

Work tools:
Django – BeautifulSoup – MySQL
editor:
Visual Studio Code
