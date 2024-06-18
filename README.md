# IEEE NITK Blogs

## Table of Contents-

- [Description](#Description)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)

## Description-

This is a guide to install and setup the blog app on your local computer. 

## Prerequisites-

- Python (This project was built on v3.12)
- Django v5.0
- pip
- virtualenv (not mandatory)

## Installation-

1. First fork and clone the following repository to your local machine

   https://github.com/UtsavBhamra/envision_blog

2. Creating and activating a virtual env, Run the following commands

    ```bash
    py -m venv myworld
    cd myworld\Scripts\activate # (for windows)
    ```
  

3. Install the markdown library-

    ```bash
    pip install django
    pip install markdown
    ```
  
4. Run all the migrations-

    ```
    py manage.py createmigrations blog
    py manage.py migrate
    ```

5. Run the server-

    ```
    py manage.py runserver
    ```
    

6. The blog app should be acccessible at https://localhost:8000






