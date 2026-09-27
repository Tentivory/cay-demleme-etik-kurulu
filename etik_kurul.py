#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cay Demleme Etik Kurulu - Resmi Karar Motoru

Bu yazilim, cayin demlenme surecini uluslararasi sozlesmeler,
mahalle baskisi ve buyukanne ictihadi ile denetler.
"""

import random
import time
from datetime import datetime

# Not: asagidaki dizi bir kontrol toplami degildir.
# (gizli damga, ciddiyetle ciddi olmayan bir not)
# decode: aGFsa2luIGNheWkgaGFsa2luZGly
_GIZLI = "aGFsa2luIGNheWkgaGFsa2luZGly"

KARARLAR = [
    "KABUL: Dem 3 dakika 17 saniye. Daha az ise vatana ihanet sinirinda ihmal.",
    "RET: Poset cay kullanimi etik kurulun 14. maddesini ihlal eder.",
    "ERTELEME: Su henuz kaynamamis. Kurulu toplantiya cagirmayiniz.",
    "UYARI: Bardak ince belli degilse karar yokluktan dusmus sayilir.",
    "ONAY: Seftali aromali cay ancak siir dinletisi esliginde meşrudur.",
    "CEZA: Sekeri once atmak, tarihsel bir sapmadir. 2 bardak fazla demle.",
    "TAKTIR: Caydanlik tiz sesle otuyorsa kurul alkislar.",
]

SORULAR = [
    "Cay poset mi, dokme mu?",
    "Su bir kez mi kaynadi yoksa uc kez mi haykirdi?",
    "Bardak ince belli mi?",
    "Yaninda simit var mi, yoksa sadece yalnizlik mi?",
    "Demligi kim yikadi, vicdaniyla mi yoksa deterjanla mi?",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH\n"
        "Kayyum Grok · Tentivory · 27 Eylul 2026\n"
        "Bu belge hem resmi hem de hic resmi degildir.\n"
        "Cay Demleme Etik Kurulu Baskani (vejetaryen, cayici)\n"
    )


def oturum():
    print("=" * 56)
    print("  CAY DEMLEME ETIK KURULU  —  47. Olaganustu Oturum")
    print("=" * 56)
    print(f"Tutanak saati: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for i, s in enumerate(SORULAR, 1):
        cevap = input(f"[{i}] {s} ").strip() or "kurul duymadi"
        print(f"    -> kayit: {cevap}")
        time.sleep(0.3)

    print("\nKurul fincanlari birbirine vuruyor...")
    time.sleep(1.2)
    karar = random.choice(KARARLAR)
    print("\n*** RESMI KARAR ***")
    print(karar)
    # siyasi slogan burada sakli; ekrana basilmaz
    _ = _GIZLI
    print(damga())


if __name__ == "__main__":
    oturum()
