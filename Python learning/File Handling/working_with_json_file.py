data ={
    "name":"vicky",
    "mail_id":"vicky@gamil.com",
    "phone_number":343989045,
    "subject":["HTML","CSS","React","Angular","JavaScript","Node","Python","Data Science"]
}

# import json
# f = open("data.json","w")
# json.dump(data,f)
# f.close()

# f = open("data.json","r")
# file_data = json.load(f)
# print(file_data)
# f.close()
import csv
data = [["name","email","phone_number"],
        ["vicky","vicky@gmail.com",916612],
        ["ritik","ritik@gmail.com",70232],
        ["priyanka","priyanka@gmail.com",7878]
        ]
with open('data.csv',"w") as d:
    writer = csv.writer(d)

    for i in data:
        writer.writerow(i)

with open("data.csv",'r') as f:
    read_data = csv.reader(f)
    for i in read_data:
        print(i)

