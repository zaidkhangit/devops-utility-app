from fastapi import FastAPI
from routers import metrics,aws
app = FastAPI(
    title ="Internal DevOps Utility API",
    description= "this is an Internal API Utility App for Monitoring metrics,AWS usag,logs",
    version="1.1.0",
    doc_url="/docs"
)
@app.get("/")
def hello():
    """" this is hello api for testing"""
    return {"message":"hello,this is teat"}
app.include_router(metrics.router)
app.include_router(aws.router, prefix = "/aws")
