import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, true
from sqlalchemy.orm import relationship

# user import
# import base from dbsetup
from ..db_setup import Base
from .mixins import Timestamp


# set up role-model
class Role(enum.Enum):
    teacher = 1
    student = 2


# set up usermodel
class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), nullable=False)
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)


# set up user profile model
class Profile(Timestamp, Base):

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # creates a relationship btwn user and Profile
    owner = relationship("User", back_populates="profile")
