import requests;
import pandas as pd
import time
from pandas import ExcelWriter
df = pd.read_csv("Bank_Ifsc_mapping.csv")

bankname = df['Bank Name']
ifsc = "UTBI0NTRD65"
ifsc = df['IFSC Code']
tem = []
for temp in ifsc:
    print(temp)
    url = "https://ifsc.razorpay.com/"+temp
    data = requests.get(url)
    data = data.json()
    try:
        c = data['BANK']

    except TypeError:  # includes simplejson.decoder.JSONDecodeError
        c = "NOTFOUND"
    print(c)
    tem.append(c)
print(tem)
print(ifsc)
writer = ExcelWriter('output.xlsx')
df3 = pd.DataFrame(ifsc,bankname,tem)
df3.to_excel(writer,'Sheet1')
writer.save()
print("output saved as  output.xlsx")
