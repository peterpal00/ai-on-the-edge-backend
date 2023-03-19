ROOT_PATH = backend
SERVICE_NAME = NOT_SET
SERVICE_PATH = $(ROOT_PATH)/$(SERVICE_NAME)

install_deps:
	poetry install \
	--with data_service \
	--with test

run_api:
	cd $(SERVICE_PATH) && \
	poetry run uvicorn $(ROOT_PATH).$(SERVICE_NAME).main:app --reload


lint:
	poetry run flake8 --config setup.cfg $(ROOT_PATH)
	poetry run mypy --config-file pyproject.toml $(ROOT_PATH)
	poetry run black --config pyproject.toml --check $(ROOT_PATH)
	poetry run isort --sp pyproject.toml --check-only $(ROOT_PATH)

format:
	poetry run black --config pyproject.toml $(ROOT_PATH)
	poetry run isort --sp pyproject.toml $(ROOT_PATH)


tf_init:
	terraform init

tf_plan:
	terraform plan -out=tfplan -detailed-exitcode

tf_apply:
	terraform apply tfplan