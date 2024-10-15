import pandas as pd
import numpy as np
from google.cloud import bigquery
from google.oauth2 import service_account
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import EmbeddingsDriftMetric
from sentence_transformers import SentenceTransformer

# Load credentials from the service account key file
project = "legalqaapp"
dataset_id = "legal_data"
table_id = "qa_logs"
key_path = 'C:/Users/a/Desktop/legalapp2/legalqaapp_key.json'  # Replace with the path to your key file
credentials = service_account.Credentials.from_service_account_file(key_path,)

# Define your BigQuery query
bq_query = """
SELECT timestamp, question, context, answer, confidence
FROM legal_data.qa_logs
"""

# Load BigQuery data
client = bigquery.Client(credentials=credentials, project=project)
current_data = client.query(bq_query).to_dataframe()

# Load Hugging Face dataset as reference data
from datasets import load_dataset
reference_dataset = load_dataset("umarbutler/open-australian-legal-qa")
reference_data = reference_dataset['train'].to_pandas()

# Select relevant columns
reference_data = reference_data[['question', 'answer']]
current_data = current_data[['question', 'answer']]

# Use sentence transformer to convert the text into embeddings
model_miniLM = SentenceTransformer('all-MiniLM-L6-v2')

# Convert the text columns into embeddings
reference_embeddings = model_miniLM.encode(reference_data['question'].tolist())
current_embeddings = model_miniLM.encode(current_data['question'].tolist())

# Convert embeddings into DataFrame
reference_df = pd.DataFrame(reference_embeddings, columns=[f'col_{i}' for i in range(reference_embeddings.shape[1])])
current_df = pd.DataFrame(current_embeddings, columns=[f'col_{i}' for i in range(current_embeddings.shape[1])])

# Create a ColumnMapping to define embedding columns
column_mapping = ColumnMapping(embeddings={'small_subset': reference_df.columns[:10]})

# Initialize Evidently report for embeddings drift
report = Report(metrics=[
    EmbeddingsDriftMetric('small_subset')
])

# Run the report
report.run(reference_data=reference_df[:500], current_data=current_df[:500], column_mapping=column_mapping)

# Save the report as an HTML file
report.save_html('C:/Users/a/Desktop/legalapp2/embeddings_drift_report.html')

print("Embeddings drift report generated successfully.")
