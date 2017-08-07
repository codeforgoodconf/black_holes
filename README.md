# BlackholeNotBlackhole

This webapp enabled scientists to quickly classify different types of spectra collected by the Sloan Digital Sky Survey.  Through an intuitive user interface, scientists build a training set for automatic black hole classification and can curate the results of expiremental automatic classification algorithms.


# Background 

> Is it possible to use machine learning to reliably identify 'fossil' black holes in the provided spectra?

A 'fossil' black hole exists in a galaxy with large amounts of Helium II (He II). We can write a script to 
filter out graphs without He II, BUT galaxies with Wolf-Rayet (WR) stars also have He II. WR stars leave a 
'bump' in the graph at a specified interval, but the bump is not well defined. There is no known way to calculate 
whether a graph has this WR bump or not. That's where machine learning comes in. We want to see if the WR bump can 
be found using a neural net. Using machine learning to find the WR bump in graphs will allow us to subtract WR bump 
graphs from the He II graphs. Thus we will have a list of spectra with He II and no WR stars, leaving us with spectra 
that have 'fossil' black holes.

For more details, please see
<a href="https://github.com/codeforgoodconf/black_holes_backend/blob/master/ML_Info/Project_Information.pdf"> ML_Info/Project_Information.pdf </a>
