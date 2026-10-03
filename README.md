# Linear Regression from Scratch
 
A small learning project: I implemented linear regression with gradient descent myself, trained it on the California Housing dataset, and deployed it as an API with FastAPI and Docker.
 
## Try it
 
**https://linear-regression-from-scratch.onrender.com/docs**
 
Click '/predict' → **Try it out**, enter an income (e.g. '3.5') and press **Execute**.
 
Note: it runs on a free server, so the first request can take about a minute to wake up.
 
**Units:** income is in $10,000s ('3.5' = $35,000), and the result is in $100,000s ('1.84' = $184,000).
 
## What I did
 
- Used one feature (median income) to predict median house value
- Removed rows where the price was capped at $500,000
- Wrote the cost function, gradients and gradient descent in NumPy
- Compared my result with scikit-learn's 'LinearRegression'
- Saved 'w' and 'b', built a FastAPI endpoint, and deployed it with Docker on Render
## Results
 
My model learned 'w = 0.408' and 'b = 0.414', and its cost was almost the same as scikit-learn's. The typical prediction error is about $TODO, because the model only uses one feature.
 
## Run locally
 
'''bash
pip install -r requirements.txt
uvicorn app.main:app --reload
'''
 
Or with Docker:
 
'''bash
docker build -t housing-api .
docker run -p 8000:8000 housing-api
'''
 
Then open http://127.0.0.1:8000/docs
