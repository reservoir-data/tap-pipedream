<div align="center">

# tap-pipedream

<div>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-pipedream/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-pipedream/main.svg"/>
  </a>
  <a href="https://github.com/reservoir-data/tap-pipedream/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-pipedream"/>
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
  </a>
  <a href="https://pypi.org/p/tap-pipedream/">
    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/tap-pipedream"/>
  </a>
</div>

Singer tap for [Pipedream](https://pipedream.com/). Built with the [Meltano Singer SDK](https://sdk.meltano.com).

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| token               | True     | None    | API Token for Pipedream |
| start_date          | False    | None    | Earliest timestamp to get data from |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

A full list of supported settings and capabilities is available by running: `tap-pipedream --about`

### Source Authentication and Authorization

To generate an API key, follow the instructions [in the docs](https://pipedream.com/docs/api/auth/#pipedream-api-key).

## Usage

You can easily run `tap-pipedream` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pipedream --version
tap-pipedream --help
tap-pipedream --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install hatch
```

### Create and Run Tests

Run integration tests:

```bash
hatch run test:integration
```

You can also test the `tap-pipedream` CLI interface directly:

```bash
hatch run sync:console -- --about --format=json
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-pipedream
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pipedream --version
# OR run a test `elt` pipeline:
meltano elt tap-pipedream target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
