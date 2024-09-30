# Feedback Application
This is a simple feedback collection web application built using Django. The app allows users to submit feedback, which is stored in the database and can be managed by an admin through the Django admin panel.


# Features
Submit feedback through a user-friendly form
Store feedback in a database
Manage feedback submissions via Django's admin interface
Form validation for user input
Responsive design using Bootstrap


# Technologies Used
Django: Python web framework used for building the backend
SQLite: Database used to store feedback
HTML/CSS: For the frontend design
Bootstrap: For responsive and modern design
JavaScript: For form handling (if applicable)
Setup
To get this project up and running locally on your machine, follow these steps:

1-Clone the repository:

```
git clone https://github.com/ARZF/Feedback.git
cd Feedback
```

2-Create a virtual environment:

```
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
```

3-Install dependencies:

```
pip install -r requirements.txt
```

4-Apply migrations:

```
python manage.py migrate
```
5-Run the development server:
```
python manage.py runserver
```

6-Access the application:
Open your browser and go to http://127.0.0.1:8000 to view the feedback app.

# Project Structure
```
Feedback/
├── feedback_app/         # Main application directory
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates for rendering
│   ├── models.py         # Feedback data models
│   ├── views.py          # Views to handle requests and responses
│   └── ...
├── static/               # Static files (CSS, JavaScript, images)
├── db.sqlite3            # SQLite database file
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```
# Future Improvements
Implement user authentication to allow logged-in users to submit feedback
Add pagination for feedback display
Implement feedback search functionality
Allow users to edit or delete their own feedback


# Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!
