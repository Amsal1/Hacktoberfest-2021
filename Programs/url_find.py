
# Pyhton code to search for URL in any sentence or string
import re
  
# function defined
def find_URL(string):

    # defined regex
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
      

# take input of string
input_string = str(input("Enter  the Input String :"))

# printing the answer, all URLS in input_string
print("Urls: ", find_URL(input_string))
