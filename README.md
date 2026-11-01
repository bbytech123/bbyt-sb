# BBY Technologies — Next Sandbox (local completed copy)

A separate, completed draft based on the current BBY Technologies sandbox. This is a buildless static website: open `dist/index.html`, or preview this checkout with the supported Sites preview workflow. No package installation, database, secrets, third-party scripts, or build step are required.

## Hosting status

**Not hosted.** The native Sites remix operation was unavailable on 2026-10-31. In accordance with the remix workflow, creation and publication were not attempted. This package is not a new hosted sandbox and has no live URL or access grants. `.openai/hosting.json` intentionally has no `project_id`.

The original sandbox, live websites, DNS, and GitHub were not changed.

## What is complete

- Approved homepage hero artwork, typography, header gradient/rim, dark backdrop, and exact brand fonts retained.
- The two existing client logos remain immediately beneath the hero.
- Three title-only audience cards now lead to completed Restaurants & Venues, SMB, and Residential pages.
- All original service routes retained and rewritten into concise, connected pages.
- Complete How It Works, About, and Contact pages; working native FAQ disclosures.
- Consistent accessible desktop/mobile navigation, full-card links, footer navigation, keyboard focus and skip link.
- Contact links use `braxton@bbytechnologies.com` and `737-333-5763`. Restaurant links use `https://bbyrestaurants.com/`.
- No fake form, invented testimonials, certifications, case studies, pricing, or guaranteed outcomes.
- Always-dark styling, reduced-motion support, local fonts, constrained static CSP, and no analytics or remote scripts.
- Unused heavy PNG illustrations excluded from this separate release; unchanged originals remain in the original sandbox checkout.

## Review and validation

Run:

```sh
python3 qa/validate_static.py
node --check dist/script.js
```

See `QA.md` and the JSON reports in `qa/` for verified results. Browser screenshots are retained locally as internal QA only and are excluded from the deliverable ZIP.

`build.py` is an optional standard-library Python content generator. Its approved home reference is bundled in `reference/dist/index.html`. The editable website is already present in `dist/`; generation is not needed for preview or future deployment.

## Supported continuation when native remix becomes available

1. Use native `remix_site` with source `appgprj_6ae1608b74c08191986eb826f311d1c0`, a new title, and a new slug (suggestion: `bby-tech-next`). Do not modify or re-register the original.
2. Open that returned destination with its own source credential and supported Sites source helper. Confirm the destination is owner-private.
3. Preserve the returned destination identity and access settings. Overlay this package's `dist/` into the destination checkout; retain any destination manifest identity rather than copying an original project ID.
4. Run checks, then package and push using the supported Sites source helper. Save and deploy only the newly returned owner-private destination.
5. Verify its terminal deployment result and returned URL. Do not change audience or invite anyone.

This local template archive cannot be passed directly to deployment until the supported destination-creation workflow establishes its new identity.
