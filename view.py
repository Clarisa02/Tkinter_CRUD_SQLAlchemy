"""

"""
# a View handles the frontend presentation 

import tkinter as tk 
from tkinter import ttk
from tkinter import  *
from tkinter.messagebox import showinfo, showerror


class CrudAppView():
    
    def __init__(self, root):
        
        #tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.wm_title(self, "CRUD App")

        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.root = root
        self.root.title("App CRUD") 
        self.root.geometry("700x600")
        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.Contenedor = Frame(self.root, bg="#444")   #container = tk.Frame(self)
        self.Contenedor.pack(expand=YES, fill=BOTH)         #container.pack(side="top", fill="both", expand=True)
        self.Contenedor.grid_rowconfigure(1000, weight=1)
        self.Contenedor.grid_columnconfigure(1000, weight=1)
        # ##################################################################
        # ##################################################################
        # Agrego Secciones Principales
        # ##################################################################
        #####  Titulo y Botones Div Superior #####
    
        self.div_superior = Frame(self.Contenedor)
        self.div_superior.pack()
        
        ######### div Superior ####################  
        # defino las variables a utilizar
        self.e_id_var = StringVar()
        self.e_titulo_var = StringVar()
        self.e_descripcion_var = StringVar() 
        self.e_tema_opcion_var = IntVar(value=0)

        #labels
        #Titulo
        label_titulo_form = Label(self.div_superior, text="Ingrese sus datos", bg='purple', fg="white" ,width=88)
        label_titulo_form = label_titulo_form.grid(row = 0, column=0, columnspan=12, sticky=W+E+N+S)


        label_explicacion = Label(self.div_superior, wraplength=600,
                                text="Funciones: " +
                                "BUSCAR POR ID: Podra buscar los registros cargados indicando el ID" +
                                " y pulsando el Boton Buscar por ID",
                        
                                 bg='blue', fg="white" , width=88)
        label_explicacion  = label_explicacion.grid(row = 5, column=0, columnspan=12, sticky=W)

        #id
        label_id = Label(self.div_superior, text= 'ID')
        label_id = label_id.grid(row= 20, column= 0, sticky= W)

        self.e_id = Entry(self.div_superior, textvariable=self.e_id_var , width = 20, state='disabled')
        self.e_id.grid( row=20, column=1, padx = 10) 

        #titulo 
        label_titulo = Label(self.div_superior, text="Titulo")
        label_titulo = label_titulo.grid(row = 30, column=0,  sticky = W)

        self.e_titulo = Entry(self.div_superior, textvariable=self.e_titulo_var , width = 20)
        self.e_titulo.grid( row=30, column=1, padx = 10)

        #Descripción 
        label_descripcion = Label(self.div_superior, text="Descripción")
        label_descripcion.grid(row = 40, column=0,  sticky = W)

        self.e_descripcion = Entry(self.div_superior, textvariable= self.e_descripcion_var , width = 20)
        self.e_descripcion.grid( row=40, column=1, padx = 10)
       
        #Botones
        self.btn_habilitar_buscar = Button(self.div_superior, text="Habilitar Búsqueda por ID", command= '')
        self.btn_habilitar_buscar.grid(row=20, column=2, padx=10, pady=10, sticky=W+E+N+S ) #

        self.btn_buscar = Button(self.div_superior, text="Buscar por ID", command= '')
        self.btn_buscar.grid(row=20, column=3 , padx=10, pady=10, sticky=W+E+N+S ) # )

        self.btn_deshabilitar_buscar = Button(self.div_superior, text="Habilitar Alta", command= '')
        self.btn_deshabilitar_buscar.grid(row=20, column=5, padx=10, pady=10, sticky=W+E+N+S ) 

        self.btn_creardb= Button(self.div_superior, text="Crear bd", command= '')
        self.btn_creardb.grid(row=45, column=0, padx=20, pady=10  )

        self.btn_mostrar = Button(self.div_superior, text="Mostrar registros existentes", command='')
        self.btn_mostrar.grid( row=45, column=2, columnspan=1,  padx=20,  pady=10, sticky=W+E+N+S)
        
        #Botones
        self.btn_alta = Button(self.div_superior, text="Alta", command= '' )
        self.btn_alta.grid(row=30, column=2, columnspan= 2, padx=10, pady=2, sticky=W+E+N+S  )
        self.btn_baja = Button(self.div_superior, text="Baja", command= '' )
        self.btn_baja.grid(row=40, column=2, columnspan= 2, padx=10, pady=2, sticky=W+E+N+S )

        self.btn_modificar = Button(self.div_superior, text="Modificar", command= '' )
        self.btn_modificar.grid(row=30, column=5, rowspan= 15, padx=10, pady=2, sticky=W+E+N+S  )
        #####  Div Central - TREE VIEW #####
        self.div_central = Frame(self.Contenedor)
        self.div_central.pack()
        self.create_tree_view()

        #####  TEMAS #####
        self.div_inferior = Frame(self.Contenedor)
        self.div_inferior.pack()
        
        #####  Show Info ###########
        #self.msj_show_info()

#https://github.com/PacktPublishing/Tkinter-GUI-Application-Development-Blueprints-Second-Edition/blob/master/Chapter%2009/9.11_phonebook.py
    def create_tree_view(self):
        self.tree = ttk.Treeview(self.div_central, height=10, columns=[ '#1', '#2', '#3'])
        self.tree.grid(row = 20, column= 1, columnspan=2)
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Titulo')
        self.tree.heading('#2', text='Descripción')
        self.tree.heading('#3', text='Fecha')
        
    def insert_tree_view(self, data_list):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        if data_list != []:
            for row in data_list:
                self.tree.insert('', 'end', text=row.id,  values = (row.titulo, row.descripcion, row.fecha) )


###############################################################################
#################  Mensajes de confirmacion y Error ###########################
################ para los diferentes Botones     ###########################
###############################################################################
    def msj_show(self, motivo_msj):
        #btn_alta
        if motivo_msj == 'alta_ok':
            showinfo("Información importante", 
            "El registro ha sido agregado a la base de datos")
        elif motivo_msj == 'validacion_erronea':
            showerror("Error",
            "El titulo debe comenzar con una letra en mayuscula o minuscala." +
            "A su vez, solamente puede tener espacios, guión bajos o medios.") 
        elif motivo_msj == 'sin_datos': # se repite el mensaje para moficicar
            showerror("Error",
            "Debe ingresar un valor para cada uno de los datos solicitados.")
        #btn Crear db
        elif motivo_msj == 'db_ya_existe':
            showerror("Información importante",
                    "La base y la tabla ya existen!")
        elif motivo_msj == 'db_creada':
            showinfo("Información importante",
            "La base y la tabla han sido creadas correctamente")
        #btn Buscar id 
        elif motivo_msj == '':
            showerror("Información importante",
            "Debe ingresar un ID para realizar la búsqueda, baja o modificación de un registro.")
        #btn Buscar id
        elif motivo_msj == []:
            showerror("Información importante",
            "No se han encontrado datos")
        #btn_mostrar
        elif motivo_msj == 'sin_registros':
            showinfo("Mensaje", 
                       "La base de datos aún no tiene registros")
        # btn_modificar
        elif motivo_msj == 'modificacion_ok':
            showinfo("Mensaje", 
                    "Los datos se han modificado correctamente.")
        # btn_baja
        elif motivo_msj == 'baja_ok':
            showinfo("Mensaje", 
                    "Se ha realizado la baja del registro indicado.")
       

    def limpiar_id(self):
        self.e_id_var.set("")

    def limpiar_registros(self ):
        self.e_titulo_var.set("")
        self.e_descripcion_var.set("")


    def cargar_resultado_search(self, datos):
        self.e_titulo_var.set(datos.titulo)
        self.e_descripcion_var.set(datos.descripcion)

    def edicion_campos(self, estado_id, estado_otros_campos):
        self.e_id.config(state= estado_id ) 
        self.e_descripcion.config(state= estado_otros_campos ) 
        self.e_titulo.config(state= estado_otros_campos) 
         # 'disabled')
        



if __name__ == '__main__':
    root = Tk()
    #desde fuera de la clase creo un objeto de la clase
    #previamente habia generado la ventana y se la paso como parametro a la clase
    MiApp = CrudAppView(root)
    root.mainloop()
