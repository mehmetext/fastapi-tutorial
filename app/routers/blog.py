from fastapi import APIRouter, Query
from app.controllers.blog import BlogController, OrderBy
from app.models.post import PostRead

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/", response_model=list[PostRead])
async def get_all_posts(
    q: str | None = Query(None, min_length=3),
    author_id: int | None = None,
    order_by: OrderBy | None = None,
):
    return BlogController.get_all_posts(q, author_id, order_by)


@router.get("/{id}", response_model=PostRead)
async def get_post(id: int):
    return BlogController.get_post(id)
