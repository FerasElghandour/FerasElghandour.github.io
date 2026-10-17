# Portfolio site operations

Static production website on GitHub Pages. No build dependencies, third-party JavaScript, backend, secrets, forms, analytics or client records. LinkedIn handles inquiries outside the site. HTML declares a restrictive content policy; the site uses same-origin styles and no JavaScript.

## Release

Run `python tools/check_site.py`, review the selected project links and responsive layout, then push to `main`. The Pages workflow validates and publishes the repository. Confirm HTTPS and live links after deployment.

## Rollback

Revert the release commit and push. A successful Pages deployment restores the earlier site. The site stores no visitor-submitted data. Review links and case-study evidence when a featured repository changes.
