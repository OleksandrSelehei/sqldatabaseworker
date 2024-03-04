from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import declarative_base, relationship
from typing import TypeVar
from structures import User, Page, Right


# дикларотивный класс
Base = declarative_base()


# Интерфейс для моделей
T = TypeVar("T", bound=Base)


class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    access_rights = Column(Integer, ForeignKey("rights.id"))
    entry_time = Column(Date, nullable=False)

    def __str__(self):
        return f"UserName -> {self.username}"

    def update_date(self, struct: User):
        if struct.name is not None:
            self.name = struct.name
        if struct.username is not None:
            self.username = struct.username
        if struct.password is not None:
            self.password = struct.password
        if struct.access_rights is not None:
            self.access_rights = struct.access_rights
        if struct.entry_time is not None:
            self.entry_time = struct.entry_time
        return self


class Pages(Base):
    __tablename__ = "pages"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    href = Column(String(200), unique=True, nullable=False)
    img = Column(String(1000), nullable=False)
    draft = Column(Boolean, nullable=False, default=False)
    level = Column(Integer, ForeignKey("levels.level_range"))

    def __str__(self):
        return f"Page name and href -> ({self.name}) {self.href}"

    def update_date(self, struct: Page):
        if struct.name is not None:
            self.name = struct.name
        if struct.href is not None:
            self.href = struct.href
        if struct.img is not None:
            self.img = struct.img
        if struct.draft is not None:
            self.draft = struct.draft
        if struct.level is not None:
            self.level = struct.level
        return self


class Rights(Base):
    __tablename__ = "rights"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    level = Column(Integer, ForeignKey("levels.level_range"))

    def __str__(self):
        return f"Rights name -> {self.name}"

    def update_date(self, struct: Right):
        if struct.name is not None:
            self.name = struct.name
        if struct.description is not None:
            self.description = struct.description
        if struct.level is not None:
            self.level = struct.level
        return self


class Levels(Base):
    __tablename__ = "levels"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    level_range = Column(Integer, unique=True, nullable=False)

    def __str__(self):
        return f"level range -> {self.level_range}"


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    user_name = Column(String(50), ForeignKey("user.username"), nullable=False)
    action = Column(String(200), nullable=False)
    date = Column(Date, nullable=False)
    rights = Column(Integer, ForeignKey("rights.id"), nullable=False)

    def __str__(self):
        return f"Log action -> {self.action}"
