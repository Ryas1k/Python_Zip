from zipfile import ZipFile
import json

l = []
with ZipFile("data.zip", mode="r") as zip_files:
    for i_json in zip_files.namelist():
      try:
        with zip_files.open(i_json, mode="r") as file:
          info1 = file.read()
          j_info1 = json.loads(info1)
          if j_info1["team"] == "Arsenal":
            l.append((j_info1["first_name"], j_info1["last_name"]))    
      except:
        continue

l.sort(key=lambda x: (x[0], x[1]))
for i in l:
    print(*i)
