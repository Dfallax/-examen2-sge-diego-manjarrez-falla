import pandas as pd
import json
import hashlib

newJSON = "secure-users.json"
readJSON = "users.json"
# leemos el json
with open(readJSON, "r") as fileJSON:
    data = json.load(fileJSON)

# crear el json
with open(newJSON, "w") as fileJSON:
    fileJSON.write("[]")

for password in data:
    password["password"] = hashlib.sha256(password["password"].encode()).hexdigest()
    print(password["password"])

# Escribimos en el json
with open(newJSON, "w") as fileJSON:
    json.dump(data, fileJSON, indent=1)




#password = hashlib.sha256(password.encode()).hexdigest()