IMAGE_NAME = ml-model-serving
CONTAINER_NAME = ml-serving
PORT = 5001

# Build the container image
build:
	podman build -t $(IMAGE_NAME) -f Containerfile.serving .

# Run the container (mapping port 5001 on host to 5000 in the container)
run:
	podman run -d --name $(CONTAINER_NAME) -p $(PORT):5000 $(IMAGE_NAME)

# Stop the running container
stop:
	podman stop $(CONTAINER_NAME)

# Remove the stopped container
remove:
	podman rm $(CONTAINER_NAME)

# Stop and remove the container
clean: stop remove

# Install Python dependencies locally (optional)
install:
	pip install -r requirements.txt

# Set up for development or testing (optional)
dev:
	python app.py

# Rebuild and restart the container
rebuild: clean build run
