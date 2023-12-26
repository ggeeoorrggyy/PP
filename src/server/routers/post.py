import fastapi
from src.server.resolvers import post
from src.server.sql_base.models import Post

router = fastapi.APIRouter(prefix='/post', tags=['Post'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{post_id}', response_model=Post | dict)
def get(post_id: int) -> Post | dict:
    res = post.get(post_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Post] | dict)
def get_all() -> list[Post] | dict:
    return post.get_all()


@router.delete('/delete/{post_id}', response_model=str | dict)
def remove(post_id: int) -> str | dict:
    res = post.delete(post_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Post | dict)
def create(new_post: Post) -> Post | dict:
    return post.create(new_post)


@router.put("/update/{post_id}", response_model=Post | dict)
def update(post_id: int, new_data: Post):
    return post.update(post_id=post_id,
                        new_data=new_data)