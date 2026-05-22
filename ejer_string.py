1. # crear un programa que busque en el pensamiento de cesar acuñas la palbra politicos.
# hay politicos que no hacen nada por que nunca han hecho nada
# y mostrarlo por terminal si lo encuentra

pensamiento_uno:str="hay politicos que no hacen nada por que nunca han hecho nada"
palabra_buscar="politicos"
print ("politicos" if pensamiento_uno.find(palabra_buscar)>0 else "texto no encontrado")

2. # crear un programa que en el siguente texto 'yo ya no vivo en trujillo, yo vivo en en peru' busque peru y lo remplace por narnia finalmente mostrarlo por terminal.

pensamiento_dos:str='yo ya no vivo en trujillo, yo vivo en en peru'
print(pensamiento_dos)
print(pensamiento_dos.replace("peru","narnia"))