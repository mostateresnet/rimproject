Steps to get started:
1. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) if not yet installed.
2. Migrate using `uv run manage.py migrate` command.
3. Populate the RIM database using `uv run manage.py populate` command (for additional info refer to `./populationfolders/readme.md`).
4. Create a local super user to login into the RIM web interface using `uv run manage.py createsuperuser` command. Follow instructions in the CLI.
5. Run `uv run manage.py runserver` to run the local dev server.
6. Access the server by going to [localhost:8000](http://localhost:8000) using your browser.
