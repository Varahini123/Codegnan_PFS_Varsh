#7.?-it will form a searching pattern as it will take any zero or one character for (?)
#syntax-re.findall(".?",variable_name)
'''
import re
any="This meta character"
an=re.findall("Th.?",any)
go=re.search("Th.?",any)
print(an)
print(go)
'''
#8.{}-This meta character will form a searching pattern as we can mention the size in the {}
#syntax-re.search(".{size}",variable_name)
'''
import re
any="This meta character will form a searching pattern as it will take"
an=re.findall(".{25}",any)
so=re.search(".{25}",any)
print(an)
print(so)
'''
#9. | -it will form a searching pattern as it consider right or left any string is present or not for (|)
#syntax-:re.findall("|",var_name)
'''
import re
any="this meta character will form a searching pattern as it will take"
an=re.findall("that | will",any)
print(an)
'''
#10.specical sequence-a \ followed by one of the characters in the list below and has a special meaning
#\A-returns a match if the specified characters are at the beginning of the string
#Ex-\AThe
'''
import re
txt="The rain in Spain"
#check if the string starts with "The":
x=re.findall(r"\AThe",txt)
print(x)
if x:
    print("Yes,there is a match")
else:
    print("No match")
'''
#\b-returns a match where the specified characters are at the beginning or at the end of a word
#Ex-r"\bain"
'''
import re
txt="The rain in Spain"
#Check if " is present at the beginning of a WORD
x=re.findall(r"\bSpain",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
'''
#\d-returns a match where the string contains digits(numbers from 0-9)
#Ex-"\d"
'''
import re
txt="The rain in 56 Spain"
#check if the string contains any digits(numbers from 0-9)
x=re.findall("\d",txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")
'''
#\D-returns a match where the string does not contain digits
#Ex-"\D"
'''
import re
txt="The rain in 76 Spain"
#returns a match at every no-digit character
x=re.findall("\D",txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")
'''
#\s-returns a match where the string contains a white space character
#Ex-"\s"
'''
import re
txt="The rain in Spain"
#returns a match at every white-space characters
x=re.findall("\s",txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")
'''
#\S-returns a match where the string does not contain a white space character
#Ex-"\S"
'''
import re
txt="The rain in Spain"
#returns a match at every non-white-space characters
x=re.findall("\S",txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")
'''
'''
Time and Date
-------------
%d-day
%m-month
%Y-year
%H-hour
%M-minute
%S-second
%p-AM/PM
%A-Day name
%D-month name
'''
import datetime
now=datetime.datetime.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))
