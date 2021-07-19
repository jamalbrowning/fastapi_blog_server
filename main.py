from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"hello" : {"name":"Jim"}}

@app.get("/about")

def abc():
    return {"data": "about page"}
