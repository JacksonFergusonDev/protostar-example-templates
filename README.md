# Protostar example templates

Two [Protostar](https://github.com/JacksonFergusonDev/protostar) templates for a FastAPI service: one as small as a template gets, and one that shows what a template can do. Both stay declarative. There is no template logic in any file.

## `minimal/`: one short file

[`minimal/protostar.toml`](minimal/protostar.toml) is the whole template. It names the tools it wants and adds stricter type checking, and Protostar writes everything those tools need: their configuration, commit hooks, and a CI workflow.

```bash
mkdir my-service && cd my-service
protostar init --from https://github.com/JacksonFergusonDev/protostar-example-templates/tree/main/minimal
```

## `service/`: starter code, a choice, and two tiers

[`service/protostar.toml`](service/protostar.toml) adds:

- **Starter files** in [`service/template/`](service/template/), with placeholders such as `<% PACKAGE_NAME %>` and a custom `<% SERVICE_PORT %>`.
- **A choice:** `--option database=postgres` adds SQLAlchemy, a `db.py`, and a `.env.example`; the default, `none`, leaves them out.
- **Two tiers:** `production` (the default) adds type checking, tests, commit hooks, and CI; `workbench` keeps the tooling light.

```bash
mkdir orbit-api && cd orbit-api
protostar init --from https://github.com/JacksonFergusonDev/protostar-example-templates/tree/v1.0.0/service \
  --option database=postgres --var SERVICE_PORT=8000
```

Leave out the flags in a terminal and Protostar asks for each choice instead.

[protostar-example-project](https://github.com/JacksonFergusonDev/protostar-example-project) was made this way. A scheduled workflow there opens a pull request whenever this repository tags a new release.

## Releases

Templates here are released together, as tags such as `v1.0.0`. A project made from a tag stays on it until it moves with `protostar sync --to latest`, which merges the new release into the project and keeps its own edits.

## Checking the templates

[`.github/workflows/check.yml`](.github/workflows/check.yml) runs `protostar check-template --strict` on both templates for every push, and reports any finding on the line it concerns.

See [Authoring Templates](https://protostar.jacksonferguson.me/usage/authoring-templates/) for the full template format.
