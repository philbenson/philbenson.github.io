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
