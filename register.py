import re
import sys
import base64

print("Sorry, the workshop is full! Please signup to the dotConferences newsletter at http://www.dotconferences.com to be the first to know about future events!")
sys.exit(1)

if sys.version_info[0] != 3:
    print("Sorry, you need Python 3 for this workshop. Please refer to the README for instructions!")
    sys.exit(1)

from urllib.request import urlopen
from urllib.parse import urlencode

try:
    import tensorflow
except:
    print("Sorry, but you don't seem to have Tensorflow installed. Please refer to the README for instructions!")
    sys.exit(1)

try:
    import matplotlib
except:
    print("Sorry, but you don't seem to have matplotlib installed. Please refer to the README for instructions!")
    sys.exit(1)

print("Congratulations you have Tensorflow %s installed. Now, let's register to the workshop!" % tensorflow.__version__)
print("")

fullname = input("What is your full name? ")
email = input("What is your email address? ")

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("This doesn't look like a valid email address, sorry!")
    sys.exit(1)

print("")
print("We are now ready to submit your registration!")

if input("Are you *sure* you will be able to attend the workshop on April 26th? [y, n] ").lower() not in ("y", "yes"):
    print("Okay! Next time maybe.")
    sys.exit(1)

formid = "1FAIpQLSd4bKqFTcTa-3XbxS9Jp5TqtAreo1Zf15IAF7yxpd3wovYdZQ"
form = "https://docs.google.com/forms/d/e/%s/formResponse" % formid

try:
    r = urlopen(form, bytes(urlencode({
        "entry.180159366": fullname,
        "entry.232824734": email,
        "entry.78057320": "Tensorflow %s / Python %s" % (tensorflow.__version__, ".".join(map(str, sys.version_info[:3]))),
        "entry.1000848763": base64.b64encode(bytes(fullname, "utf-8"))
    }), "utf-8"))

    resp = r.read()
except Exception as e:
    raise

print("")
print("Congratulations, you are registered to the workshop! You will receive an email as confirmation in the next few days.")
print("")
