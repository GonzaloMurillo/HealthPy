# HealthPy

A collection of Python scripts oriented to health / sport training enthusiasts.

plotmytrainig.py 

This scripts helps to draw training routines mostly for winter training in the roller. 
The way it works is taking the input from a file with the following format:

minutesxbpmxcadence
minutesxbpmxcadence
minutesxbpmxcadence

Each line representing an interval; so for example if you want to define a training of 20 minutes at 150 bpm with a cadence of 80 rpm, followed by 10 minutes recover at 110 bpm and a cadence of 105 rpm, and finally 20 minutes at 148bpm and a cadence of 90 rpm, the file that you would need shall contain the following lines:

20x150x80
10x110x105
20x148x90

The script will ask for the name of the file with this information and also will request you to input personal data like age, max heart rate and rest heart rate, so it can calculate the heart zones based on the Karvonen formula.

With all the above information will plot a graph.
