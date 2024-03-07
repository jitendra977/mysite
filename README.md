# Django CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built with Django. It allows users to perform CRUD operations on recipes.

## Features

- Create new recipes with a name, description, and image.
- View a list of all recipes.
- Edit existing recipes.
- Delete recipes.

## Installation

1. Clone the repository to your local machine:
   ```
  git@github.com:jitendra977/mysite.git
   ```

2. Navigate to the project directory:
   ```
   cd django-crud-app
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations to create the database schema:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- To create a new recipe, click on the "Add Recipe" button and fill in the required details.
- To view all recipes, navigate to the homepage.
- To edit a recipe, click on the "Edit" button next to the recipe you want to edit.
- To delete a recipe, click on the "Delete" button next to the recipe you want to delete. A confirmation dialog will appear before deletion.

## Technologies Used

- Django
- HTML/CSS
- Bootstrap

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---
