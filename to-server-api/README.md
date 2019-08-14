<p align='center'><img src='./assets/to-logo.png' width='50px'/></p>

# TO - Server and API

## Developers

For development, use the `wsgi.py` file as the starting point.

```bash
python wsgi.py
```

## Server Configuration

Many files for configuring an Ubuntu server to run application can be found in `server-configs/`.

> Be sure to modify files with correct user information (\<username>, etc)

Some intructions can be found on [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04).

## Environment Variables

- `DB_USER`: the username for your database
- `DB_PASS`: the password for your database
- `DATABASE_URL` (optional): The location of the database. If none is provided, a local SQLite DB will be used

## API

For POST requests, params are the keys present in the JSON

For GET requests, params are the keys present in the URL params

HTTP Method | Endpoint      | Params    | Description
:---:       | ---           | ---       | ---
POST        | /create-alias | `alias`: the alias for the target<br/>`target`: the target URL | Creates an alias from the given params
GET         | /search       | `query`: the query string for the search | Returns the top 10 aliases from the search query. Aliases include the `alias` and `target`. The response is JSON w/ `aliases` as a key for a list of objects with `alias` and `target` keys
GET | /alias/&lt;alias&gt;  | None, but the url should contain `alias`: the alias you want the `target` for | Returns the `target` for the given alias. If no `target` exists, a `404` will be returned