from fastapi import APIRouter, HTTPException

from service.aws_service import get_bucket
router = APIRouter()

@router.get("/")
@router.get("/s3")
def get_metrics():
    try:
      buckets=get_bucket()
    except:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )
    return {
       "buckets":buckets
    }