# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
op = search.GPSProblem('O', 'P', search.romania)
lu = search.GPSProblem('L', 'U', search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

print("Pruebas de Busqueda de  Ramificación y acotación sin Subestimación")
print(search.ramificacion_y_acotacion(ab).path())
print("Pruebas de Busqueda de  Ramificación y acotación con Subestimación")
print(search.ramificacion_y_acotacion_con_subestimacion(ab).path())
print("Pruebas de Busqueda de  Ramificación y acotación sin Subestimación")
print(search.ramificacion_y_acotacion(op).path())
print("Pruebas de Busqueda de  Ramificación y acotación con Subestimación")
print(search.ramificacion_y_acotacion_con_subestimacion(op).path())
print("Pruebas de Busqueda de  Ramificación y acotación sin Subestimación")
print(search.ramificacion_y_acotacion(lu).path())
print("Pruebas de Busqueda de  Ramificación y acotación con Subestimación")
print(search.ramificacion_y_acotacion_con_subestimacion(lu).path())


