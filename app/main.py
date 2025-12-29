from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import HoroscopeRequest, HoroscopeResponse
from .storage import get_text

app = FastAPI(
    title="AstroBot API",
    version="1.0.0"
)

# Разрешаем запросы от iOS / Web / Telegram
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PREMIUM_TYPES = {"love", "career"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/horoscope", response_model=HoroscopeResponse)
def horoscope(req: HoroscopeRequest):
    # Premium gate
    if req.type in PREMIUM_TYPES and req.user_type == "free":
        return HoroscopeResponse(
            sign=req.sign,
            type=req.type,
            lang=req.lang,
            text="Этот раздел доступен в Premium.",
            is_premium_content=True
        )

    text = get_text(req.sign, req.type, req.lang)
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

