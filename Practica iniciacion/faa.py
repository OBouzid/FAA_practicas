import numpy as np
import sys

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
            linesL=f.read().splitlines()
            con,nom = self.TiposDeAtributos
            self.nDatos = int(linesL[0])
            self.nombreAtributos = linesL[1].split(',')
            self.tipoAtributos = linesL[2].split(',')
            self.nominalAtributos = map(lambda x: True if x == nom else False, self.tipoAtributos)
            datosAux = np.array(map(lambda x:list(x.split(',')),linesL[3:]))
            i=0
            tam=len(self.nominalAtributos)
            while i<tam:
                if not self.nominalAtributos[i]:
                    self.diccionarios.append({})
                else:
                    auxC = set(datosAux[:,i])
                    j=0
                    dicAux={}
                    for x in sorted(auxC):
                        dicAux[x]=j
                        j+=1
                    self.diccionarios.append(dicAux)
                i+=1
            i=0
            self.datos=np.empty((self.nDatos,tam))
            while i<tam:
                if not self.nominalAtributos[i]:
                    self.datos[:,i]=datosAux[:,i]
                else:
                    dic=self.diccionarios[i]
                    j=0
                    while j<self.nDatos:
                        self.datos[j,i]=dic[datosAux[j,i]]
                        j+=1
                i+=1


            print self.nDatos
            print self.nombreAtributos
            print self.tipoAtributos
            print self.nominalAtributos
            print self.diccionarios
            print self.datos





    # TODO: implementar en la prctica 1

    def extraeDatosTrain(idx):
        pass

    def extraeDatosTest(idx):
        pass

if __name__ == '__main__':
    datos= Datos(sys.argv[1])