import os
import sys
import math

f = open("map.txt")
lines = f.readlines()
lines = [line.strip() for line in lines]
bucket_size = int( math.ceil( float(len(lines))/30 ) )

keys = ["ohone", "ohtwo", "ohthree", "ohfour", "ohfive",
    "ohsix",  "ohseven",  "oheight", "ohnine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen",  "nineteen", "twentyoh",
    "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive",
    "twentysix", "twentyseven", "twentyeight", "twentynine", "thirty"]

payload = {}
counter = 0
for key in keys:
    payload[key] = lines[counter:counter+bucket_size]
    counter = counter + bucket_size

args = sys.argv
index = args[1]

print "keyed on:"
print index

os.popen("mkdir -p %s" % (index))

for file in payload[index]:
    out_file = index + '/' + file.split("/")[5].replace(':','-').replace("'","-")
    os.popen("wget '%s' -O '%s'" % (file, out_file))
