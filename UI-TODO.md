# UI TODO

## Done

- [x] Front desk page: offer, four-step project flow, drawn gallery, brief form, who runs it
- [x] Privacy, terms and data deletion pages at the root, all three telling the same story
- [x] `vercel.json` fixed: catch-all rewrite removed (it was sending `/privacy.html` to the home page, which breaks verification and hides the policy)
- [x] Placeholder `HELLO_EMAIL` replaced everywhere with a working address
- [x] Duplicate policies removed. `docs/privacy.html` said "no user data is collected" while the site has a brief form; that contradiction is gone, one policy set remains
- [x] Gallery assets moved `docs/assets/` → `assets/`, all four SVGs rasterised and ink-measured before being shown
- [x] AI renders (`assets/0*.jpg`) no longer presented as "selected work"; they are not on the front desk until they have an honest label

## Open

- [ ] Domain purchase, then DNS to Vercel
- [ ] Real mail on the domain (for now `levia-2@ilands.app` is the working address)
- [ ] Connect Vercel auto-deploy (needs the account owner)
- [ ] Tool directory page driven by `tools/registry.json`, with tier from `docs/tools-ui.md` and honest status
- [ ] Gallery page with zoom/pan over the SVG pages
- [ ] Concrete-render section: one finished sheet set, once the set is complete
