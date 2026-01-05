print(">>> ASTROBOT API MAIN.PY LOADED <<<")
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import HoroscopeRequest, HoroscopeResponse
from .storage import get_text

app = FastAPI(
    title="AstroBot API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS — iOS / Web / Telegram
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Типы контента, которые считаются premium
PREMIUM_TYPES = {"love", "career"}


@app.get("/")
def root():
    return {
        "service": "AstroBot API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/horoscope", response_model=HoroscopeResponse)
def horoscope(req: HoroscopeRequest):
    """
    Основной endpoint гороскопа
    """

    # --- Premium gate ---
    if req.type in PREMIUM_TYPES and req.user_type == "free":
        return HoroscopeResponse(
            sign=req.sign,
            type=req.type,
            lang=req.lang,
            text="Этот раздел доступен в Premium.",
            is_premium_content=True
        )

    # --- Получаем текст ---
    text = get_text(
        sign=req.sign,
        content_type=req.type,
        lang=req.lang
    )

    if not text:
        raise HTTPException(
            status_code=404,
            detail="Text not found for given parameters"
        )

    return HoroscopeResponse(
        sign=req.sign,
        type=req.type,
        lang=req.lang,
        text=text,
        is_premium_content=req.type in PREMIUM_TYPES
    )
@app.get("/")
def root():
    return {
        "service": "AstroBot API",
        "status": "running"
    }
