from db import Base
from sqlalchemy.orm import Mapped, mapped_column # specify the types and attributes of columns in the model
from sqlalchemy import Text # specify the type of the content column
from datetime import datetime

"""
class Note:
    id str
    title str
    content str
    date_created datetime

"""

#the database model for notes
class Note(Base):
    __tablename__ = "notes"
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Note {self.title} at {self.date_created}>"