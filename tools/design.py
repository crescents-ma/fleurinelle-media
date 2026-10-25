"""Fleurinelle social design system. Template-inspired layouts at 1080x1350."""
import math, html

W, H = 1080, 1350
BRAND = "/home/claude/instagram-fleurinelle/brand"
IMG = "/home/claude/fleurinelle-media/products"
REV = "/home/claude/fleurinelle-30d/img"
AMIRI = "/home/claude/fleurinelle-30d/work/Amiri-Bold.woff2"

CREAM = "#FCF0E4"; CREAM2 = "#F6E4D6"; GREEN = "#0C3018"; GREEN2 = "#1E4A2C"
BLUSH = "#E8A097"; BLUSH2 = "#F7DCD3"; GOLD = "#C29A52"; SOFT = "#3d5a45"


def star(cx, cy, R, r, n=8, rot=0):
    pts = []
    for k in range(2 * n):
        a = math.pi * k / n + rot
        rad = R if k % 2 == 0 else r
        pts.append(f"{cx + rad * math.sin(a):.1f},{cy - rad * math.cos(a):.1f}")
    return " ".join(pts)


def zellige_uri(tile=110, bg=CREAM2, c1=GREEN, c2=BLUSH, c3=GOLD):
    t = tile; h = t / 2
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{t}' height='{t}' viewBox='0 0 {t} {t}'>"
        f"<rect width='{t}' height='{t}' fill='{bg}'/>"
        f"<polygon points='{star(h, h, h*0.92, h*0.70, rot=math.pi/8)}' fill='{c1}'/>"
        f"<polygon points='{star(h, h, h*0.62, h*0.47, rot=math.pi/8)}' fill='{c2}'/>"
        f"<polygon points='{star(h, h, h*0.26, h*0.2, rot=math.pi/8)}' fill='{c3}'/>"
    )
    for cx, cy in ((0, 0), (t, 0), (0, t), (t, t)):
        svg += f"<polygon points='{star(cx, cy, h*0.42, h*0.18, n=4)}' fill='{c3}'/>"
    svg += "</svg>"
    from urllib.parse import quote
    return "url(\"data:image/svg+xml," + quote(svg) + "\")"


def arch_path(w, h, inset_ratio=0.075):
    """Moroccan horseshoe (keyhole) arch: the round top is wider than the
    straight sides below it."""
    r = w / 2
    ins = w * inset_ratio
    y0 = r + math.sqrt(r * r - (r - ins) ** 2)
    return (f"M{ins:.1f},{h} L{ins:.1f},{y0:.1f} "
            f"A{r:.1f},{r:.1f} 0 1 1 {w-ins:.1f},{y0:.1f} L{w-ins:.1f},{h} Z")


def arch(w, h, inner, fill="#FFFFFF", outline=GOLD, gap=26, extra="", tile=64):
    """Keyhole window: gold line, a band of zellige, then the photo inside."""
    W2, H2 = w + 2 * gap, h + gap
    return f"""
<div class="arch" style="width:{W2+12}px;height:{H2+6}px;{extra}">
  <svg width="{W2+12}" height="{H2+6}" style="position:absolute;left:0;top:0">
    <path d="{arch_path(W2+12, H2+6)}" fill="none" stroke="{outline}" stroke-width="3"/>
  </svg>
  <div style="position:absolute;left:6px;top:6px;width:{W2}px;height:{H2}px;
       clip-path:path('{arch_path(W2, H2)}');background:{zellige_uri(tile).replace(chr(34), chr(39))};background-size:{tile}px"></div>
  <div style="position:absolute;left:{gap+6}px;top:{gap+6}px;width:{w}px;height:{h}px;
       clip-path:path('{arch_path(w, h)}');background:{fill};
       display:flex;align-items:flex-end;justify-content:center">{inner}</div>
  <svg width="{w}" height="{h}" style="position:absolute;left:{gap+6}px;top:{gap+6}px">
    <path d="{arch_path(w, h)}" fill="none" stroke="{outline}" stroke-width="4"/>
  </svg>
</div>"""


def texture_uri():
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='540' height='540'>"
           "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.012 0.02' numOctaves='4' seed='7'/>"
           "<feColorMatrix values='0 0 0 0 0.62  0 0 0 0 0.42  0 0 0 0 0.28  0 0 0 0.11 0'/></filter>"
           "<rect width='540' height='540' filter='url(#n)'/>"
           "<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' seed='3'/>"
           "<feColorMatrix values='0 0 0 0 0.4  0 0 0 0 0.3  0 0 0 0 0.2  0 0 0 0.05 0'/></filter>"
           "<rect width='540' height='540' filter='url(#g)'/></svg>")
    from urllib.parse import quote
    return "url(\"data:image/svg+xml," + quote(svg) + "\")"


def star_uri(c=GOLD):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='40' height='40'>"
           f"<polygon points='{star(20, 20, 19, 11, rot=math.pi/8)}' fill='{c}'/>"
           f"<circle cx='20' cy='20' r='4.5' fill='{CREAM}'/></svg>")
    from urllib.parse import quote
    return "url(\"data:image/svg+xml," + quote(svg) + "\")"


def photo(name, maxh, maxw=900, pad=0, blend=True):
    style = f"max-height:{maxh}px;max-width:{maxw}px;margin-bottom:{pad}px"
    if blend:
        style += ";mix-blend-mode:multiply"
    return f'<img src="file://{IMG}/{name}.jpg" style="{style}">'


CSS = f"""
@font-face{{font-family:Cormorant;src:url(file://{BRAND}/fonts/CormorantGaramond-SemiBold.ttf)}}
@font-face{{font-family:Inter;src:url(file://{BRAND}/fonts/Inter-Medium.ttf)}}
@font-face{{font-family:Amiri;src:url(file://{AMIRI})}}
*{{margin:0;padding:0;box-sizing:border-box;font-variant-numeric:lining-nums !important;font-feature-settings:"lnum" 1 !important}}
body{{background:#ccc}}
section{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:{texture_uri()},{CREAM};background-size:540px;color:{GREEN};
  display:flex;flex-direction:column;align-items:center;text-align:center}}
.arch{{position:relative;flex:none}}
.eyebrow{{font:30px Inter;letter-spacing:9px;color:{GOLD};text-transform:uppercase;display:inline-flex;align-items:center;gap:22px}}
.eyebrow::before,.eyebrow::after{{content:'';width:30px;height:30px;background:{star_uri()};background-size:30px;flex:none}}
.eyebrow:empty{{display:none}}
.h-xl{{font:600 96px/1.02 Cormorant}}
.h-l{{font:600 82px/1.05 Cormorant}}
.h-m{{font:600 68px/1.08 Cormorant}}
.caps{{font:600 64px/1.08 Cormorant;letter-spacing:4px;text-transform:uppercase}}
.sub-caps{{font:30px Inter;letter-spacing:6px;text-transform:uppercase;color:{SOFT}}}
.body{{font:38px/1.45 Inter;color:{SOFT}}}
.small{{font:28px/1.4 Inter;color:{SOFT}}}
.ar{{font:700 64px/1.5 Amiri;direction:rtl}}
.band{{position:absolute;left:0;right:0;height:110px;background:{zellige_uri()};background-size:110px;border-top:4px solid {GOLD};border-bottom:4px solid {GOLD}}}
.mark{{position:absolute;width:118px;height:118px;border-radius:50%;background:{CREAM};
  display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px {GOLD}}}
.mark img{{width:88px}}
.foot{{position:absolute;bottom:52px;font:28px Inter;color:{SOFT};letter-spacing:1px}}
.num{{position:absolute;bottom:52px;right:80px;font:28px Inter;color:{GOLD};letter-spacing:2px}}
.url{{position:absolute;bottom:52px;left:80px;font:28px Inter;color:{SOFT}}}
.rule{{width:90px;height:3px;background:{GOLD};margin:36px auto 0}}
.code{{display:inline-block;border:4px dashed {GOLD};border-radius:18px;padding:14px 56px;
  font:600 96px Cormorant;letter-spacing:8px;color:{CREAM};font-feature-settings:"lnum" 1}}
.key{{display:inline-block;border:3px solid {GREEN};border-radius:16px;padding:10px 46px;
  font:600 92px Cormorant;letter-spacing:5px}}
"""

LOGO_G = f"file://{BRAND}/logos/logo-horizontal-green.png"
LOGO_C = f"file://{BRAND}/logos/logo-horizontal-cream.png"
MARK = f"file://{BRAND}/logos/logo-mark.png"


def esc(s):
    return html.escape(s).replace("\n", "<br>")


def mark_badge(right=60, bottom=46):
    return f'<div class="mark" style="right:{right}px;bottom:{bottom}px"><img src="{MARK}"></div>'


# ---------- layouts ----------

def riad(s):
    """Template 1: eyebrow + headline at top, product in a Moroccan arch,
    a line under it, zellige band and the logo mark bottom right."""
    head = s.get("head", "")
    hcls = "h-l" if len(head) > 34 else "h-xl"
    ar = f'<div class="ar" style="margin-top:6px">{esc(s["ar"])}</div>' if s.get("ar") else ""
    ah = s.get("arch_h", 720 if not ar else 600)
    inner = photo(s["photo"], ah - 60, 560, pad=30) if s.get("photo") else ""
    return f"""
<section style="justify-content:center;padding-bottom:130px">
  <div class="eyebrow">{esc(s.get('eyebrow','Fleurinelle'))}</div>
  <div class="{hcls}" style="margin:22px 90px 0">{esc(head)}</div>
  {ar}
  <div style="margin-top:36px">{arch(600, ah, inner)}</div>
  <div class="body" style="margin:30px 120px 0">{esc(s.get('line',''))}</div>
  <div class="band" style="bottom:0"></div>
  {mark_badge()}
</section>"""


def frame(s):
    """Template 2: blush border, wordmark top, caps headline, product in arch."""
    inner = photo(s["photo"], 700, 600, pad=26) if s.get("photo") else ""
    return f"""
<section style="background:{BLUSH};padding:34px">
  <div style="width:100%;height:100%;background:{CREAM};position:relative;display:flex;flex-direction:column;align-items:center;text-align:center">
    <img src="{LOGO_G}" style="height:96px;margin-top:62px">
    <div class="caps" style="margin:34px 70px 0">{esc(s['head'])}</div>
    <div class="sub-caps" style="margin:18px 70px 0">{esc(s.get('sub',''))}</div>
    <div style="position:absolute;bottom:0">{arch(680, 790, inner)}</div>
  </div>
</section>"""


def promo(s):
    """Green offer card: logo, big number, product in a cream arch, code, terms."""
    inner = photo(s["photo"], 420, 340, pad=0)
    return f"""
<section style="background:{GREEN};color:{CREAM}">
  <div style="position:absolute;inset:30px;border:2px solid {GOLD};border-radius:6px"></div>
  <div style="position:absolute;inset:42px;border:1px solid {GOLD};opacity:.6;border-radius:4px"></div>
  <img src="{LOGO_C}" style="height:84px;margin-top:84px">
  <div style="display:flex;align-items:center;gap:46px;margin-top:40px">
    {arch(340, 450, inner, outline=GOLD, gap=22)}
    <div style="text-align:left">
      <div class="eyebrow" style="color:{GOLD}">{esc(s['eyebrow'])}</div>
      <div style="font:600 {s.get('bigsize',220)}px/0.9 Cormorant;margin-top:10px">{esc(s['big'])}</div>
      <div style="font:600 54px/1.1 Cormorant;margin-top:10px;max-width:470px">{esc(s['head'])}</div>
    </div>
  </div>
  <div style="font:30px Inter;letter-spacing:6px;color:{GOLD};margin-top:48px">{esc(s['code_label'])}</div>
  <div class="code" style="margin-top:16px">FIRST10</div>
  <div style="font:27px/1.5 Inter;color:{CREAM};opacity:.85;margin:30px 110px 0">{esc(s['terms'])}</div>
</section>"""


def text(s):
    """Text-led post (funny, tips, engagement). Zellige band top and bottom."""
    pic = ""
    if s.get("photo"):
        pic = f'<div style="margin-top:34px">{photo(s["photo"], s.get("ph", 420), 520)}</div>'
    hcls = s.get("hcls", "h-l")
    quote = f'<div class="{hcls}" style="margin:24px 100px 0">{esc(s["head"])}</div>'
    ar = f'<div class="ar" style="margin-top:10px">{esc(s["ar"])}</div>' if s.get("ar") else ""
    second = f'<div class="body" style="margin:28px 120px 0">{esc(s["line"])}</div>' if s.get("line") else ""
    after = f'<div class="h-m" style="margin:20px 100px 0">{esc(s["after"])}</div>' if s.get("after") else ""
    return f"""
<section>
  <div class="band" style="top:0;height:70px"></div>
  <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:90px 0 120px">
    <div class="eyebrow">{esc(s.get('eyebrow',''))}</div>
    {quote}{ar}{second}{pic}{after}
  </div>
  <div class="band" style="bottom:0;height:70px"></div>
  {mark_badge(bottom=12)}
</section>"""


def versus(s):
    left, right = s["pair"]
    def card(p):
        return f"""<div style="display:flex;flex-direction:column;align-items:center">
          {arch(400, 520, photo(p[0], 460, 380, pad=18))}
          <div class="h-m" style="margin-top:20px">{esc(p[1])}</div></div>"""
    return f"""
<section>
  <div class="eyebrow" style="margin-top:90px">{esc(s['eyebrow'])}</div>
  <div class="h-l" style="margin:20px 80px 0">{esc(s['head'])}</div>
  <div style="display:flex;gap:30px;margin-top:50px;align-items:flex-end">{card(left)}
    <div style="font:600 64px Cormorant;color:{GOLD};margin-bottom:250px">or</div>{card(right)}</div>
  <div class="small" style="margin-top:26px">{esc(s.get('line',''))}</div>
  <div class="band" style="bottom:0;height:70px"></div>
  {mark_badge(bottom=12)}
</section>"""


def review(s):
    return f"""
<section>
  <div class="eyebrow" style="margin-top:80px">{esc(s.get('eyebrow','Kind words'))}</div>
  <div class="h-m" style="margin:20px 110px 0;font-style:italic">{esc(s['head'])}</div>
  <div style="margin-top:34px;border:3px solid {GOLD};border-radius:34px;overflow:hidden;line-height:0">
    <img src="file://{REV}/{s['img']}.png" style="height:{s.get('ih',800)}px"></div>
  <div class="band" style="bottom:0;height:70px"></div>
  {mark_badge(bottom=12)}
</section>"""


def ranked(s):
    rows = "".join(
        f"""<div style="display:flex;align-items:baseline;gap:30px;padding:24px 0;border-bottom:2px solid {BLUSH2};text-align:left">
          <div style="font:600 52px Cormorant;width:250px;flex:none;color:{GREEN}">{esc(a)}</div>
          <div style="font:36px/1.35 Inter;color:{SOFT}">{esc(b)}</div></div>"""
        for a, b in s["rows"])
    return f"""
<section>
  <div class="band" style="top:0;height:70px"></div>
  <div class="eyebrow" style="margin-top:130px">{esc(s['eyebrow'])}</div>
  <div class="h-l" style="margin:20px 80px 0">{esc(s['head'])}</div>
  <div style="width:880px;margin-top:40px">{rows}</div>
  <div class="band" style="bottom:0;height:70px"></div>
  {mark_badge(bottom=12)}
</section>"""


def slide(s, i, n):
    """Carousel slide."""
    parts = [f'<img src="{MARK}" style="position:absolute;top:70px;height:70px">']
    body = []
    if s.get("photo"):
        ah = s.get("arch_h", 560)
        body.append(f'<div style="margin-bottom:40px">{arch(s.get("arch_w", 520), ah, photo(s["photo"], ah-50, 480, pad=18))}</div>')
    if s.get("eyebrow"):
        body.append(f'<div class="eyebrow" style="margin-bottom:26px">{esc(s["eyebrow"])}</div>')
    if s.get("head"):
        cls = s.get("hcls", "h-l")
        body.append(f'<div class="{cls}" style="margin:0 110px">{esc(s["head"])}</div>')
    if s.get("ar"):
        body.append(f'<div class="ar" style="margin-top:14px">{esc(s["ar"])}</div>')
    if s.get("line"):
        body.append(f'<div class="body" style="margin:28px 130px 0">{esc(s["line"])}</div>')
    if s.get("cities"):
        cs = "".join(f"<span>{c}</span>" for c in s["cities"])
        body.append(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px 130px;font:42px Inter;margin-top:34px">{cs}</div>')
    if s.get("list"):
        li = "".join(f'<li style="margin:0 0 24px;padding-left:76px;position:relative"><b style="position:absolute;left:0;font:600 50px/1 Cormorant;color:{GOLD}">{k+1}</b>{esc(t)}</li>' for k, t in enumerate(s["list"]))
        body.append(f'<ol style="list-style:none;text-align:left;font:38px/1.35 Inter;margin-top:34px">{li}</ol>')
    if s.get("key"):
        body.append(f'<div class="body" style="margin-top:30px">{esc(s.get("key_pre","Comment"))}</div><div class="key" style="margin:14px 0 26px">{esc(s["key"])}</div><div class="body" style="margin:0 130px">{esc(s.get("key_post",""))}</div>')
    if s.get("rule", not s.get("photo") and not s.get("list") and not s.get("cities") and not s.get("key")):
        body.append('<div class="rule"></div>')
    frame_line = f'<div style="position:absolute;inset:28px;border:2px solid {GOLD};opacity:.55;pointer-events:none"></div><div style="position:absolute;inset:38px;border:1px solid {GOLD};opacity:.35;pointer-events:none"></div>'
    if not s.get("photo"):
        frame_line += (f'<svg width="820" height="820" style="position:absolute;top:265px;left:130px;opacity:.10">'
                       f'<polygon points="{star(410, 410, 405, 300, rot=math.pi/8)}" fill="none" stroke="{GOLD}" stroke-width="10"/>'
                       f'<polygon points="{star(410, 410, 300, 222, rot=math.pi/8)}" fill="none" stroke="{GREEN}" stroke-width="6"/></svg>'
                       f'<div class="band" style="top:0;height:46px;background-size:46px"></div>')
    return f"""
<section style="justify-content:center">
  {frame_line}{''.join(parts)}
  <div style="display:flex;flex-direction:column;align-items:center;margin-top:30px">{''.join(body)}</div>
  <div class="url">fleurinelle.com</div><div class="num">{i}/{n}</div>
</section>"""


LAYOUTS = {"riad": riad, "frame": frame, "promo": promo, "text": text,
           "versus": versus, "review": review, "ranked": ranked}


def render_post(post):
    sl = post["slides"]
    out = []
    for i, s in enumerate(sl, 1):
        if s.get("layout") == "lifestyle":
            out.append(lifestyle(s, i if len(sl) > 1 else None, len(sl)))
        elif s.get("layout") == "slide" or (len(sl) > 1 and "layout" not in s):
            out.append(slide(s, i, len(sl)))
        else:
            out.append(LAYOUTS[s["layout"]](s))
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(out)}</body></html>"


GEN = "/home/claude/fleurinelle-media/gen"


def lifestyle(s, i=None, n=None):
    """Template-style full-bleed photo with people. Headline over a soft cream
    fade at the top, zellige band and logo mark at the bottom."""
    pos = s.get("pos", "center 60%")
    head = s.get("head", "")
    hcls = s.get("hcls", "h-l" if len(head) > 30 else "h-xl")
    ar = f'<div class="ar" style="margin-top:4px;font-size:58px">{esc(s["ar"])}</div>' if s.get("ar") else ""
    line = (f'<div style="position:absolute;bottom:{150 if i is None else 120}px;left:50%;transform:translateX(-50%);'
            f'background:rgba(252,240,228,.93);border:2px solid {GOLD};border-radius:999px;padding:16px 44px;'
            f'font:34px/1.3 Inter;color:{GREEN};white-space:nowrap">{esc(s["line"])}</div>') if s.get("line") else ""
    logo = f'<img src="{LOGO_G}" style="height:74px;margin-bottom:18px">' if s.get("logo") else ""
    foot = (f'<div class="url" style="color:{CREAM};text-shadow:0 1px 6px rgba(0,0,0,.5)">fleurinelle.com</div>'
            f'<div class="num" style="color:{CREAM};text-shadow:0 1px 6px rgba(0,0,0,.5)">{i}/{n}</div>') if i else ""
    band = "" if i else f'<div class="band" style="bottom:0;height:74px"></div>{mark_badge(bottom=14)}'
    return f"""
<section style="background:#000">
  <img src="file://{GEN}/{s['bg']}.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
  <div style="position:absolute;left:0;right:0;top:0;height:{s.get('fade',560)}px;
       background:linear-gradient(to bottom,rgba(252,240,228,.97) 0%,rgba(252,240,228,.9) 45%,rgba(252,240,228,0) 100%)"></div>
  <div style="position:relative;margin-top:70px;display:flex;flex-direction:column;align-items:center">
    {logo}<div class="eyebrow">{esc(s.get('eyebrow',''))}</div>
    <div class="{hcls}" style="margin:16px 80px 0">{esc(head)}</div>{ar}
  </div>
  {line}{band}{foot}
</section>"""


LAYOUTS["lifestyle"] = lifestyle
