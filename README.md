Features

- Staff:
  - Upload notes
  - Delete notes
- Students:
  - Download notes

Technologies Used

- Frontend:
  - HTML
  - CSS
  - JavaScript
- Backend:
  - Python
  - Django
- Database:
  - MySQL
- Server:
  - Apache (via XAMPP)

 Setup Instructions

 Prerequisites

- Python 3.x
- Django
- MySQL
- XAMPP
- pip (Python package installer)

 Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/notes-sharing-application.git
   cd notes-sharing-application
   

2. Start XAMPP and set up the database:
   - Open XAMPP and start the Apache and MySQL services.
   - Open your web browser and go to http://localhost/phpmyadmin.
   - Create a new database named notes_sharing.

3. Configure the database in Django:
   - Open the settings.py file in the notes_sharing directory.
   - Update the DATABASES setting to use MySQL:
     python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'notes_sharing',
             'USER': 'your_mysql_username',
             'PASSWORD': 'your_mysql_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     

4. Run database migrations:

   python manage.py migrate
   

5. Start the development server:

   python manage.py runserver
   

 Usage

1. Access the application:
   Open a web browser and go to http://127.0.0.1:8000/.

2. Login as Staff:
   - Go to the admin panel at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.
   - Add staff users and assign them appropriate permissions to upload and delete notes.

3. Login as Student:
   - Students can register on the main site and log in to download notes.

4. Uploading Notes (Staff):
   - After logging in, staff can upload notes by navigating to the upload section.

5. Downloading Notes (Students):
   - Students can browse and download notes from the notes section.

 Project Structure


notes-sharing-application/
│
├── notes/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── notes_sharing/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md


 Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

 Contact

If you have any questions or suggestions, please feel free to contact me at [arulprakash8624@gmail.com].
