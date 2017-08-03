# Black Holes Web App

Question: 

Is it possible to use machine learning to reliably identify 'fossil' black holes in galaxies?

Background:

A 'fossil' black hole exists in a galaxy with large amounts of Helium II (He II).
We can easily write a script to filter out graphs without He II, BUT galaxies with Wolf-Rayet (WR) stars also have He II.
WR stars leave a 'bump' in the graph at a specified interval, but the bump is not well defined.
There is no known way to calculate whether a graph has this WR bump or not.
That's where machine learning comes in.
We want to see if the WR bump can be found using a neural net.
Using machine learning to find the WR bump in graphs will allow us to subtract WR bump graphs from the He II graphs.
Thus we will have a list of galaxies with He II and no WR stars, leaving us with galaxies that have 'fossil' black holes.

# MVP (work on during the event)

Our Data set:

  - 2D graphs with flux (or brightness) over wavelength. 
  - Each graph is less than 100 Kb.
  - maximum 1,271,680 data files.

ML Algorithm Building Process:

  - Go to http://skyserver.sdss.org/casjobs/ and create an account and run a SQL query for the spectra set,
  while filtering out data files with 'STAR' header
  - Download all or a sample of the spectra to local machines
  - Run a script on the plots to filter only graphs with Equivalent Width around He II area
  - Use resulting set to build an ML algorithm to find WR bumps
  - Confirm with our solution set of WR bump graphs that it works

Goals:
  - Complete process outlined above
  - Create database with tables of unclassified, computer classified and human classified graphs
  - Build server-side code to handle computations and calls to the database on George Mason Argo Cluster: http://orc.gmu.edu/research-computing/argo-cluster/
  
  - Push unclassified and computer classified graphs to the frontend for classification and evaluation
  - receive user input on classification for unclassified graphs and put in human classified graphs table
  - receive user input on verification on classified graphs to teach the ML algorithm
