# Use a base image that includes PyTorch
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set the working directory
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Create a directory to store the downloaded model
RUN mkdir -p /app/models

# Download the model and save it to the models directory
RUN python -c "from transformers import AutoModelForQuestionAnswering, AutoTokenizer; \
    AutoTokenizer.from_pretrained('deepset/roberta-base-squad2', cache_dir='/app/models'); \
    AutoModelForQuestionAnswering.from_pretrained('deepset/roberta-base-squad2', cache_dir='/app/models')"

# Copy the fine-tuned model into the container
COPY fine_tuned_legalqa ./fine_tuned_legalqa

# Copy the rest of the application code
COPY . .

# Expose the port that Uvicorn runs on
EXPOSE 8000

# Run the application with Uvicorn
CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "8000"]
