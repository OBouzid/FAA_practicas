import numpy as np


class Datos(object):

    TiposDeAtributos = ('Continuo', 'Nominal')
    tipoAtributos = []
    nombreAtributos = []
    nominalAtributos = []
    datos = np.array(())
    # Lista de diccionarios. Uno por cada atributo.
    diccionarios = []
    # TODO: procesar el fichero para asignar correctamente las variables
    #  tipoAtributos, nombreAtributos,nominalAtributos, datos y diccionarios

    def __init__(self, nombreFichero):
        with open(nombreFichero, 'r') as f:
            nDatos =    int(f.readline().strip('\n'))
            



    # TODO: implementar en la pr�ctica 1

    def extraeDatosTrain(idx):
        pass

    def extraeDatosTest(idx):
        pass
