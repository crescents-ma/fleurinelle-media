# fleurinelle-media

Public image host for Fleurinelle social posts (Ocoya pulls media from raw URLs here).

- `products/` brand-ready product photos from fleurinelle.com, background normalised to white.
  `products/index.json` lists name, product page, raw URL and whether it is usable.
  Little Prince and Serenity show another brand on the box: do not use until reshot.
- `site-photos/` untouched originals as downloaded from the site.
- `posts/NN-YYYY-MM-DD/` rendered post images, one folder per day.
- `tools/fetch_site_photos.py` + the "Fetch site photos" workflow re-sync photos from the site
  (run it from the Actions tab whenever new bouquets go live).

Raw URL pattern: `https://raw.githubusercontent.com/crescents-ma/fleurinelle-media/main/<path>`
