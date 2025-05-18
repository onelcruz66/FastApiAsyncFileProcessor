import os
import uuid 
import shutil

from app.models.file import FileMetaData
from app.tasks.worker import ProcessFile 
from app.utils.redis_cache import CacheStatus

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def SaveMetadataAndEnqueue(file, description, db):
    fileId = str(uuid.uuid4())
    filepath = os.path.join(UPLOAD_DIR, fileId + "_", file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    metadata = FileMetaData(filename=filepath, description=description)
    db.add(metadata)
    db.commit()
    db.refresh(metadata)

    CacheStatus(metadata.id, "queued")
    ProcessFile.delay(metadata.id, filepath)
    return metadata.id