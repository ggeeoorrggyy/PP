from fastapi import FastAPI
from src.server.router import routers
from fastapi.responses import RedirectResponse
import uvicorn
import setting

app = FastAPI(title='EfimtsovAPI',
              version='0.88.0 ')

[app.include_router(router) for router in routers]


@app.router.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("start_server:app", reload=True, host=setting.HOST, port=setting.PORT)