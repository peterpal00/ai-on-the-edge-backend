ROOT_PATH = backend

tf_init:
	terraform init

tf_plan:
	terraform plan -out=tfplan -detailed-exitcode

tf_apply:
	terraform apply tfplan

lint:
	poetry run flake8 --config setup.cfg $(ROOT_PATH)
	poetry run mypy --config-file pyproject.toml $(ROOT_PATH)
	poetry run black --config pyproject.toml --check $(ROOT_PATH)
	poetry run isort --sp pyproject.toml --check-only $(ROOT_PATH)

format:
	poetry run black --config pyproject.toml $(ROOT_PATH)
	poetry run isort --sp pyproject.toml $(ROOT_PATH)