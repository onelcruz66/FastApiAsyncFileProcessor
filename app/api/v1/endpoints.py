from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi import Depends
from fastapi import Path

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.file_service import SaveMetadataAndEnqueue
from app.utils.redis_cache import GetStatus

router = APIRouter()

# Defining async function allows other code to execute 
# while waiting for long running operations to complete.
@router.post("/upload")
async def UploadFile(
    file: UploadFile = File(...),
    description: str = Form(...),
    db: Session = Depends(det_db)
):
    # await is used within an async function
    # to pause execution until a specified task 
    # has completed. 
    fileId = await SaveMetadataAndEnqueue(file, description, db)
    return {"fileId": fileId}

@router.get("/status/{fileId}")
def GetFileStatus(fileId: int = Path(...)):
    status = GetStatus(fileId)
    return {"fileId": fileId, "status": status}

