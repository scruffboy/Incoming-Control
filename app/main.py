from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main_info():
    return {"status": "OK", "message": "Server is running"}
