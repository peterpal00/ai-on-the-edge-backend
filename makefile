ROOT_PATH = backend
SERVICE_NAME =
SERVICE_PATH = $(ROOT_PATH)/$(SERVICE_NAME)

install:
	poetry install \
	--with data_service \
	--with test

run_api:
	poetry run uvicorn $(ROOT_PATH).$(SERVICE_NAME).main:app --reload --host 0.0.0.0


lint:
	poetry run flake8 --config setup.cfg $(SERVICE_PATH) --exclude *test*
	poetry run mypy --config-file pyproject.toml $(SERVICE_PATH) --exclude .*test*.
	poetry run black --config pyproject.toml --check $(SERVICE_PATH) --exclude .*test*.
	poetry run isort --sp pyproject.toml --check-only $(SERVICE_PATH) --skip *test*

format:
	poetry run black --config pyproject.toml $(SERVICE_PATH)
	poetry run isort --sp pyproject.toml $(SERVICE_PATH)


tf_init:
	terraform init

tf_plan:
	terraform plan -out=tfplan -detailed-exitcode

tf_apply:
	terraform apply tfplan

docker_build_prod:
	docker build --build-arg SERVICE_NAME=$(SERVICE_NAME) --target prod -t prod_$(SERVICE_NAME)_image .

docker_run_prod:
	docker run prod_$(SERVICE_NAME)_image