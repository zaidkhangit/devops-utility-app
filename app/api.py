from fastapi import FastAPI
from routers import metrics, aws
app = FastAPI(
    title="Internal DevOps Utility API", description="this is an Internal API Utility App for Monitoring metrics,AWS usag, logs",version="1.1.0", doc_url="/docs")
app.include_router(metrics.router)
app.include_router(aws.router, prefix ="/aws")
