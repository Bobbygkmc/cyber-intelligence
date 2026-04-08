from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.database import engine, Base
from src.api import listings, calculator, faq

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BizBridge", description="Connect business buyers and sellers in Pennsylvania")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")

app.include_router(listings.router)
app.include_router(calculator.router)
app.include_router(faq.router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
