from typing import Optional
from .texts_seed import TEXTS


def get_text(sign: str, htype: str, lang: str) -> Optional[str]:
    return (
        TEXTS
        .get(sign, {})
        .get(htype, {})
        .get(lang)
    )

