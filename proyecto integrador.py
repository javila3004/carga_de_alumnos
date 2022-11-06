import tkinter as tk

def verificar(dato):
    if dato=="":
        dato=="Error"

    return dato

def convertir(dato):
    if dato.isdecimal():
        dato=int(dato)
    else:
        dato="error"
    return dato


def verlista():
    for clave in alumnos:
        print(clave+": ",alumnos[clave])

def agregar_ala_lista():
    nombre=caja_Nombre.get()
    nombre=verificar(nombre)
    cursos=caja_Cursos.get()
    cursos=convertir(cursos)
    if nombre=="error":
        print("Error nombre vacio")

    elif cursos=="error":
        print("El ingreso de cursos solo puede ser numerico")
    else:
        alumnos[nombre] = cursos
        print("!El alumno fue añadido correctamente!")

def ver_cand_alumnos():
    cand_cursos=caja_Nombre.get()
    cand_cursos=verificar(cand_cursos)
    for clave in alumnos:
        if cand_cursos==clave:
            print("La cantidad de cursos de "+cand_cursos + " es: ",alumnos[clave])


### programa principal
alumnos={}
ventana=tk.Tk()
ventana.title("Proyecto integrador")
ventana.config(width=400,height=300)


ver_lista=tk.Button(text="Ver lista de alumnos ",command=verlista)
ver_lista.place(x=10,y=10)


etiqueta_Nombre=tk.Label(text="Nombre del alumno:")
etiqueta_Nombre.place(x=10,y=60)

caja_Nombre=tk.Entry()
caja_Nombre.place(x=130,y=60)

etiqueta_cursos=tk.Label(text="Cursos: ")
etiqueta_cursos.place(x=10,y=100)

caja_Cursos=tk.Entry()
caja_Cursos.place(x=130,y=100,width=60 )


agregar_Lista=tk.Button(text="Agregar a la lista",command=agregar_ala_lista)
agregar_Lista.place(x=10,y=140)

candti_cursos=tk.Button(text=" Ver la cantidad de cursos",command=ver_cand_alumnos)
candti_cursos.place(x=130,y=140)


ventana.mainloop()

