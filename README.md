# Async Proof of Concept

During my internship at Wicky, the CEO Nakul had a complaint that the webscraping service was taking too long to run, reaching upwards of 15 minutes for a full run-through. Looking into the code, I identified that we could be using the python Asyncio library to run our webscrapers with concurrency. 

This is a proof-of concept for the idea, where I taught myself to use the asyncio library, and then constructed a test model to compare the async vs sync methods to demonstrate time-saving potential. After showcasing this model to Nakul, I was approved to work with the rest of the dev team in reformatting the existing code to work with the async library. 

# Setup
1. Set up a python virtual environment `python -m venv .venv`
2. Install requirements with `pip install -r requirements.txt `
3. Run program with `python __init__.py`

