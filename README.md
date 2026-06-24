# The Burn Center of the Caribbean — Website

Building Puerto Rico's first comprehensive pediatric burn center — and a financial safety net so that no family is bankrupted for saving their child's life.

> **Status:** Feasibility-stage initiative. Site copy is forward-looking; figures are illustrative; the CECFL-listed nonprofit status referenced on the site is pending.

## What's in here

- `index.html` — the complete single-page website. No build step — just open it in a browser.
- `docs/` — the donor-facing **Case for Support** and the **public Feasibility Brief summary** (each as PDF + source markdown).
- `images/` — photo slots for the hero and gallery. Drop your own licensed, consent-cleared photos here (see `images/README.md`); until then the site shows styled fallbacks.
- `scripts/` — generators that build the PDFs in `docs/` from a single content source (`python3 scripts/build_*.py`).

## View it

Open `index.html` in any browser.

## Deploy it

It's a static site — any static host works:

- **GitHub Pages:** push to `main`, then Settings → Pages → Source: "Deploy from a branch" → `main` / root.
- **Netlify / Vercel / Cloudflare Pages:** connect the repo or drag the folder in. No build command needed.

## Before you publish — please read

1. **The email form collects nothing yet.** In `index.html`, find `var SIGNUP_ENDPOINT = "";` near the bottom and paste your form endpoint (Formspree, Mailchimp, ConvertKit, Netlify Forms). Until then it shows a confirmation but does not store addresses.
2. **Replace placeholder contact details** — `hello@example.org` and the footer contact, plus `[name · email · phone]` in the Case for Support.
3. **Add real photos.** The hero and gallery use placeholder slots; drop your own licensed, consent-cleared images into `images/` before launch. Don't present stock or unrelated photos as actual patients.
4. **Only the public-safe Feasibility Brief is published.** The candid internal brief (risks, economics, donor strategy) is intentionally kept **out of this repo**. The "partners & funders" download links the public summary in `docs/Feasibility-Brief-Public.pdf`; share the full internal brief privately, on request.
5. **Charitable-status wording is feasibility-accurate.** Copy says the CECFL-listed nonprofit status is *being established / pending*. Don't change it to claim current registration until that status is actually granted.

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Burn Center of the Caribbean website"
git branch -M main
git remote add origin git@github.com:clinical-trials/BurnCenter.git
git push -u origin main
```

The `git@github.com:` URL uses SSH — you'll need an SSH key on your GitHub account. If you don't have one set up, either add one, or use the HTTPS remote instead:
`git remote add origin https://github.com/clinical-trials/BurnCenter.git`
