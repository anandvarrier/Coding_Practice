from fastapi import FastAPI

app = FastAPI()  # This creates an FastAPI instance

"""
This is a python decorator that specifies to FastAPI that the function below it is in charge of request handling.
This is a decorator that specifies the route. This creates a GET method on the site’s route.
The result is then returned by the wrapped function.
"""


@app.get("/")
async def root():
    return {"Greeting": "Bonjour Anand!"}
