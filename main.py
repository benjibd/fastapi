from fastapi import FastAPI
from fastapi import Body,Response,status,HTTPException
from pydantic import BaseModel
from random import randrange

from pydantic.types import OptionalInt
from starlette.status import HTTP_201_CREATED


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: OptionalInt

my_posts =[{"title":"Will the trotro","content":"Strie off","id":1},{"title":"Unique icon","content":"Shawa say ","id":2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
       

@app.get("/")
def root():
    return {"message':'hello wworld"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int, response:Response):
    post = find_post(id)
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Resource with id: {id} not found")
    print(id)
    return {"data": post}


@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(1,90000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def get_post(id: int, response:Response):
    post = find_post(id)
    
    print(id)
    return {"data": post}