def mitmorn():
    print("This is MIT Morning class")


mitmorn()
mitmorn()
mitmorn()


def calculate():
    x = 7
    y = 10
    print(x*y)
    print(x+y)
    print(x-y)
calculate()

def majina(fname,lname,age):
    print("My name is",fname,lname,"and I am",age,"years old.")
majina("Salma","Aden",34)
majina("Brian","Macharia",21)
majina("Samuel","Etoo",54)
majina("Christine","Atieno",43)
majina("Elizabeth","Stones",22)
majina("Elijah","Mwendwa",52)

#Calculate a function that is going to calculate the average of a list of numbers[2.5,6,3,5]

def average(list):
    total = sum(list)
    count = len(list)
    average = total / count
    return average
data =[3,6,8,9,2,1,8]
result =average(data)
print("The average is ", result)



#create a function in python that gives you the longest string in a list(palindrome)