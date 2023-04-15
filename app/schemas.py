from pydantic import BaseModel
from datetime import datetime

# Post extends BaseModel, schema of a post + validation that data is what we want 
class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True 

# use for create and update post 
class PostCreate(PostBase):
    pass 

class Post(BaseModel):
    title : str
    content : str
    published : bool = True 
