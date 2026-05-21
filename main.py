from fastapi import FastAPI
from test import csv_vers_json
from database import connexion,curseur
from pydantic import BaseModel

app = FastAPI(description='pRemier')

@app.get("/convertir")
async def convertir_csv_json():

    csv_vers_json("eleves_valides.csv", "etudiants.json")

    return {
        "message": "Conversion CSV vers JSON réussie"
    }

# GET
@app.get("/")
async def accueil():
    return {"message": "GET"}

# POST
@app.post("/")
async def ajouter():
    return {"message": "POST"}

# PUT
@app.put("/")
async def modifier():
    return {"message": "PUT"}

# PATCH
@app.patch("/")
async def modifier_partiel():
    return {"message": "PATCH"}

# DELETE
@app.delete("/")
async def supprimer():
    return {"message": "DELETE"}





