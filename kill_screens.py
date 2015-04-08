import os

keys = ["twentysix", "twentyseven", "twentyeight", "twentynine", "thirty",
    "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "six", "seven", "eight", "nine", "ten",
    "one", "two", "three", "four", "five"]

for key in keys:
    os.popen("screen -r %s -p 0 -X stuff \"exit\n\"" % (key))
