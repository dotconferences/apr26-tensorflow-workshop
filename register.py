#!/usr/bin/env python

import re
import sys
import base64
import urllib2
import urllib

try:
    import tensorflow
except:
    print("Sorry, but you don't seem to have Tensorflow installed. Please refer to the README for instructions!")
    sys.exit(1)

print("Congratulations you have Tensorflow %s installed. Now, let's register to the workshop!" % tensorflow.__version__)
print("")

fullname = raw_input("What is your full name? ")
email = raw_input("What is your email address? ")

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("This doesn't look like a valid email address, sorry!")
    sys.exit(1)

print("")
print("We are now ready to submit your registration!")

if raw_input("Are you *sure* you will be able to attend the workshop on April 26th? [y, n] ").lower() not in ("y", "yes"):
    print("Okay! Next time maybe.")
    sys.exit(1)


form = "https://docs.google.com/forms/d/e/1FAIpQLSd4bKqFTcTa-3XbxS9Jp5TqtAreo1Zf15IAF7yxpd3wovYdZQ/formResponse"

try:
    r = urllib2.urlopen(form, urllib.urlencode({
        "entry.180159366": fullname,
        "entry.232824734": email,
        "entry.78057320": tensorflow.__version__,
        "entry.1000848763": base64.b64encode(fullname)
    }))

    resp = r.read()
except Exception, e:
    raise

print("")
print("Congratulations, you are registered to the workshop! You will receive an email as confirmation in the next few days.")
print("")
