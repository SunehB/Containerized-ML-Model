# Iris Classification API

This is an API that serves a machine learning model trained on the famous Iris dataset. The model predicts the species of an Iris flower based on four input features: sepal length, sepal width, petal length, and petal width.

## Requirements

- Podman
- Python 3.x (optional, for local setup)
- Pip (optional, for local setup)

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SunehB/containerized-ml-model.git
   cd containerized-ml-model
2. **Build and run the container**:
    make build
    make run
The API will be running at http://localhost:5001/.

**To stop and remove the container**:

make stop

make remove

**Rebuild**

make rebuild

**To test inputs**

Place whatever combination of inputs to get a prediction. Can compare to the actual data set here: https://www.kaggle.com/datasets/uciml/iris

curl -X POST -H "Content-Type: application/json" \
    -d '{"input": [5.1, 3.5, 1.4, 0.2]}' \
    http://localhost:5001/predict





