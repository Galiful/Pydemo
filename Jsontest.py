
import re
import json
from pandas import Series,DataFrame
import pandas as pd
import csv



pattern = re.compile('{\s+"header".*?]\s}',re.S)
filename = "2D.json"
savename = "C:/Users/Administrator/Desktop/file/"
def jsonParse(filename):
    with open(filename, 'r') as file:
        str = file.read()
        results = re.findall(pattern,str)
        for result in results:
            yield result
            
def saveTojson(data,savename):
    with open (savename+".json",'w') as f:
        f.write(data)

def saveTocsv(data,savename):
    for item in data: 
        df = pd.DataFrame(item)
        writer = pd.ExcelWriter(savename+item["id"]+".xlsx")
        df.to_excel(writer,sheet_name=item["id"])
        writer.save()
        writer.close()


def getItem():    
    for data in jsonParse(filename):
        # saveTojson(data,savename+str(i))
        newdata = json.loads(data)
        # print(newdata["object"])
        items = newdata["object"]
        for item in items:
            # print("="*20)
            # print (item)
            yield item

def main(data):
    for item in data: 
        with open(savename+item["id"]+'.csv', 'a') as csvfile:
            fieldnames = ['id', 'timestamp', 'position','size', 'velocity', 'objectClass']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(item)

    # writer = pd.ExcelWriter(savename+item["id"]+".xlsx")
    # df = pd.DataFrame(newdata["object"])
    # df.to_excel(writer,sheet_name=item["id"])
    # writer.save()
    # writer.close()
if __name__ == '__main__':     
    # main(getItem())
    saveTocsv(getItem(),savename)