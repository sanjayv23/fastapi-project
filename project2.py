from fastapi import FastAPI, Path,HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

posts = {
    1: {
        'title': "Title 1",
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque a nunc vulputate, maximus nibh ac, sagittis est. Mauris porta laoreet dignissim. Ut id consectetur neque. Nullam dolor velit, pellentesque ut erat et, sollicitudin convallis massa. Sed eleifend finibus purus, sed dapibus orci porttitor id. Nulla vel porta est. Fusce nec rutrum magna. Phasellus lacinia orci a tincidunt sollicitudin. Etiam ut augue ac eros sollicitudin varius. Morbi dui enim, suscipit id nunc eget, tempus mollis dui. Ut aliquet nulla non massa ultrices, sit amet porta metus pulvinar. Nullam commodo non erat vehicula aliquet. Fusce et ipsum lectus.,",
        'author': "Sanjay",
        
    },
    2: {
        'title': "title2",
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque a nunc vulputate, maximus nibh ac, sagittis est. Mauris porta laoreet dignissim. Ut id consectetur neque. Nullam dolor velit, pellentesque ut erat et, sollicitudin convallis massa. Sed eleifend finibus purus, sed dapibus orci porttitor id. Nulla vel porta est. Fusce nec rutrum magna. Phasellus lacinia orci a tincidunt sollicitudin. Etiam ut augue ac eros sollicitudin varius. Morbi dui enim, suscipit id nunc eget, tempus mollis dui. Ut aliquet nulla non massa ultrices, sit amet porta metus pulvinar. Nullam commodo non erat vehicula aliquet. Fusce et ipsum lectus.,",
        'author': "ruban",
        
    }
}


class blogpost(BaseModel):
    title: str
    content: str
    author: str

class Updatepost(BaseModel):
    
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

# GET METHOD BY post_ID
@app.get("/get-post/{post_id}")
def get_post(post_id: int = Path(description="The ID of the post you want to view", gt=0, le=len(posts))):
    if  post_id in posts:
        return posts[post_id]
    raise HTTPException(status_code=404, detail="Post not found")
    


# POST METHOD 
@app.post("/create-post/{post_id}")
def create_post(post_id : int, createpost : blogpost):
    if post_id in posts:
         raise HTTPException(status_code=409, detail="Post already exists")

    posts[post_id] = createpost
    return posts[post_id]

# PUT METHOD 
@app.put("/update-post/{post_id}")
def update_post(post_id: int, Upost: Updatepost):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")

    if Upost.title != None:
        posts[post_id]['title']  = Upost.title

    if Upost.content != None:
        posts[post_id]['content'] = Upost.content

    if Upost.author != None:
        posts[post_id]['author'] = Upost.author

    return posts[post_id]

# # DELETE METHOD 
@app.delete("/delete-post/{post_id}")
def delete_post(post_id: int):
    if post_id  in posts:
        del posts[post_id]
        
        return {"Message":"Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")

    