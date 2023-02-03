from fastapi import FastAPI
from datetime import datetime
from Routes import route

app = FastAPI()

app.include_router(route.router)

@app.get("/")
def root():
    return {"message": "Hi!"}

# @app.get("/posts")
# def get_posts():
#     return {"data": dataCards}

newDate = datetime.today().strftime('%d-%m-%Y %H:%I:%S')
# test formating date
print("statringDate:" + " " + newDate)
