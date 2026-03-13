from fastapi import APIRouter, HTTPException

from service.aws_service import get_bucket, get_ec2_instances
router = APIRouter()

@router.get("/")

def get_all_metrics():
    try:
        buckets = get_bucket()
        instances = get_ec2_instances()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"internal server error: {str(e)}")
    return {
        "buckets": buckets,
        "instances": instances
    }

@router.get("/s3")

def get_metrics():
    
    try:
      buckets=get_bucket()
     # ec2_instances = get_ec2_instances()

    except:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )
    return {
       "buckets":buckets,
       #"ec2_instances": ec2_instances

    }
@router.get("/ec2")
def get_metrics():
    
    try:
     # buckets=get_bucket()
      ec2_instances = get_ec2_instances()

    except:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )
    return {
       #"buckets":buckets,
       "ec2_instances": ec2_instances

    }