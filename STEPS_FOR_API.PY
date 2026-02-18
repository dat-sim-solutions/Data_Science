#----- FOLDER STRUCTURE -------

# MODULAR STRUCTURE
# Create a folder named geophysics-api and set it up like this:

geophysics-api/
├── app/
│   ├── __init__.py      # Makes 'app' a package. It is empty.
│   ├── main.py          # Your FastAPI code
│   └── models.py        # Logic for K-Means/Random Forest

# in app/main.py ------------------

from fastapi import FastAPI
# We import the function from our other file
from app.models import multiply_by_ten

app = FastAPI()

@app.get("/calculate/{number}")
def get_multiplication(number: float):
    # We call the function from models.py
    result = multiply_by_ten(number)
    
    return {
        "original": number,
        "result": result,
        "method": "Imported from models.py"
    }

# in app/models.py ----------------------

# This is a standard Python script
def multiply_by_ten(value: float):
    return value * 10

# In the Terminal run Uvicorn from the parent folder (the one outside the app folder) like this:
 uvicorn app.main:app --reload
# The output in 
http://127.0.0.1:8000/docs   
