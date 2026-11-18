# Empowered Health website

Source for www.empoweredhealthtn.com, a static site served by GitHub Pages from the `docs/` folder on `main`.

- Page content lives in `src/*.html` (each file starts with `title:`, `description:` and `path:` lines).
- Shared header, footer and page shell live in `build.py`.
- Styles and images live in `docs/assets/`.

To change the site, edit `src/` or `build.py`, run `python3 build.py`, and commit the updated `docs/` folder.
