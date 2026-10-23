# philbenson

Phil Benson's portfolio site: Django for pages, Vite and Tailwind for styles.

## Preview locally

Needs Docker (OrbStack works).

```sh
docker compose up --build
```

Open http://localhost:8000. Edits to templates, styles and Python reload the
page on their own. Stop with Ctrl+C.

After changing `package.json`, clear the cached packages so they reinstall:

```sh
docker compose down --volumes
docker compose up --build
```

## Build the site

The published site is static files: Django renders each page once, and GitHub
Pages serves the result. To build it locally, with the containers running:

```sh
docker compose exec vite npm run build
docker compose exec -e DJANGO_DEBUG=0 -e DJANGO_SECRET_KEY=local-build web python manage.py build_site _site
```

The site lands in `_site/`.

## Deploy

Every push to `main` runs `.github/workflows/deploy.yml`, which builds the site
the same way and publishes it to GitHub Pages at https://philbenson.name. A run
can also be started by hand from the repository's Actions tab.
