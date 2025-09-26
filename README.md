# NADAG innmelding python client 🚀

**A lightweight, Pythonic library for interacting with the 
[NADAG innmelding API](https://test.ngu.no/api/openapi-ui/) — 
quickly sync ground investigation data, all from Python.**


## Other resources
- https://test.ngu.no/api/openapi-ui/ + Explore: /api/nadag/innmelding/openapi/v1
- https://ngu.github.io/mono/

## Installation (end users)

```bash
pip install nadag-innmelding-python-client
```

## Usage

```python

```

## Automation: keeping the client in sync with upstream OpenAPI

A scheduled / on-demand GitHub Actions workflow (`auto-update.yaml`) keeps the client current:

1. Downloads the upstream OpenAPI specification from:
   `https://test.ngu.no/api/nadag/innmelding/openapi/v1` (stored at `openapi_specification/nadag-innmelding.yaml`).
2. Extracts the `info.version` value.
3. If the version differs from the committed spec, it regenerates the client using `openapi-python-client` with `templates/` + `config.yaml`.
4. Updates the package version in `nadag-innmelding-python-client/pyproject.toml` to match the spec version.
5. Creates a pull request (branch name: `chore/openapi-spec-v<spec-version>`) instead of committing directly.

After the pull request is merged:
- Manually create a git tag `v<spec-version>` (or create a GitHub Release with that tag).
- The existing `release.yaml` workflow (triggered on release creation) publishes the new version to PyPI using the `PYPI_TOKEN` secret.

Rationale for PR-based flow:
- Enables code review of generated changes.
- Lets you amend / adjust the version or templates before publishing.

### Manual update (optional)
To replicate the regeneration locally:

```bash
pip install openapi-python-client
python scripts/update_from_spec.py
```

This will download the latest spec, regenerate the client, and bump the package version. You can then open a PR or tag manually.

## Developer installation

Clone the repository.

## Contributing

Please open an issue before submitting a pull request. We welcome contributions and suggestions!
