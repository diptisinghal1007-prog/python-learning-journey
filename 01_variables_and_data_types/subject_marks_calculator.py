#----------Subject Marks Calc-----------

sub1 = float(input("Enter first subject marks :"))
sub2 = float(input("Enter second subject marks : "))
sub3 = float(input("Enter third subject marks : "))
sub4 = float(input("Enter fourth subject marks : "))
sub5 = float(input("Enter fifth subject marks :"))
total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5
percentage = avg
print("Total marks obtained : ", total)
print("Average marks : ", avg)
print("Percentage :", percentage,"%")
