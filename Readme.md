
# Online Shop


This is Django based management system for online shop. It has the following functionalities:

   * #### Add, edit and delete an item  
   * #### Search for an item  
   * #### Show all items of a user  
   * #### Contact sellers regarding an item  
   * #### Show all conversations a user has regarding different items
   * #### Register and login for users after email confirmation

The system is build using **Django 4**, **Python 3.10**, **Tailwind** and **HTML 5**. Users can activate their account after email confirmation.  

![image](https://github.com/YordanovaT/OnlineShop/assets/109622871/7db52bbc-7209-4faa-b4a7-7bc1ee2bdc78)

## Table of contents
*  [Installation](#Installation)  
*  [Running the application](#Running-the-application)  
*  [View the application](#View-the-application)

### [Installation](#Installation) 

**1. Create virtual environment**  
*From the **root** directory run:*

      python -m venv venv  

**2. Activate the environment**  
*On MacOS:* 

    source venv/bin/activate
*On Windows :*  

    venv\scripts\activate

**3. Install required dependencies**  
*From the **root** directory run:* 

    pip install -r requirements.txt

**4. Run migrations**  
*From the **root** directory run:*  

    python manage.py makemigrations

*Then run:*  

    python manage.py migrate

**5. Create Django admin user in order to have access to the Django Admin Panel:**  
*From the **root** directory run:*  

    python manage.py createsuperuser

*When prompted, enter an email, username and password.*  

### [Running the application](#Running-the-application)  

*From the **root** directory run:*  

    python manage.py runserver

### [View the application](#View-the-application)  

*Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)*  
  
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)