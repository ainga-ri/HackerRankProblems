dates = "Day Month Year"
date_keys = dates.split()

values_returned = list(map(int, input().rstrip().split()))
values_due = list(map(int, input().rstrip().split()))

data_returned = dict(zip(date_keys, values_returned))
data_due = dict(zip(date_keys, values_due))

if (data_returned["Year"] == data_due["Year"]):
    if (data_returned["Month"] == data_due["Month"]):
        if(data_returned["Day"] <= data_due["Day"]):
            charge = 0
        else:
            charge = (data_returned["Day"] - data_due["Day"]) * 15
    else:
        if (data_returned["Month"] < data_due["Month"]):
            charge = 0
        else:
            charge = (data_returned["Month"] - data_due["Month"]) * 500
else:
    if (data_returned["Year"] < data_due["Year"]):
        charge = 0 
    else:
        charge = 10000
print(charge)
