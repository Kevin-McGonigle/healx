# Healx Full-Stack Technical Assessment - Kevin McGonigle

## Installation
1. Clone this repo.
2. Change to the `front-end` directory and run `npm install` (latest version of Node recommended).
3. Change to the `back-end` director, create and activate a new virtual environment, and run 
`pip install -r requirements.txt` (Python 3.10 required).
4. Then, run `python scripts/create_db.py` to create and populate the database.

## Running
1. Change to the `back-end` directory and, with the virtual environment activated, run `python server/main.py` _or_
`uvicorn server.main:app --reload`.
2. Change to the `front-end` directory and run `npm start`.
3. You should be good to go! Head over to http://localhost:3000 to view the user interface. Or, if you want to take a
look at the API more closely, head to http://localhost:8000/docs to view the Swagger docs.