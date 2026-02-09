from fastapi import FastAPI

app = FastAPI(
    title="FinSphere Backend",
    description="Secure Finance + Social Insights API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "FinSphere API is running"}
