import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets" / "people"
ASSET_DIR.mkdir(parents=True, exist_ok=True)

PAGES = {
    "recent": (
        "https://sites.google.com/view/knuasml/members/students/recent",
        {
            "Yun Jong Jung": "jung-yoonjong",
            "Kang Jin Lee": "lee-kangjin",
            "Seung Hwan Shin": "shin-seunghwan",
            "Soon Won Choi": "choi-soonwon",
            "Seong Jin Im": "im-seongjin",
            "Min A Heo": "heo-mina",
            "Sang Min Park": "park-sangmin",
            "Min Cheol Kwon": "kwon-mincheol",
            "Yoon Ji Shin": "shin-yoonji",
            "Dong Hyun Kim": "kim-donghyun",
            "Jeong Hyeon Im": "im-jeonghyeon",
            "Seon Yeong Kwak": "kwak-seonyeong",
        },
    ),
    "alumni": (
        "https://sites.google.com/view/knuasml/members/students/alumni",
        {
            "Jong Tae Kim": "kim-jongtae",
            "Ho Seop Song": "song-hoseop",
            "Byung Chan Cho": "cho-byungchan",
            "Jeong Eun Kim": "kim-jeongeun",
            "Syed Muhammad Hamza Ifthikar": "hamza-ifthikar",
            "Kang Hyun Park": "park-kanghyun",
        },
    ),
}

def clean_url(url: str) -> str:
    url = url.replace("\\u003d", "=").replace("\\u0026", "&")
    url = url.split('"')[0].split("'")[0].split(")")[0]
    url = re.sub(r"=w\d+.*$", "=w600", url)
    if "=w" not in url:
        url += "=w600"
    return url

def extract_url(text: str, name: str):
    idx = text.find(name)
    if idx < 0:
        return None
    win = text[max(0, idx - 6000):idx + 500]
    parts = win.split("https://lh3.googleusercontent.com/")
    if len(parts) <= 1:
        return None
    return clean_url("https://lh3.googleusercontent.com/" + parts[-1])

manifest = {}
for page_name, (url, names) in PAGES.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    text = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    for label, slug in names.items():
        image_url = extract_url(text, label)
        if not image_url:
            manifest[slug] = {"name": label, "url": None, "file": None, "status": "no image detected"}
            continue
        out = ASSET_DIR / f"{slug}.jpg"
        try:
            req_img = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req_img, timeout=30).read()
            out.write_bytes(data)
            manifest[slug] = {"name": label, "url": image_url, "file": str(out.relative_to(ROOT)).replace('\\', '/'), "bytes": len(data), "status": "downloaded"}
        except Exception as exc:
            manifest[slug] = {"name": label, "url": image_url, "file": None, "status": f"download failed: {exc}"}

(ROOT / "assets" / "people" / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
for slug, item in manifest.items():
    print(slug, item["status"], item.get("bytes", ""))
