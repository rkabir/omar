import os

keys = ["twentysix", "twentyseven", "twentyeight", "twentynine", "thirty",
    "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "ohsix", "ohseven", "oheight", "ohnine", "ten",
    "ohone", "ohtwo", "ohthree", "ohfour", "ohfive"]

for key in keys:
    os.popen("screen -r %s -p 0 -X stuff \"exit\n\"" % (key))
