from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

router = FastAPI()

static = StaticFiles(directory=Path(__file__).resolve().parent)
router.mount(path="/goosebit", name="static", app=static)
