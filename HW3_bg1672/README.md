# Homework 3

## Assignment 1
In the Thursday section of PUI, a classmate modeled how to make a set of 100 different sample sizes between 10 and 2000, how to then create an array, wherein each element was a random set of numbers with a chi-square distribution that had a mean of 100. He then wrote the code to calculate the means of each distribution, graph those means against sample size, and then plot the means in a histogram.  I used this code to replicate for the other distributions in the assignment: Poisson, Normal, Binomial, and one of my choosing: Wald.  I changed the code for each distribution so that the samples would be distributed according to the specific distribution I was modeling, but the basic code skeleton that my classmate origionally modeled was used for each one.  

## Assignment 2
I worked with Shay Lehman (sl5335) and Enrique Sanz Gonzalez (esg336@nyu.edu), as well as Dana Karwas (dlk253).  I wrote the code that takes any datestring and downloads the citibike data for that year/month to the present working directory.  I used code from this website: #https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659 to unzip and read the csv file to a dataframe.

I used the strategy used in last week's homework to cut columns from the data frame, that I had origionally borrowed from Matt Sloane (See HW2 for citation).  

Shay Lehman (sl5335) wrote the code to convert the starttime (which was a string data type) to a datetime data type.  She borrowed the code origionally from stack overflow.

Jon Toy helped me to pick out the start hour from the starttime by indexing into the string.  He shared with me code that was used in his other computer science class at NYU: DS-GA1002.  I borrowed that same idea of using the lambda to convert the string to a number.

Christian Rosado helped me plot the histogram.s

## Assignment 3
I used the curl method that Prof. Bianco showed us in class to download the bus time data to my working directory.  I took the formula for the z-statistic out of the class text, Statistics in a Nutshell, and I calculated the p value for the returned Z-statistic at this p value calculator: http://graphpad.com/quickcalcs/PValue1.cfm . 