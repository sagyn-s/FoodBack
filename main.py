import os

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from logmeal_response import logmeal_response

app = FastAPI()


@app.post("/upload-image")
async def upload_image(image: UploadFile = File(...)):
    try:
        response = await logmeal_response(image)
        return JSONResponse(content=response)

    except Exception as e:
        error_message = f"Error processing image: {str(e)}"
        print(error_message)
        return JSONResponse(status_code=500, content={"error": error_message})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
# python3 -m uvicorn main:app --host 0.0.0.0 --port 5000
# python3 -m uvicorn main:app --host 0.0.0.0 --port 5000
