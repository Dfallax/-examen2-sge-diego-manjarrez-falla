import pandas as pd
import json

excel = "usuarios.xlsx"
readJSON = "secure-users.json"

# leemos el json
with open(readJSON, "r") as fileJSON:
    data = json.load(fileJSON)


for books in data:
    del books["books"]


# hay qu epasarle los MAPA
df = pd.DataFrame(data)
df.index.name = 'ID'
df.to_excel(excel)
print(df)
