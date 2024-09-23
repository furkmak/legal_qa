FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create a directory to store the downloaded model
RUN mkdir -p /app/models

# Download the model and save it to the models directory
RUN python -c "from transformers import AutoModelForQuestionAnswering, AutoTokenizer; \
    AutoTokenizer.from_pretrained('deepset/roberta-base-squad2', cache_dir='/app/models'); \
    AutoModelForQuestionAnswering.from_pretrained('deepset/roberta-base-squad2', cache_dir='/app/models')"

COPY fine_tuned_legalqa ./fine_tuned_legalqa

COPY . .

EXPOSE 8000

CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "8000"]
