from sqlalchemy.orm import relationship

from database.connect import Base, create_session
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    password = Column(String)
    login = Column(String)
    email = Column(String)
    children = relationship("UserData", back_populates="parent")
    children2 = relationship("UserTrash", back_populates="parent")

    def __repr__(self):
        return f"<User(id:{self.id}, login:{self.login}, email:{self.email}, password:{self.password})>"

    def create(self):
        with create_session() as db:
            db.add(self)
            db.commit()
            db.refresh(self)
        return self
