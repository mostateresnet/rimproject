Steps to get started:
1. Install `Python` if not yet installed.
2. Install `pip` if not yet installed.
3. Install `virtualenvwrapper` if not yet installed.
4. Create and launch a virtual environment. <br/>
<tab/>To launch a virtual environment for the project follow these steps:
    1. Open the project folder and run `mkvirtualenv rimproject` to create a new environment.
    2. Run `pip install -r requirements.txt` to install all the dependencies.
    3. In the future, you just run `workon rimproject` to switch to the environment we have just created.
5. Migrate using `python manage.py migrate` command.
6. Populate the RIM database using `python manage.py populate` command (for additional info refer to `./populationfolders/readme.md`).
7. Create a local super user to login into the RIM web interface using `python manage.py createsuperuser` command. Follow instructions in the CLI.
8. Run `python manage.py runserver` to run the  server.
9. Access the server by going to [localhost:8000](http://localhost:8000) using your browser.
