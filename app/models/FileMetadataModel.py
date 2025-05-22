from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

# Base is the class all db models inherits from. 
from app.database.base import Base

class FileMetaData(Base):
    __tablename__ = "file_metadata"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    description = Column(String)

    # func.now() is used to insert the current timestamp into created_at field.
    created_at = Column(DateTime(timezone=True), server_default=func.now())