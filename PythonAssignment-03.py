'''
Python code to create a function called most_frequent that takes a string
and prints the letters in decreasing order of frequency. Use dictionaries.
'''
str = (input("Please Enter a String: "))

def most_frequent(str):
    str = list(str)
    i = 0
    j = 0
    mydict = dict()

    for i in range(len(str)):
        count = 0
        for j in range(len(str)):
            if str[j] == str[i]:
                count += 1

        mydict[str[i]] = count

    print(mydict)

most_frequent(str)



   
