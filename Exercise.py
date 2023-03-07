Weight  = float(input("weight: "))
weight_meter = input("K(g) or L(b): ")

if weight_meter == "l":
    weight_in_KG = Weight /2.2
    print("Weight in KG: " + str(weight_in_KG))
elif weight_meter == "k":
    Weight_in_LB = Weight * 2.2
    print("Weight in LB: " + str(Weight_in_LB))
