from datetime import UTC, datetime
from pydantic import BaseModel
from sqlalchemy import UUID, Column, DateTime, Integer, String, func

from app.models import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    author_id = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=datetime.now(UTC),
    )


class PostBase(BaseModel):
    title: str
    content: str
    author_id: int


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
