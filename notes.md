# Black Holes Web App

Question: 

Is it possible to use machine learning to reliably identify 'fossil' black holes in galaxies?

Background:

A 'fossil' black hole exists in a galaxy with large amounts of He II.
We can easily write a script to filter out graphs without He II, BUT galaxies with Wolf-Rayet (WR) stars also have He II.
WR stars leave a 'bump' in the graph at a specified interval, but the bump is not well defined.
There is no known way to calculate whether a graph has this WR bump or not.
That's where machine learning comes in.
We want to see if the WR bump can be found using a neural net.
Using machine learning to find the WR bump in graphs will allow us to subtract WR bump graphs from the He II graphs.
Thus we will have a list of galaxies with He II and no WR stars, leaving us with galaxies that have 'fossil' black holes.

# What's Important for the Backend

Our Data set:

  - 2D graphs with flux (or brightness) over wavelength. 
  - Each graph is less than 100 Kb.
  - maximum 1,271,680 data files.

