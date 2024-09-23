# Legal Q&A Model

## Overview
A web interface for a fine-tuned legal question-answering model using Hugging Face Transformers.

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
