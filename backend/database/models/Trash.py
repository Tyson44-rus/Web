from sqlalchemy.orm import relationship

from database.connect import Base, create_session
from sqlalchemy import Column, Integer, String


class Trash(Base):
    __tablename__ = "trash"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    parent = relationship("UserTrash", back_populates="child")

    def __repr__(self):
        return f"<Trash(id:{self.id}, description:{self.description})>"

    def create(self):
        with create_session() as db:
            db.add(self)
            db.commit()
            db.refresh(self)
        return self
