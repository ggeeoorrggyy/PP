from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Post


def get(post_id: int) -> Post | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, Name_post FROM post WHERE id=(?)',
        args=(post_id,))

    return None if not res else Post(
        id=res[0],
        Name_post=res[1]
    )


def get_all() -> list[Post] | dict:
    post_list = dbmanager.execute_query(
        query="SELECT id, Name_post FROM post",
        fetchone=False)

    res = []

    if post_list:
        for post in post_list:
            res.append(Post(
                id=post[0],
                Name_post=post[1]
            ))

    return res


def delete(post_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM post WHERE id=(?) RETURNING id',
        args=(post_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_post: Post) -> Post | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO post (Name_post) VALUES (?, ?) RETURNING id",
        args=(new_post.Name_post))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(post_id: int, new_data: Post) -> Post | dict:
    res = dbmanager.execute_query(
        query="UPDATE post SET (Name_post) = (?, ?) WHERE id=(?)",
        args=(new_data.Name_post, post_id))

    if type(res) != dict:
        res = get(post_id)

    return res