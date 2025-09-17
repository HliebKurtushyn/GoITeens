from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first_page():
    return "Welcome to My Website!"

@app.get("/second_page")
def second_page():
    return "This website is built using the FastApi framework."