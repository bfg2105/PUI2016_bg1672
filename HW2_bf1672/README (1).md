This folder contains scripts and notebooks for the homework 2 assignment for PUI2016.  It contains the following notebooks:
HW2\_assignment3.pynb (This is my notebook for assignment 3)
bus\_locations\_practice.pynb (this was a practice notebook for writing scripts for assignments 1 and 2)

This folder contains the following scripts:
README.md (this readme file)
show\_bus\_locations.py (script for assignment 1-- when entered in the command line with two arguments (mta api key, and the bus line) returns a list of the busses in that line and gives their lat and long coordinates)
get\_bus\_info.py (script for assignment 2 -- when entered in the command line with 3 arguments (mta api key, bus line, and csv file named for the busline) writes the status of all the busses in that line by naming the stop they are approaching or at, and specifies if they are approaching or at the stop)

For this homework assignment, I worked by myself, but I got help from Professor Bianco and classmates at Wednesday night's office hours.

For assignment 1 and 2 (get\_bus\_info.py and show\_bus\_locations.py) I used a script I found online (at this website: http://python3porting.com/noconv.html) in order to load the url library for both python 2 and python 3.  There was an error in this code, and Professor Bianco fixed it for me (she added a 2 after urllib).

Matt Sloane showed me how to use the .columns() command on my dataframe for assignment three.  He also shared his code for writing to a csv file for assignment 2.  

