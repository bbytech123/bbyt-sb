# Verification — 2026-10-31

## Passed

- Static validation: 19 complete HTML pages; 645 local file/anchor references; no missing files, duplicate IDs, broken anchors, forms, or inline event handlers.
- JavaScript syntax: `node --check dist/script.js`.
- Genuine cloud-browser QA using CUA against the supported managed Sites preview.
- All 19 pages rendered at a desktop browser viewport of 1180px, with no horizontal overflow, missing images, or non-dark body backgrounds.
- All 19 pages rendered at each of three real iframe viewport widths (375px, 320px, 768px): 57 responsive checks. Scrollbars reduced content widths to 360px, 305px, and 753px. No horizontal overflow, missing images, or mismatched page headings.
- 17 actual link-navigation journeys: all six Services dropdown destinations, all three top-level pages, and all eight detailed service pages.
- Homepage What We Do anchor landed correctly beneath the sticky header.
- Mobile Menu → Services → Residential, and Menu → How It Works, navigated correctly and closed the menu.
- Native mobile FAQ opened and displayed its answer.
- Escape closed the Services disclosure and the mobile menu; desktop focus returned to the Services trigger.
- Keyboard skip link moved focus to `main-content`.
- Contact `mailto:` and `tel:` destinations exactly match the supplied business email and phone. No message or call was sent; visitor mail/phone app behavior depends on the visitor's device.
- Header CSSOM confirmed charcoal `rgb(32,33,35)` backdrop; the original radial/linear gradient and complete 1px teal rim; BBY in Playfair Display 700 and Technologies in Inter 600.
- The original checkout remained clean after all work.

## Issues found and fixed during QA

- Desktop Services dropdown initially extended beyond the right edge: aligned it to the trigger's right edge.
- Decorative subpage art initially widened the document: clipped it within its section.
- Platform-dependent diagonal arrow glyph rendered as a missing character: replaced directional arrows with inline stroke SVG icons.
- Long contact email wrapped awkwardly at the narrowest mobile width: adjusted only its mobile type size/spacing.

## Limits

- **No new hosted sandbox exists yet.** Native Sites remix capability was unavailable; no manual hosting workaround was used.
- Therefore new-site owner-private access and deployed behavior cannot yet be verified. The local draft contains no hosted project ID and is not publicly published.
- Browser console errors observed were from the environment's browser extension, not the site's assets or application code.
- No live email, telephone call, or form delivery was attempted. The site intentionally uses ordinary mail/phone links, not a submission backend.
- External BBY Restaurants URL is the user-supplied official link; its service was not modified.
- Preview fixture files and browser screenshots are internal QA and not part of the hosted `dist/` release.
