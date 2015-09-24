"""
birthday.py
Author: Ryan Kynor
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""



name = input("What is your name? ")
month = float(input("What month were you born? "))
year = float(input("What year were you born "))
day = float(input("What day were you born "))


if month == October and day == 31:
    print ("You were born on Halloween!")
elif month == September and day == 24:
    print ("Happy Birthday")
elif 1950 > year >= 1940:
    print ("{0}, you were a 40's baby." format.(name))
elif 1960 > year >= 1950:
    print ("{0}, you were a 50's baby." format.(name))
elif 1970 > year >= 1960:
    print ("{0}, you were a 60's baby." format.(name))
elif 1980 > year >= 1970:
    print ("{0}, you were a 70's baby." format.(name))
