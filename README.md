# Legal Q&A Model

## Overview
A web interface for a fine-tuned legal question-answering model using Hugging Face Transformers.

# Table of Contents

- [Legal Q&A Model](#legal-qa-model)
  - [Overview](#overview)
  - [Model](#model)
  - [Training Data](#training-data)
  - [Web Interface](#web-interface)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Instructions to Use the Legal Q&A Model](#step-by-step-instructions-to-use-the-legal-qa-model)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Build the Docker Container](#step-2-build-the-docker-container)
    - [Step 3: Run the Docker Container](#step-3-run-the-docker-container)
    - [Step 4: Access the Application](#step-4-access-the-application)
    - [Step 5: Using the Application](#step-5-using-the-application)
    - [Step 6: Stopping the Container](#step-6-stopping-the-container)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [License](#license)

## Model

The model used in this project is a fine-tuned version of the [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) model from Hugging Face Transformers. It is specifically designed for question-answering tasks, utilizing a transformer architecture to provide accurate responses based on given contexts. 

### Key Features:
- **Transformer Architecture**: Leverages the power of transformer models for improved performance.
- **Fine-Tuning**: Adapted for legal document context, enhancing its ability to understand and respond to legal inquiries.

## Training Data

The model has been fine-tuned using the [Open Australian Legal Q&A Dataset](https://huggingface.co/datasets/umarbutler/open-australian-legal-qa) (Butler, 2023) available on Hugging Face. This dataset comprises a collection of legal questions and their corresponding answers extracted from Australian legal documents. 

### Dataset Features:
- **Diverse Legal Questions**: Includes a wide range of questions covering various aspects of Australian law.
- **Contextual Information**: Each question is paired with relevant context from legal documents, allowing the model to learn the relationship between legal texts and user inquiries.

This rich dataset enables the model to provide precise and contextually relevant answers to user queries related to Australian legal matters.

## Web Interface

The web interface is built using [FastAPI](https://fastapi.tiangolo.com/) and provides an intuitive user experience for interacting with the question-answering model. 

### Key Features:
- **User-Friendly Form**: Users can easily input their questions and context through a simple HTML form.
- **Dynamic Responses**: The application processes inputs in real-time and displays the top answers along with their confidence scores.
- **Responsive Design**: The interface is designed to be accessible on both desktop and mobile devices.

### Technologies Used:
- **FastAPI**: For building the web application and API.
- **Jinja2**: For rendering HTML templates dynamically.
- **Transformers**: For loading the fine-tuned model and processing questions.

The web interface serves as a bridge between users and the underlying model, facilitating easy access to legal information and enhancing the usability of the fine-tuned question-answering system.

## Prerequisites

Before you start, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started) (follow the installation instructions for your operating system)
- Basic command line knowledge

## Step-by-Step Instructions to Use the Legal Q&A Model

### Step 1: Clone the Repository

1. Open your terminal (Command Prompt, PowerShell, or Terminal).
2. Clone the repository using the following command (replace `yourusername` and `yourrepository` with your GitHub username and repository name):
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
3. Navigate into the cloned directory:
   ```bash
   cd yourrepository

### Step 2: Build the Docker Container

1. In the terminal, ensure you are in the root of the project directory (where the `Dockerfile` is located). 
2. Build the Docker image using the following command (replace `yourimage` with your desired image name):
   ```bash
   docker build -t yourimage .

### Step 3: Run the Docker Container

Once the image is built, you can run the Docker container using:
  ```bash
docker run -p 8000:8000 yourimage
```

This command maps port 8000 of your local machine to port 8000 of the container, allowing you to access the web interface.

### Step 4: Access the Application

1. Open your web browser.
2. Navigate to http://localhost:8000.
3. You should see the application interface where you can input your questions and context.

### Step 5: Using the Application

1. Enter your Question: In the "Question" input field, type your legal question.
2. Provide Context: In the "Context" textarea, paste the relevant legal document text.
3. Click the "Get Answer" button.
4. The application will process your input and display the answer with its confidence score.

### Step 6: Stopping the Container

To stop the Docker container, go back to your terminal and press `Ctrl + C`. This will stop the running process.

## Troubleshooting

- If you encounter issues building the Docker image, ensure that you have Docker running and that your internet connection is stable (as it may need to download dependencies).
- For any errors while running the container, check the terminal output for error messages, and ensure that the correct ports are not in use by other applications.

## Contributing

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.
