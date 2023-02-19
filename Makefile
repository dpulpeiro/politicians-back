DOCKER_IMAGE_NAME=politicians-back
PROD_TAG=0.0.1

DEV_IMAGE_NAME=${DOCKER_IMAGE_NAME}:dev
PROD_IMAGE_NAME=${DOCKER_IMAGE_NAME}:${PROD_TAG}

# -------------------- Development -----------------------
dev/build:
	DOCKER_BUILDKIT=1 docker build \
		--build-arg USER_NAME=user \
		--build-arg USER_UID=$(shell id -u) \
		--build-arg USER_GID=$(shell id -g)  \
		-f devops/dev/Dockerfile \
		-t ${DEV_IMAGE_NAME} .

dev/up:
	cd devops/dev && docker-compose up -d

dev/down:
	cd devops/dev && docker-compose down

dev/shell:
	docker run -it --rm \
		-v $(shell pwd):/app \
		--network host \
		--entrypoint /bin/bash \
		${DEV_IMAGE_NAME}

black:
	docker run -it --rm \
		-v $(shell pwd):/app \
		${DEV_IMAGE_NAME} black /app/src

# -------------------- Production -----------------------
prod/build:
	DOCKER_BUILDKIT=1 docker build \
		-f devops/prod/Dockerfile \
		-t ${PROD_IMAGE_NAME} .

prod/up:
	cd devops/prod && docker-compose up -d

prod/down:
	cd devops/prod && docker-compose down

