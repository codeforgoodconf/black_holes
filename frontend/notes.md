# Black Holes Web App

Question:

Is it possible to use machine learning to reliably identify 'fossil' black holes in galaxies?

Background:

A 'fossil' black hole exists in a galaxy with large amounts of Helium II (He II). We can easily write a script to 
filter out graphs without He II, BUT galaxies with Wolf-Rayet (WR) stars also have He II. WR stars leave a 
'bump' in the graph at a specified interval, but the bump is not well defined. There is no known way to calculate 
whether a graph has this WR bump or not. That's where machine learning comes in. We want to see if the WR bump can 
be found using a neural net. Using machine learning to find the WR bump in graphs will allow us to subtract WR bump 
graphs from the He II graphs. Thus we will have a list of galaxies with He II and no WR stars, leaving us with galaxies 
that have 'fossil' black holes.

# MVP (work on during event)

UX and functionality:

  - Landing screen is login page
  - After login, user sees two modules: 'module1' and 'module2' (we can change the names later)
  - 'module1' allows user to see a graph that has not been classified by the ML algo as having the WR 'bump' or not and allows them to classify it
  - 'module2' allows user to see a graph that has already been classified by the ML algo and can verify that 
  it does have the WR 'bump'
 
'module1' will have a graph and a simple 'yes' or 'no' form for WR bump

'module2' will have a graph with title 'classified WR' or 'classified NOT WR' and simple form to confirm or deny
classification
