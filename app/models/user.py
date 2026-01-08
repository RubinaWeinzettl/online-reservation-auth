from sqlalchemy import Boolean, Column, DateTime, String, func

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    email_norm = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
