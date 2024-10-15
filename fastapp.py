from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline
from typing import List
from jinja2 import Template

app = FastAPI()

# Load the Q&A model pipeline
qa_pipeline = pipeline("question-answering", model="fine_tuned_legalqa")

# Sliding window function to split context into chunks
def split_into_windows(context: str, max_len: int = 384, stride: int = 128) -> List[str]:
    tokens = context.split()  # Tokenize the text into words
    windows = []
    start = 0
    while start < len(tokens):
        window = tokens[start:start + max_len]  # Take a chunk of max_len tokens
        windows.append(" ".join(window))  # Join the tokens back into a string
        start += stride  # Move the window forward by the stride (overlap)
    return windows

# Aggregate results and return top 5 answers based on confidence
def aggregate_top_answers(question: str, context_windows: List[str], top_n: int = 5):
    all_results = []

    for window in context_windows:
        result = qa_pipeline(question=question, context=window)
        all_results.append(result)

    # Sort the answers by confidence score (descending order)
    sorted_results = sorted(all_results, key=lambda x: x['score'], reverse=True)

    # Return the top 'n' results
    return sorted_results[:top_n]

# HTML template for the form
html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal Q&A Model</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #2b2b2b;
            color: #eaeaea;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        h1 {
            text-align: center;
            color: #f1f1f1;
            font-size: 2.5em;
        }
        form {
            background-color: #3c3c3c;
            max-width: 600px;
            width: 100%;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border: 1px solid #555;
        }
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
            color: #cfcfcf;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            background-color: #4b4b4b;
            border: 1px solid #666;
            border-radius: 5px;
            color: #fff;
            font-size: 16px;
            box-sizing: border-box;
        }
        input[type="text"]::placeholder, textarea::placeholder {
            color: #9a9a9a;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        button:hover {
            background-color: #0056b3;
        }
        h2 {
            text-align: center;
            color: #7ed957;
            margin-top: 20px;
            font-size: 1.8em;
        }
        @media (max-width: 768px) {
            form {
                padding: 20px;
            }
            h1 {
                font-size: 2em;
            }
            h2 {
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <form method="POST" action="/qa">
        <h1>Ask About Court Cases</h1>
        <label for="question">Question:</label>
        <input type="text" id="question" name="question" placeholder="Enter your question here" required>
        
        <label for="context">Context:</label>
        <textarea id="context" name="context" rows="6" placeholder="Enter the legal document text here" required></textarea>
        
        <button type="submit">Get Answer</button>
    </form>

    {% if answer %}
        <h2>Answer: {{ answer[0].answer }} (Confidence: {{ answer[0].score | round(2) }})</h2>
    {% endif %}
</body>
</html>
"""

# Define the route to display the form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    template = Template(html_form)
    return template.render(answer=None)

# Define the API endpoint for form submission
@app.post("/qa", response_class=HTMLResponse)
async def answer_question(question: str = Form(...), context: str = Form(...)):
    # Split the context into windows
    context_windows = split_into_windows(context)

    # Aggregate and get top 5 answers
    top_answers = aggregate_top_answers(question, context_windows)

    # Render the template with the answer
    template = Template(html_form)
    return template.render(answer=top_answers)

# Run the app with Uvicorn when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
