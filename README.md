# flask_for_testing

## Venv

In the root of the project, run `. venv/bin/activate` (UNIX) or `venv\Scripts\activate` (Win).


## Set env vars

In the root of the project, set env vars to the following values: (UNIX: use `export`; Win: use `set`)  
- `FLASK_APP=flaskr`
- `FLASK_ENV=development`


## Initiate DB

In the root of the project, run `flask init-db`.


## Run

Run the app using `flask run`.


## Test

In the root of the project, run `python -m pytest tests/`.  
  
Depending on your OS, you may have to use `python3` command instead.