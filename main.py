import pandas as pd
from data.platos import platosPopulares
from helpers.crearTabla import crearTabla

from data.Reservas import reservas

from data.proveedores import Proveedores

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos, "tablaplatospopulares")

tablaReservas=pd.DataFrame(reservas)
print(reservas)
#crearTabla(tablaReservas, "tablareservas")

tablaProveedores=pd.DataFrame(proveedores)
print(proveedores)
#crearTabla(tablaProveedores, "tablaproveedores")

