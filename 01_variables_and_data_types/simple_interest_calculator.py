#----------SI Calculation-----------

P = float(input("Enter the principal amt :"))
R = float(input("Enter the rate of interest :"))
T = float(input("Enter the time period in years:"))
si = (P * R * T) / 100
print("The simple interest is :", si)
