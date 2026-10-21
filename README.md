# Steps to create a Django Project

1. Create a folder for the new project
2. Open VS Code and a terminal at that project (or any other IDE)
3. Create the virtualenvironment  
    - Mac: python3 -m venv venv (Last parameter is optional, not mandatory to call it 'venv')
    - Windows: python -m venv venv  
4. Activate the venv  
    - Mac: source venv/bin/activate
    - Windows: .\venv\Scripts\activate  
5. Install the required dependencies  
    - Both OS: pip install django (pip3 if you're on a MAC)  
6. Create the django project (One time only command)
    - Both OS: django-admin startproject NAME_FOLDER .
    Expectation is: NAME_FOLDER folder, venv folder and manage.py
7. Update settings.py to recognize **static** and **templates** folders
    Expectation is: templates and static folders are created  
    7.1. Inside of static you can create three subfolders called: js, images and css
8. Adding misc files: .gitignore, README.md
9. To generate the requirements.txt file:
    - Both OS: pip freeze > requirements.txt (pip3 if you're on a MAC)

