# BlackholeNotBlackhole

This webapp enabled scientists to quickly classify certain types of galaxy spectra.  Through an intuitive user interface, scientists build a training set for automatic galaxy classification and can curate the results of expiremental automatic classification algorithms.


# Background 

> Is it possible to use machine learning to reliably identify 'fossil' black holes in galaxies?

A 'fossil' black hole exists in a galaxy with large amounts of Helium II (He II). We can easily write a script to 
filter out graphs without He II, BUT galaxies with Wolf-Rayet (WR) stars also have He II. WR stars leave a 
'bump' in the graph at a specified interval, but the bump is not well defined. There is no known way to calculate 
whether a graph has this WR bump or not. That's where machine learning comes in. We want to see if the WR bump can 
be found using a neural net. Using machine learning to find the WR bump in graphs will allow us to subtract WR bump 
graphs from the He II graphs. Thus we will have a list of galaxies with He II and no WR stars, leaving us with galaxies 
that have 'fossil' black holes.

For more details, please see
<a href="https://github.com/codeforgoodconf/black_holes_backend/blob/master/ML_Info/Project_Information.pdf"> ML_Info/Project_Information.pdf </a>

# Functionality 

- After login, user sees two modules: 'module1' and 'module2' (we can change the names later)
- **Training page** allows a user to classify whether a shown spectra has a WR bump or not.  This human labeled data is then added to the known WR bump data set that is used to train the classification models.
- **Varification page** allows a user currate the results of the expiremental classification models.  They are shown the spectra and the machines prediction and are asked to confirm or deny the results.
 


