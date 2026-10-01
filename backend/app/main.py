from fastapi import FastAPI

app = FastAPI(
    title="NEXUS API",
    description="AI-powered university knowledge and learning system",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "NEXUS is online 🚀",
        "version": "0.1.0",
        "status": "operational"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }