ROOT_PATH = backend
SERVICE_NAME = NOT_SET
SERVICE_PATH = $(ROOT_PATH)/$(SERVICE_NAME)

install_deps:
	poetry install

run_api:
	cd $(SERVICE_PATH) && \
	poetry run uvicorn $(ROOT_PATH).$(SERVICE_NAME).main:app --reload

