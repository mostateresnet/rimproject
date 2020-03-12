To launch a virtual environment for the project follow these steps:

1. Install `pip` if not yet installed.
2. Install `pipenv` if not yet installed.
3. Open the project folder and run `pipenv install` to create a new environment.
4. Run `pipenv shell` to switch to the environment we have just created.
5. Run `python manage.py runserver` to run the  server.
6. Access the server by going to `[localhost:8000](localhost:8000)` using your browser.

Useful info and commands:
1.  Use `pipenv install <package-name>` to install a package
    and `pipenv uninstall <package-name>` to uninstall.

    **`WARNING`**: do not use `pip install <package-name>` to install packages as `pip` bypasses the `pipenv` dependency manager and therefore a package installed this way will not be added to the `Pipfile.lock`.

2. `pipenv install` creates a new environment AND installs all dependencies listed in `Pipfile.lock`.
3. `Pipfile.lock` gets updated only when hashes of the dependencies don't match (e.g. when a dependency gets updated or when you add a new dependency).
4. `pipenv --rm` lets you remove ALL environments you have created before.
