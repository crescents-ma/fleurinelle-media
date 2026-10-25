"""Build the 30-day review board (self-contained HTML, thumbnails inlined)."""
import sys, os, io, base64, datetime, html, json
sys.path.insert(0, os.path.dirname(__file__))
from posts import POSTS
from PIL import Image

MEDIA = "/home/claude/fleurinelle-media/posts"
START = datetime.date(2026, 10, 27)
SCHED = json.load(open(os.path.join(os.path.dirname(__file__), "schedule.json")))
STATUS = json.load(open(os.path.join(os.path.dirname(__file__), "status.json"))) if os.path.exists(
    os.path.join(os.path.dirname(__file__), "status.json")) else {}

def thumb(path):
    im = Image.open(path).convert("RGB")
    im.thumbnail((360, 450))
    b = io.BytesIO(); im.save(b, "JPEG", quality=72, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

KIND_GROUP = {"Promo": "Promo", "Offer": "Offer", "B2B": "Promo", "Brand": "Promo",
              "Educational": "Educational", "Guide": "Educational", "Cities": "Educational",
              "Tip": "Tips", "Tips": "Tips", "Funny": "Funny", "Engagement": "Engagement",
              "Testimonial": "Testimonial", "Story": "Story", "Occasion": "Story"}

cards = []
for n, p in sorted(enumerate(POSTS, 1), key=lambda t: SCHED[str(t[0])]["utc"]):
    folder = f"{MEDIA}/{n:02d}-{(START + datetime.timedelta(days=n - 1)).isoformat()}"
    d = datetime.date.fromisoformat(SCHED[str(n)]["date"])
    when = SCHED[str(n)]["paris"][-5:]
    imgs = sorted(f for f in os.listdir(folder) if f.endswith(".jpg"))
    strip = "".join(f'<img src="{thumb(os.path.join(folder, f))}" alt="Slide {i+1} of post {n}" loading="lazy">'
                    for i, f in enumerate(imgs))
    fmt = f"Carousel · {len(imgs)} slides" if len(imgs) > 1 else "Single image"
    group = KIND_GROUP.get(p["kind"], p["kind"])
    st = STATUS.get(str(n), "pending")
    st_label = {"scheduled": f"Scheduled · {when} Paris", "pending": f"Add slides in Ocoya · {when} Paris"}.get(st, st)
    cap = p["caption"].strip() + "\n\n" + p["tags"]
    flags = []
    if p.get("aigc"): flags.append("AI lifestyle photo")
    if p.get("commercial"): flags.append("Promotional label on TikTok")
    flag_html = "".join(f'<span class="flag">{html.escape(f)}</span>' for f in flags)
    cards.append(f"""
<article class="card" data-group="{group}" id="day{n}">
  <header class="card-head">
    <div class="date"><span class="dow">{d.strftime('%a')}</span><span class="dnum">{d.day}</span><span class="mon">{d.strftime('%b')}</span></div>
    <div class="meta">
      <div class="kicker"><span class="kind k-{group.lower()}">{html.escape(p['kind'])}</span><span class="lang">{p['lang']}</span><span class="fmt">{fmt}</span></div>
      <h2>{html.escape(p['title'])}</h2>
      <div class="status s-{st}">{st_label}</div>
    </div>
    <span class="dayno">Day {n}</span>
  </header>
  <div class="strip">{strip}</div>
  <details>
    <summary>Caption and hashtags</summary>
    <pre class="cap" id="cap{n}">{html.escape(cap)}</pre>
    <button type="button" class="copy" data-target="cap{n}">Copy caption</button>
  </details>
  <div class="flags">{flag_html}</div>
</article>""")

groups = ["All", "Promo", "Offer", "Educational", "Tips", "Funny", "Engagement", "Testimonial", "Story"]
chips = "".join(f'<button type="button" class="chip{" on" if g=="All" else ""}" data-g="{g}">{g}</button>' for g in groups)
done = sum(1 for n in range(1, 31) if STATUS.get(str(n)) == "scheduled")

page = f"""<title>Fleurinelle Content Calendar</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap">
<style>
/* Layout: a riad-ledger calendar. One card per day, the real visuals as a swipeable strip. */
:root {{
  --bg: #FCF0E4; --surface: #FFF8F1; --fg: #0C3018; --muted: #4f6b57; --line: #EBD9C7;
  --gold: #A9803C; --blush: #E8A097; --chip: #F4E2D2; --ok: #2E6B45; --wait: #9A6A1E;
  --display: "Cormorant Garamond", "Iowan Old Style", Georgia, serif;
  --body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0E1F14; --surface: #15291C; --fg: #F6E9DA; --muted: #B9C9BC; --line: #2A4231;
  --gold: #D8B272; --blush: #E8A097; --chip: #1F3627; --ok: #7FC79A; --wait: #E2B45F; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #0E1F14; --surface: #15291C; --fg: #F6E9DA; --muted: #B9C9BC; --line: #2A4231;
  --gold: #D8B272; --blush: #E8A097; --chip: #1F3627; --ok: #7FC79A; --wait: #E2B45F; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 15px; line-height: 1.5;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding-block: 28px 64px; }}
.top {{ display: flex; flex-wrap: wrap; align-items: end; justify-content: space-between; gap: 16px 32px;
  border-bottom: 2px solid var(--gold); padding-bottom: 18px; }}
.eyebrow {{ font-size: 12px; letter-spacing: .22em; text-transform: uppercase; color: var(--gold); font-weight: 600; }}
h1 {{ font-family: var(--display); font-weight: 600; font-size: clamp(34px, 5vw, 52px); line-height: 1.02; margin: 6px 0 0; text-wrap: balance; }}
.sub {{ color: var(--muted); margin: 8px 0 0; max-width: 62ch; }}
.facts {{ display: flex; gap: 22px; flex-wrap: wrap; font-variant-numeric: tabular-nums; }}
.fact b {{ display: block; font-family: var(--display); font-size: 30px; line-height: 1; }}
.fact span {{ font-size: 12px; color: var(--muted); letter-spacing: .06em; text-transform: uppercase; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 18px 0 22px; }}
.chip {{ font: 500 13px var(--body); color: var(--fg); background: var(--chip); border: 1px solid var(--line);
  border-radius: 999px; padding: 6px 14px; cursor: pointer; }}
.chip.on {{ background: var(--fg); color: var(--bg); border-color: var(--fg); }}
.chip:focus-visible, .copy:focus-visible, summary:focus-visible {{ outline: 2px solid var(--gold); outline-offset: 2px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 18px; }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 16px; min-width: 0;
  display: flex; flex-direction: column; gap: 12px; }}
.card-head {{ display: grid; grid-template-columns: auto 1fr auto; gap: 14px; align-items: start; }}
.date {{ display: grid; justify-items: center; width: 54px; border: 1px solid var(--gold); border-radius: 27px 27px 6px 6px;
  padding: 6px 0 5px; line-height: 1.05; }}
.dow, .mon {{ font-size: 10px; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }}
.dnum {{ font-family: var(--display); font-size: 26px; font-weight: 600; font-variant-numeric: tabular-nums; }}
.meta {{ min-width: 0; }}
.kicker {{ display: flex; flex-wrap: wrap; gap: 6px 10px; font-size: 12px; color: var(--muted); align-items: center; }}
.kind {{ font-weight: 600; letter-spacing: .04em; color: var(--fg); padding: 1px 8px; border-radius: 999px; background: var(--chip); }}
.k-offer {{ background: var(--blush); color: #2a1410; }}
.lang {{ font-weight: 600; color: var(--gold); }}
h2 {{ font-family: var(--display); font-weight: 600; font-size: 23px; line-height: 1.12; margin: 4px 0 2px; text-wrap: balance; }}
.status {{ font-size: 12px; font-weight: 500; }}
.status::before {{ content: ""; display: inline-block; width: 7px; height: 7px; border-radius: 50%; margin-right: 6px; vertical-align: 1px; background: currentColor; }}
.s-scheduled {{ color: var(--ok); }} .s-pending {{ color: var(--wait); }}
.dayno {{ font-size: 11px; color: var(--muted); letter-spacing: .1em; text-transform: uppercase; white-space: nowrap; }}
.strip {{ display: flex; gap: 8px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 4px; }}
.strip img {{ flex: none; width: 78%; max-width: 280px; aspect-ratio: 4 / 5; object-fit: cover; border-radius: 8px;
  scroll-snap-align: start; border: 1px solid var(--line); }}
.strip img:only-child {{ width: 100%; max-width: 100%; }}
details {{ border-top: 1px solid var(--line); padding-top: 10px; }}
summary {{ cursor: pointer; font-weight: 500; font-size: 14px; }}
.cap {{ white-space: pre-wrap; font: 14px/1.55 var(--body); margin: 10px 0; color: var(--fg); }}
.copy {{ font: 500 13px var(--body); background: var(--fg); color: var(--bg); border: 0; border-radius: 8px; padding: 7px 14px; cursor: pointer; }}
.flags {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.flags:empty {{ display: none; }}
.flag {{ font-size: 11px; color: var(--muted); border: 1px dashed var(--line); border-radius: 6px; padding: 2px 8px; }}
.notes {{ margin-top: 36px; border-top: 1px solid var(--line); padding-top: 18px; color: var(--muted); max-width: 70ch; font-size: 14px; }}
.notes h3 {{ font-family: var(--display); color: var(--fg); font-size: 22px; margin: 0 0 6px; }}
.notes code {{ font-size: 13px; }}
@media (max-width: 420px) {{ .grid {{ grid-template-columns: 1fr; }} }}
</style>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Instagram · Facebook · LinkedIn · TikTok</div>
      <h1>Fleurinelle, 25 Oct to 23 Nov</h1>
      <p class="sub">One post a day for the diaspora sending flowers home. Green posts are scheduled in Ocoya and publish automatically at the time shown. Amber posts are carousels that still need their slides added in Ocoya. Times are Paris time.</p>
    </div>
    <div class="facts">
      <div class="fact"><b>30</b><span>posts</span></div>
      <div class="fact"><b>{sum(1 for p in POSTS if len(p['slides'])>1)}</b><span>carousels</span></div>
      <div class="fact"><b>{done}/30</b><span>scheduled</span></div>
    </div>
  </div>
  <div class="chips" role="group" aria-label="Filter by content type">{chips}</div>
  <div class="grid">{''.join(cards)}</div>
  <section class="notes">
    <h3>Before you publish</h3>
    <p>FIRST10 (posts 2, 16, 29) must be live at checkout: 10% off, orders above 50€, first 100 orders. English posts ask people to comment CITY, French posts VILLE, so have a reply ready for both. TikTok posts are public. Images live in the public repo <code>crescents-ma/fleurinelle-media</code>.</p>
  </section>
</div>
<script>
document.querySelectorAll('.chip').forEach(function (c) {{
  c.addEventListener('click', function () {{
    document.querySelectorAll('.chip').forEach(function (x) {{ x.classList.toggle('on', x === c); }});
    var g = c.dataset.g;
    document.querySelectorAll('.card').forEach(function (card) {{ card.hidden = !(g === 'All' || card.dataset.group === g); }});
  }});
}});
document.querySelectorAll('.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{
    var el = document.getElementById(b.dataset.target), t = el.textContent;
    var done = function () {{ b.textContent = 'Copied'; setTimeout(function () {{ b.textContent = 'Copy caption'; }}, 1600); }};
    var fallback = function () {{ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected, press copy'; }};
    if (navigator.clipboard) {{ navigator.clipboard.writeText(t).then(done, fallback); }} else {{ fallback(); }}
  }});
}});
</script>
"""
open(os.path.join(os.path.dirname(__file__), "board.html"), "w").write(page)
print("board.html", round(len(page) / 1e6, 2), "MB")
