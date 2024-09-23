# Legal Q&A Model

## Overview
A web interface for a fine-tuned legal question-answering model using Hugging Face Transformers.

## Prerequisites
- Docker installed on your machine
- Basic knowledge of using Docker

## Getting Started

### Building the Docker Container
To build the Docker container, run:
bash```docker build -t yourimage ```

### Running the Container

To run the container, use:

bash```docker run -p 8000:8000 yourusername/yourimage:tag```

### Accessing the Application
Once the container is running, access the application at `http://localhost:8000`

## Model Details
The model is fine-tuned on legal documents and can answer questions based on the provided context.
