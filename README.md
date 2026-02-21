PCA applied to mining magnitudes  
Applied to denoising and Correlation  

Random Forest  
For 1 magnitud and for 6 magnitudes, with confusion matrix and Feature Ranking (similar to PCA)

K-means

K Nearest Neighbourd

Logistic regression considering 4 physics magnitudes for the samples, and 3 possible rock units classification.

Steps for API:  
Call them in different scripts via Terminal.  
Use uvicorn: > uvicorn main:app --reload  # main is the name of file main.py with fastapi inside
then go to http://127.0.0.1:8000/docs         # there you see a web app with the input output of your script.

Steps for fasAPI and Streamlit (web app):  
geophysics-api/  
├── app/  
│   ├── __init__.py      # Makes 'app' a package. It is empty.  
│   ├── main.py          # Your FastAPI code  
│   └── models.py    
|____ streamlit_app.py  

You need two terminals open:  
Terminal 1 (The Backend): uvicorn app.main:app --reload  
Terminal 2 (The Frontend): streamlit run streamlit_app.py
