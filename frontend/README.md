# Functionality 

- After login, user sees two modules: 'module1' and 'module2' (we can change the names later)
- **Training page** allows a user to classify whether a shown spectra has a WR bump or not.  This human labeled data is then added to the known WR bump data set that is used to train the classification models.
- **Varification page** allows a user currate the results of the expiremental classification models.  They are shown the spectra and the machines prediction and are asked to confirm or deny the results.
 
# Setup

The app is built using Flask and Plotly.

With Python3.6 installed on your machine the following sequence of commands will get the development app running.

```
git clone https://github.com/codeforgoodconf/black_hole_frontend
cd black_hole_frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m scripts.seeds
python run.py
```


