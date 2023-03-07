Patient_name = input("Patient Name: ")
Patient_Birth_Date = input("When Patient born: ")
Age = 2022 - int(Patient_Birth_Date)
Is_NewPatient = input("Is a new patient: ")
print("Patient Name "+ Patient_name, "His Age is " + str(Age), "Is he New patient " + str(Is_NewPatient))

print("A basic calculator")
First = float(input("First number: "))
Second = float(input("Second Number: "))
Sum = First + Second
print("Sum of both numbers: " + str(Sum))