"""Download every product photo from fleurinelle.com into site-photos/."""
import re, os, json, urllib.request, urllib.parse, html

BASE = "https://www.fleurinelle.com"
UA = {"User-Agent": "Mozilla/5.0 (fleurinelle-media sync)"}
OUT = "site-photos"
os.makedirs(OUT, exist_ok=True)

def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        return data if binary else data.decode("utf-8", "replace")

urls = set()
for sm in ("/sitemap.xml", "/en/sitemap.xml", "/sitemap-0.xml"):
    try:
        x = get(BASE + sm)
        urls |= set(re.findall(r"<loc>([^<]+)</loc>", x))
    except Exception as e:
        print("sitemap miss", sm, e)
for page in ("/", "/en", "/en/flowers", "/en/bouquets", "/en/shop"):
    try:
        h = get(BASE + page)
        urls |= {urllib.parse.urljoin(BASE, u) for u in re.findall(r'href="([^"]*/product/[^"#?]+)"', h)}
    except Exception as e:
        print("page miss", page, e)
products = sorted({u for u in urls if "/product/" in u and "/en/" in u} or {u for u in urls if "/product/" in u})
print(len(products), "product pages")

index = []
seen = set()
for u in products:
    try:
        h = get(u)
    except Exception as e:
        print("fail", u, e); continue
    title = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', h)
    imgs = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', h)
    imgs += [m for m in re.findall(r'(https?://[^"\'\s>]+?\.(?:jpe?g|png|webp))', h) if "logo" not in m.lower()]
    slug = u.rstrip("/").split("/")[-1]
    got = []
    for k, im in enumerate(dict.fromkeys(html.unescape(i) for i in imgs)):
        if im in seen or len(got) >= 4:
            continue
        seen.add(im)
        ext = os.path.splitext(urllib.parse.urlparse(im).path)[1] or ".jpg"
        fn = f"{OUT}/{slug}-{len(got)+1}{ext}"
        try:
            data = get(im, binary=True)
            if len(data) < 15000:
                continue
            open(fn, "wb").write(data); got.append({"file": fn, "src": im, "bytes": len(data)})
        except Exception as e:
            print("img fail", im, e)
    index.append({"url": u, "title": html.unescape(title.group(1)) if title else slug, "images": got})
    print(slug, len(got))
json.dump(index, open(f"{OUT}/index.json", "w"), indent=1, ensure_ascii=False)
