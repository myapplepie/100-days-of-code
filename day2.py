# BMI = weight / height2 // kg and meters
# male/female  and pounds options
# output must be integer
height = float(input("enter your height in m "))
weight = float(input("enter your weight in kg "))
# gender = input("enter male or female")

result = int(weight / (height ** 2))

print(result)