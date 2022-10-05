import re
#import reg ex library

def find_name(line): #creating namefinder function
  
    # Names with 2 or 3 words (meaning a capital letter followed by lower case letters)
    pattern = r"([A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)"
    result = re.findall(pattern, line)

    # Names with a title
    pattern = r'(?:Mrs\.|Mr\.|Dr\.|Ms\.) [A-Z][a-z]+'
    result = result + re.findall(pattern, line)

    #Names with single letters 
    pattern = r'(Dr\. [A-Z]\. [A-Z][a-z]+|[A-Z]\. ?[A-Z]\. [A-Z][a-z]+|[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z][a-z]+)'
    result = result + re.findall(pattern, line)

    return result


f = open("names.txt")
for line in f.readlines():
    # print(line)
    result = find_name(line)
    if (len(result) > 0):
        print(result)
