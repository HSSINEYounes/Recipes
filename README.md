# Recipe Scraping Web Application
This is a Django web application that allows users to search and view recipes scraped from a website using Beautiful Soup. Users can also add comments, rate recipes, and add recipes to their favorites.
# Installation
### 1. Clone the repository to your local machine.
### 2. Navigate to the project directory and create a virtual environment:
    python -m venv venv
### 3. Activate the virtual environment:
    source venv/bin/activate
### 4. Install the required dependencies:
    pip install -r requirements.txt
### 5. Create the database tables:
    python manage.py migrate
### 6. Start the development server:
python manage.py runserver
### 7. Navigate to http://localhost:8000/Recette/index in your web browser to use the application.
# Usage
  The home page displays a list of scraped and stored recipes with a **search bar** where users can enter keywords to search for recipes. The search will return a list of recipes that match the keywords. Users can click on a recipe to view its details, including its ingredients and instructions.

  To add a **comment**, **rate** a recipe, or add a recipe to favorites, the user must be logged in. Users can create an account by clicking the **"Register"** button on the navigation bar.

  Once logged in, users can add a comment by entering their text in the comment box and clicking the "**Submit**" button. Users can rate a recipe by clicking on the number of stars they want to give and clicking the "**Rate**" button.

To add a recipe to **favorites**, users can click the "**the heart icon**" in the top left of the recipe card. Users can view their favorites by clicking the "**Profile**" button on the navigation bar.

# Credits
This web application was created by:
- **HSSINE Younes** 
- **KHARDALI Ikram**
- **EL MANSOURI Mohamed Achraf**

The recipe data was scraped using Beautiful Soup from the website https://www.jamieoliver.com
