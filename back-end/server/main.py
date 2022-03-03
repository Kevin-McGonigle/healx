import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.middleware.database import AsyncDatabaseSessionMiddleware
from server.routes import reading_list_routes, search_routes

app = FastAPI()

# Middleware
app.add_middleware(AsyncDatabaseSessionMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(reading_list_routes.router)
app.include_router(search_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
