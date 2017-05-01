dic = {'perro': 'ladra', 'gato': 'maulla'}

''' Obtener el valor de una clave '''
dic.get('perro') # ladra

''' Saber si una clave existe en el diccionario '''
'elefante' in dic # False

''' Obtener claves y valores '''
for clave, valor in dic.iteritems(): 
    print "El valor de la clave %s es %s" % (clave, valor)

''' Obtener las claves '''
dic.keys() # ['gato', 'perro']

''' Obtener los valores '''
dic.values() # ['maulla', 'ladra']

''' Obtener la cantidad de elementos '''
len(dic) # 2

''' Agregar un par clave-valor: '''
dic['gallina'] = 'cocotea'

''' Borrar un par clave-valor '''
del dic['gallina']

''' Imprimir de una forma legible en formato string '''
import json
print json.dumps(dic, indent=1)

# ---------------------------------------------------------

# Convertir diccionario en array de numpy
import numpy as np
result = {0: 1.1181753789488595, 1: 0.5566080288678394, 2: 0.4718269778030734, 3: 0.48716683119447185, 4: 1.0, 5: 0.1395076201641266, 6: 0.20941558441558442}

names = ['id','data']
formats = ['f8','f8']
dtype = dict(names = names, formats=formats)
array = np.array(result.items(), dtype=dtype)

print(repr(array))


# Otra forma
import numpy as np
result = {0: 1.1181753789488595, 1: 0.5566080288678394, 2: 0.4718269778030734, 3: 0.48716683119447185, 4: 1.0, 5: 0.1395076201641266, 6: 0.20941558441558442}

arrays = {'names': np.array(k.keys(), dtype=float),
          'values': np.array(k.values(), dtype=float)}
