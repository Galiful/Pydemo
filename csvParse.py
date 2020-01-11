import re
import json
import csv
import os

pattern = re.compile('"id": "(.*?)".*?"timestamp": "(.*?)".*?"x": (.*?),.*?"y": (.*?),.*?"z": (.*?)\s.*?"x": (.*?),.*?"y": (.*?),.*?"z": (.*?)\s.*?"x": (.*?),.*?"y": (.*?),.*?"z": (.*?)\s.*?"objectClass": "(.*?)"',re.S)

filename = "C:/Users/Administrator/Documents/WXWork/1688853123380626/Cache/File/2019-12/1223af.txt"
savename = "C:/Users/Administrator/Desktop/file/"

def csvParse(filename):
    with open(filename, 'r') as file:
        str = file.read()
        # print (str)
        results = re.findall(pattern,str)
        for result in results:
            yield {
                'id':result[0],
                'timestamp':result[1]+'\t',
                'position_x':result[2],
                'position_y':result[3],
                'position_z':result[4],
                'size_x':result[5],
                'size_y':result[6],
                'size_z':result[7],
                'velocity_x':result[8],
                'velocity_y':result[9],
                'velocity_z':result[10],
                'objectClass':result[11]
            }

def saveTojson(data,savename):
    with open (savename+".json",'a') as f:
        f.write(json.dumps(data))

def saveTocsv(data):
    mode = 'a' if os.path.isfile(savename+data["id"]+'.csv') else 'w'
    with open(savename+data["id"]+'.csv', mode, newline='') as csvfile:
        fieldnames = ['id', 'timestamp', 'position_x','position_y', 'position_z', 'size_x','size_y','size_z','velocity_x','velocity_y','velocity_z','objectClass']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if mode=='w':
            writer.writeheader()
        writer.writerow(data)

if __name__ == '__main__':
    for data in csvParse(filename):
        print(data)
        # saveTojson(data,"1")
        saveTocsv(data)