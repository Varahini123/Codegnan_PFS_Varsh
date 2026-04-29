'''
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[a-z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name = input("Enter Name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    if not validate_name(name):
        print("Invalid_Name")
    elif not validate_email(email):
        print("Inavlid email")
    elif not validate_phone(phone):
        print("Inavlid phone")
    elif not validate_password(password):
        print("Inavlid password")
    else:
        print("All inputs are valid")

if __name__ == "__main__":
    main()

Data analysis

#Useage
--------
this is critical because it converts raw data into actionable insights, enabling information to decision-making easy and improve
operational efficiency.

Impacts on:-
1.Decision-making
2.Improved Operational Efficiency
3.Customer Understanding
4.Market Insights
5.Risk Management
6.Data-Driven Strategies


import matplotlib.pyplot as pit
X = [1,2,3,4,5]
Y = [10,20,15,25,9]
pit.plot(X,Y)
pit.show()

#bar graph
import matplotlib.pyplot as pit
pit.bar(["TV9","NDTV","SumanTV"],[4,10,7])
pit.show()

#Pie graph
import matplotlib.pyplot as pit
pit.pie([30,40,50,20], labels = ["divya","varshini","likitha","vidyanjali"])
pit.show()

#Histogram
import matplotlib.pyplot as pit
pit.hist([23,4,6,18])
pit.show()

Numpy
-----
-->Numpy(numerical python) is the foundational open-source library for scientific computing in python, providing high-performance,
N-dimensional array objects (ndarray)
-->This enables efficient numerical computation linear algebra, and data manipulation, serving as the basis for tools like
Tensorflow and Scipy.

import numpy as np
arr = np.array([1,2,3])
print(arr - 1)

Pandas
------
-->this pandas is used for handling structured data in table format

import pandas as pd
data = {"Name" : ["Hema","Varshini"], "Marks" : [35,89]}
any = pd.DataFrame(data)
print(any)'''
































































