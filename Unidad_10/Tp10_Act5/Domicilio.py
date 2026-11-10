from Barrio import Barrio
from Habitacion import Habitacion
from Vivienda import Vivienda

hab1 = Habitacion("Cocina", 12.0)
hab2 = Habitacion("Dormitorio Principal", 15.0)
hab3 = Habitacion("Comedor", 20.0)

casa1 = Vivienda("San Martin", 123, "A", 1, 200.0)
casa2 = Vivienda("Belgrano", 456, "A", 2, 150.0)

casa1.habitacion.append(hab1)
casa1.habitacion.append(hab2)
casa2.habitacion.append(hab3)

mi_barrio = Barrio("Los Pinos", "Constructora SA")

mi_barrio.vivienda.append(casa1)
mi_barrio.vivienda.append(casa2)

print(" RESULTADOS DEL BARRIO")
print(f"Superficie total de terreno: {mi_barrio.getSuperficieTotalTerreno()}")
print(f"Superficie de terreno en Manzana A: {mi_barrio.getSuperficieTotalTerrenoXManzana('A')}")
print(f"Superficie total cubierta del barrio: {mi_barrio.getSuperficieTotalCubierta()}")