import pandas as pd

archivo = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv"
df = pd.read_csv(archivo, sep=';')



class CargarDatos:
    url = ""
    nombre = ""

    def __init__(self, url, nombre):
        self.url = url 
        self.nombre = nombre
        


    def calcularPromedio(self):
        pass 

    def calcularSuma(self):
        pass 

