# From a Python shell or add to a `setup.py` script
from app.database.base import Base
from app.database.session import engine
Base.metadata.create_all(bind=engine)
