import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from design import render_post
from posts import POSTS
from playwright.sync_api import sync_playwright

OUT = "/home/claude/fleurinelle-media/posts"
START = datetime.date(2026, 10, 27)
only = {int(a) for a in sys.argv[1:]}

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for n, p in enumerate(POSTS, 1):
        if only and n not in only:
            continue
        d = START + datetime.timedelta(days=n - 1)
        folder = f"{OUT}/{n:02d}-{d.isoformat()}"
        os.makedirs(folder, exist_ok=True)
        for f in os.listdir(folder):
            os.remove(os.path.join(folder, f))
        hp = f"/home/claude/fleurinelle-30d/work/post-{n:02d}.html"
        open(hp, "w").write(render_post(p))
        pg.goto("file://" + hp)
        pg.wait_for_timeout(500)
        for i, s in enumerate(pg.query_selector_all("section"), 1):
            s.screenshot(path=f"{folder}/{i:02d}.jpg", type="jpeg", quality=92)
        print(n, d, len(p["slides"]), "slides")
    b.close()
