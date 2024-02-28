import pandas as pd
import json

newJSON = "libraries-and-books.json"
readJSON = "secure-users.json"
excel = "28-febrero-libros-prestados.xlsx"



# leemos el json
with open(readJSON, "r") as fileJSON:
    data = json.load(fileJSON)


# crear el json
with open(newJSON, "w") as fileJSON:
    fileJSON.write("[]")
new_json_datos = []

new_json = []
for pos in data:
    for data_book in pos["books"]:
        new_json_datos.append({"ID_Libro":data_book["bookId"],
                        "Titulo": data_book["bookTitle"],
                        "Editorial": data_book["bookEditorial"],
                        "Anio_de_publicacion": data_book["bookPublication"]})


for pos in range(0, len(data)):
    new_json_datos[pos]["ID_Usuario"] = data[pos]["userId"]
    new_json_datos[pos]["Nombre_completo"] = data[pos]["userName"]

print(data[1]["userName"])
for pos in new_json_datos:
    new_json.append({"libraryId": data_book["libraryId"],
                     "books": [pos]})
        # print(data_book["libraryId"])

# Escribimos en el json
with open(newJSON, "w") as fileJSON:
    json.dump(new_json, fileJSON, indent=1)

print(new_json)
df = pd.DataFrame(new_json_datos)
df.index.name = 'ID'
df.to_excel(excel)
