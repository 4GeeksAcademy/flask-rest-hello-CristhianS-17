from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False)


class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)
    user_to_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)


class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50))
    url: Mapped[str] = mapped_column(String(250))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)


class Like(db.Model):
    __tablename__ = 'like'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)


if __name__ == "__main__":
    from eralchemy2 import render_er
    try:
        render_er(db.Model, 'diagram.png')
        print("¡Éxito! Diagrama actualizado con db.Model")
    except Exception as e:
        print(f"Error: {e}")
