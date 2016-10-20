## HW6 
**Author:** Bailey Griswold

Principles of Urban Informatics
Professor Bianco
October 19, 2016

### Assignment 1
I worked with Dana Krawas, Jon Toy, Celia Yu, and Trang Tran Linh Dam.
For this assignmnet, we had to download the energy use by building from the New York City open data, as well as the PLUTO shape files.
I used code that Celia shared to download and unzip the data. After wrangling the data (dropping columns, forcing to float, calculating total energy, merging the two datasets)
I plotted total energy use and number of units.  To zoom in, I cut the data, and then plotted it on a log scale. 
I fit a linear model, flipped the variables, and plotted another linear model.  Then I compared the two models using a chi sq test, and the results were that
the Units vs Energy model was a better fit. Next I plotted a 2nd degree polynomial curve, and tested its goodness of fit against the linear model using the likilood ratio test.
The polynomial model was a better fit.

### Assignment 2:
My write up is on https://www.authorea.com/users/106627/articles/134234/_show_article
