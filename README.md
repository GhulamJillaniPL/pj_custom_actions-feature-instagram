# pj_custom_actions
PJ Custom Actions Application - API

## Development Environment Setup

```shell
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -e .[dev]
pip install -U -r dev-requirements.txt
```

## Run Development Server
```shell
flask --app custom_actions --debug run -h 0.0.0.0 -p 8000
```
Then visit http://localhost:8000

## Managing Dependencies

When updating adding a new dependency or updating the version of a dependency 
modify the pyproject.toml. Put application requirements in `dependencies` under 
`[project]` with fully qualified version. For test/build/development dependencies, 
add to the `dev` list under `[project.optional-dependencies]`. Then run 
`make requirements` which will run `pip-compile` to update both `requirements.txt` 
and `dev-requirements.txt`. Then run `pip install -e .` or `pip install -e .[dev]` 
to install newly added requirements
