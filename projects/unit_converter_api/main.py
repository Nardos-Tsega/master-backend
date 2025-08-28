from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import converter

app = FastAPI(title="Unit Converter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(converter.router)

@app.get("/", include_in_schema=False)
async def root():
    return {"message" : "Unit converter API - see /docs for documentation"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)