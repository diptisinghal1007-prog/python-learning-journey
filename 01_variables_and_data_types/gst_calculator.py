#------------GST Calc------------

cost = float(input("Enter cost of the product : "))
gst = float(input("Enter GST rate : "))

gst_amount = (cost * gst) / 100
total_cost = cost - gst_amount
print("Total cost after applying GST : ", total_cost, "rs.")
