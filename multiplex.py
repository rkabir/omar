import os

keys = ["ohone", "ohtwo", "ohthree", "ohfour", "ohfive",
    "ohsix",  "ohseven",  "oheight", "ohnine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen",  "nineteen", "twentyoh",
    "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive",
    "twentysix", "twentyseven", "twentyeight", "twentynine", "thirty"]

for key in keys:
    os.popen("screen -x %s -p 0 -X stuff \"python worker.py %s\n\"" % (key, key))
