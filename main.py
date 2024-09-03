import vdm

print('opcion - 1 ver grafica de barras')
print('opcion - 2 ver mapa de calor')
print('')
print('/////////////////////////////////////////')
print('')
op = int(input('ingrese una opicion:'))

if op == 1:
    vdm.draw_cat_plot()
if op == 2:
    vdm.draw_heat_map()

