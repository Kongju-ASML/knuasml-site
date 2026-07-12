import json
import re
import urllib.request
from pathlib import Path
from PIL import Image
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "google-sites"
OUT.mkdir(parents=True, exist_ok=True)
PAGES = {
    "research-facility": "https://sites.google.com/view/knuasml/research-facility",
    "activity": "https://sites.google.com/view/knuasml/activity",
    "award": "https://sites.google.com/view/knuasml/award",
    "home": "https://sites.google.com/view/knuasml",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read()

def clean_url(raw):
    u = raw.replace("\\u003d", "=").replace("\\u0026", "&")
    u = u.split('"')[0].split("'")[0].split(")")[0].split(";")[0]
    # Google Sites often wraps long image URLs across lines in the HTML.
    u = re.sub(r"\s+", "", u)
    u = re.sub(r"=w\d+.*$", "=w1600", u)
    if "=w" not in u:
        u += "=w1600"
    return u

manifest = []
seen = set()
for page, url in PAGES.items():
    html = fetch(url).decode("utf-8", "ignore")
    raw_urls = []
    for part in html.split("https://lh3.googleusercontent.com/")[1:]:
        raw_urls.append("https://lh3.googleusercontent.com/" + part)
    idx = 0
    for raw in raw_urls:
        img_url = clean_url(raw)
        if img_url in seen:
            continue
        seen.add(img_url)
        try:
            data = fetch(img_url)
            img = Image.open(BytesIO(data))
            w, h = img.size
            if len(data) < 8000 or w < 120 or h < 120:
                status = "skipped_small"
                file_rel = None
            else:
                idx += 1
                ext = "jpg" if img.format and img.format.upper() in {"JPEG", "JPG"} else (img.format or "jpg").lower()
                out = OUT / f"{page}-{idx:02d}.{ext}"
                out.write_bytes(data)
                status = "downloaded"
                file_rel = str(out.relative_to(ROOT)).replace('\\', '/')
            manifest.append({"page": page, "source_page": url, "url": img_url, "file": file_rel, "bytes": len(data), "width": w, "height": h, "status": status})
        except Exception as exc:
            manifest.append({"page": page, "source_page": url, "url": img_url, "file": None, "status": f"error:{exc}"})

(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
for item in manifest:
    if item["status"] == "downloaded":
        print(item["page"], item["file"], item["width"], item["height"], item["bytes"])
print("downloaded", sum(1 for x in manifest if x["status"] == "downloaded"), "total", len(manifest))
