from sqlalchemy.orm import relationship

from database.connect import Base, create_session
from sqlalchemy import Column, Integer, String, ForeignKey


class UserTrash(Base):
    __tablename__ = "user_to_trash"

    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_trash = Column(Integer, ForeignKey('trash.id'), primary_key=True)
    child = relationship("Trash", back_populates="parent")
    parent = relationship("User", back_populates="children2")

    def __repr__(self):
        return f"<UserTrash(id_user:{self.id}, id_trash:{self.description})>"

    def create(self):
        with create_session() as db:
            db.add(self)
            db.commit()
            db.refresh(self)
        return self
