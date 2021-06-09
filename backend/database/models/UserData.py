from sqlalchemy.orm import relationship

from database.connect import Base, create_session
from sqlalchemy import Column, Integer, String, ForeignKey


class UserData(Base):
    __tablename__ = "users_data"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    sex = Column(String)
    parent = relationship("User", back_populates="children")

    def __repr__(self):
        return f"<UserData(id:{self.id}, name:{self.name}, surname:{self.surname}, age:{self.age}, sex:{self.sex})>"

    def create(self):
        with create_session() as db:
            db.add(self)
            db.commit()
            db.refresh(self)
        return self
