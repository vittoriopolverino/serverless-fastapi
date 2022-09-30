from fastapi import FastAPI
from app.api.v1.api import router as api_router
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(api_router, prefix="/api/v1")
# Mangum is an adapter for running ASGI applications in AWS Lambda to handle
# Function URL, API Gateway, ALB and Lambda@Edge events.
handler = Mangum(app)
