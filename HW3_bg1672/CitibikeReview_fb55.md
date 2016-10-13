# Citibike mini project review by fb55

very good presentation, usage of markdown cells and style options!

## IDEA:

well justified and interesting

## Null hypothesis and alternative

Formulated correctly, but missing the mathematical formulation.

## Data wrangling;

The data has to be moved into the PUIDATA directory; data should not be kept in the same directory as code, and for the class it has to be stored in PUIDATA so that we avoiding having multiple copies of redundant data as we grade 90 notebooks. so you should not get data from the puidata dir, which is your own so it only hosts data you downloaded in it, but put your data in that dir (so when we run it goes into our own $PUIDATA). If it is still not clear please do ask me what I mean.

good that you check both head and tail of your file. 

you have a lot of numbers of columns hardcoded in. That is risky if you have a flexible string as input: if a csv file with the same content but different column order is used your code would fail. it is best to be explicit when possible (i.e. use column names instead of number)

EACH FIGURE NEEDS A CAPTION THAT DESCRIBES IT. 

In your first figure, since the two histograms are separated in the axis, plotting with different colors is unnecessary and it does not help relating the gender between the two time ranges. Preserve the color for the gender so that a comparison is more intuitive.

The second plot is unnecessary for your research, but ointeresting for context. But context should come before targeted reserch details. So that should be the first plot.

You are not done quite yet with the wrangling. Not you have the start hour and you can take ratios of rides starting at the relevant time for the 2 genders, and then you are all set for a test of proportions (e.g. chi sq)

