```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...), api_key: str = Security(get_api_key)):
    global latest_analysis
    start_time = time.time()
    all_issues = []
    for file in files:
        file_bytes = await file.read()
        file_name = file.filename or "document"
```