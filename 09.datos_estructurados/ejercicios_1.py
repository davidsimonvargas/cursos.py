# crear una lista de 5 vertebrados y 5 invertebrados el orden debera ser aleatorio y tendras que hacer las siguientes correciones 
"""
1. modificar los 3 primeros elementos por aves
2. modificar el elemento 6 y ultimo elemnto por reptiles
3. modificar el elemento 8 por gianfranco
4. mostrar la lista nueva con las modificaciones
"""

animales:list[str]=['leon','zancudo','jaguar','zaltamontes','jabali','araña','perro','cangrejo','estrella de mar','aguila']
print(f"los animales son: {animales}")

animales[0]=['loro']
animales[1]=['gallina']
animales[2]=['pato']
animales[5:]=['cocodrilo','boa','piton','dragon de comodo','caiman negro','camaleon']
animales[7]=['gianfranco']

print(f"la lista modificada es: {animales}")