from fastapi import APIRouter, HTTPException
from service.metric_service import  get_system_metrics

router = APIRouter()

@router.get("/metric")


def get_metrics():
    try:
      metric= get_system_metrics()
    except:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )
    return metric