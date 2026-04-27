'''
#Regular Expression(RegEx)
------------------
-->this regular expression or RegEx is a sequence of characters that forms a searching pattern.
-->to use this we have to import re, which will unlock the package

Functions
----------
1.find all-->by using this fucntion, it will find all sequnece in the string
syntax-->re.findall(metachar,variable_name)
2.search-->by using this function, it will only find first sequence in the string
syntax-->re.search("metachar",variable_name)

Metacharacters
------------------
-->Metacharacters are used to form searching patterns

1.[]->in this metacharcters we search for [a-z],[A-Z],[0-9]
import re
any = "this regular expression or RegEx is a sequence of characters that forms a searching pattern."
so = re.findall("[a-z]",any)
an = re.search("[a]",any)
print(so)
print(an)

2.dot(.)->this meta character will form a searching pattern as it will take any single character for(.)
import re
we = "hello"
the = re.findall("h....o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

3.cap^->this is used to find the string is starting with the sequence or not
syntax-->re.findall("metachar",variable_name)
import re
how = "this is used to find the string is starting with the sequence or not"
who = re.findall("^This is",how)
then = re.search("^this",how)
print(who)
print(then)

4.$->used to find the string is ending with the sequence or not
syntax-->re.findall("$",variable_name)
import re
out = "this is used to find the string is starting with the sequence or not"
one = re.findall("sequence $",out)
two = re.search("^this$",out)
print(one)
print(two)

5.*->will form a searching pattern as it will take any zero or more character for (*)
syntax-->re.findall(".*",variable_name)
import re
hey="will form a searching pattern as it will take any zero or more character"
hi=re.findall("c.*r",hey)
hello=re.search("T.*",hey)
print(hey)
print(hi)

6.+->this meta characterbwill form a searching pattern as it will take any one or more character for(+)
syntax-->re.search(".+",variable_name)
import re
hema="will form a searching pattern as it will take any zero or more character"
hi=re.findall("an.+r",hema)
hey=re.search("T.*",hema)
print(hi)
print(hey)'''

























                    
