Steps to get started:
    1. Install Python if not yet installed.
    2. Install `pip` if not yet installed.
    3. Install `pipenv` if not yet installed.
    4. Create and launch a virtual environment
        To launch a virtual environment for the project follow these steps:
        4.1 Open the project folder and run `pipenv install` to create a new environment and install all dependencies.
        4.2 Run `pipenv shell` to switch to the environment we have just created.
    5. Migrate using `python manage.py migrate` command.
    6. Populate the RIM database using `python manage.py populate` command (for additional info refer to `./populationfolders/readme.md`).
    7. Create a local super user to login into the RIM web interface using `python manage.py createsuperuser` command. Follow instructions in the CLI.
    8. Run `python manage.py runserver` to run the  server.
    9. Access the server by going to [localhost:8000](http://localhost:8000) using your browser.


Useful info and commands:
1.  Use `pipenv install <package-name>` to install a package
    and `pipenv uninstall <package-name>` to uninstall.

    **`WARNING`**: do not use `pip install <package-name>` to install packages as `pip` bypasses the `pipenv` dependency manager and therefore a package installed this way will not be added to the `Pipfile.lock`.

2. `pipenv install` creates a new environment AND installs all dependencies listed in `Pipfile.lock`.
3. `Pipfile.lock` gets updated only when hashes of the dependencies don't match (e.g. when a dependency gets updated or when you add a new dependency).
4. `pipenv --rm` lets you remove ALL environments you have created before.


 