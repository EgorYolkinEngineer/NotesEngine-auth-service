from fastapi import FastAPI
from routes.user import user_router
from routes.jwt import jwt_router
import uvicorn

app = FastAPI()
app.include_router(jwt_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)