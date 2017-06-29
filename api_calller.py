import requests
import pandas as pd
import numpy as np
import time
from pandas import ExcelWriter
df = pd.read_csv("Bank_Ifsc_mapping.csv")
datap = np.array_split(df, 30)
writer = ExcelWriter('outputerfd.xlsx')
for i in range(26,30):
    time.sleep(10)
    print(datap[i])
    bankname = datap[i]['Bank Name'].str.capitalize()
    ifsc = "UTBI0NTRD65"
    ifsc = datap[i]['IFSC Code'].str.upper()
    tem = []
    for temp in ifsc:
        print(temp)
        url = "http://api.techm.co.in/api/v1/ifsc/" + temp
        datap1 = requests.get(url)
        datap1 = datap1.json()
        try:
            c = datap1['data']['BANK']

        except KeyError:
            c = "NOTFOUND"

        print(c)
        tem.append(c)
    print(tem)
    print(ifsc)
    df3 = pd.DataFrame(list(map(list, zip(ifsc, bankname, tem))))
    sher = "sheet"+str(i)
    df3.to_excel(writer,sher)
    writer.save()
    print("output saved as  output.xlsx")
