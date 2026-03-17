\# AI Semantic Search Project using Endee



\## Project Overview

In this project, I built a simple AI-based search system that understands the meaning of a query instead of just matching keywords. The goal is to demonstrate how vector databases and embeddings can be used in real-world applications like semantic search.



\## Features

\- Accepts user query and returns the most relevant result

\- Uses embeddings for similarity search

\- Built using FastAPI for backend

\- Demonstrates the concept of vector databases (Endee)



\## How It Works

When a user enters a query, the system converts it into a vector using a pre-trained model. The stored data is also converted into vectors. Then, similarity is calculated, and the most relevant result is returned.



\## Technologies Used

\- Python

\- FastAPI

\- Sentence Transformers

\- NumPy



\## Steps to Run the Project



1\. Install required libraries:

pip install -r requirements.txt



2\. Run the application:

python -m uvicorn app:app --reload



3\. Open the browser and go to:

http://127.0.0.1:8000/docs



4\. Use the `/search` endpoint to test the project.



\## Example

Input: AI  

Output: Machine learning is used in artificial intelligence.



\## Project Structure

\- app.py : Main API implementation

\- ingest.py : Data processing

\- requirements.txt : Required dependencies

\- README.md : Project documentation



\## Conclusion

This project helped me understand how embeddings and vector-based search work. It also gave hands-on experience with building APIs using FastAPI.

