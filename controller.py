
#the model and the view never interact directly
#Cada vez que la vista requiere acceder backend data, its request the controller
#to intervene with the model and fetch the required data

from tkinter import *
#from model import Model
from model_SQLAlchemy import Modelo, create_session
from view import CrudAppView

class Controller():

    def __init__(self, root):

        self.root = root
        self.view = CrudAppView(root)
        self.model_sqlAlchemy = Modelo()
        
        self.view.btn_mostrar.config(command=self.mostrar_db)
        self.view.btn_alta.config(command=self.alta)
        self.view.btn_creardb.config(command=self.crear_base)
        self.view.btn_buscar.config(command=self.search)
        self.view.btn_modificar.config(command=self.modificar)
        self.view.btn_baja.config(command =self.baja)
        self.view.btn_habilitar_buscar.config(command=self.habilitar_busqueda)
        self.view.btn_deshabilitar_buscar.config()

    def mostrar_db(self):
        resultado_list_db = self.model_sqlAlchemy.list_bd()
        #if resultado_list_db == []:
        #    self.view.msj_show(resultado_list_db)
        #else:       
        #   self.view.insert_tree_view(resultado_list_db)
        self.view.insert_tree_view(resultado_list_db)
         

    def alta(self):
        #ver si el get va acá o donde deberia
        resultado_validar_insertar = self.model_sqlAlchemy.validar_insertar(self.view.e_titulo_var.get(), self.view.e_descripcion_var.get())
        self.view.msj_show(resultado_validar_insertar)
        self.view.limpiar_registros()
        #self.model_sqlAlchemy.alta_db(self.view.e_titulo_var.get(), self.view.e_descripcion_var.get())
        self.mostrar_db()

    def crear_base(self):
        resultado = self.model_sqlAlchemy.create_db()
        self.view.msj_show(resultado)

        
    def search(self):
        #pk = self.view.e_id_var.get()
        pk = self.view.tree.item(self.view.tree.focus())
        print(pk)
        registro_encontrado = self.model_sqlAlchemy.buscar(self.view.e_id_var.get())
        #print('encontrado' + str(registro_encontrado))
        if pk == '' or registro_encontrado == []:
            self.view.limpiar_registros()
            self.view.limpiar_id()
            self.view.btn_alta.config(state='normal')
            if pk == '':
                self.view.msj_show(pk)
            elif registro_encontrado == []:
                self.view.msj_show(registro_encontrado)   
        else:         
        #si encontro algo   
            self.view.cargar_resultado_search(registro_encontrado)
        self.view.edicion_campos('disabled', 'normal')
        self.view.btn_baja.config(state='normal')
        self.view.btn_modificar.config(state='normal')



    def modificar(self):
        #dobleclick = self.view.tree.item(self.view.tree.MouseDoubleClic())
        #print(dobleclick)
        #idselected = self.view.tree.item(self.view.tree.focus())
        #print(idselected)
        resultado_validar_modificar = self.model_sqlAlchemy.validar_modificar(self.view.e_id_var.get(), 
                                                                self.view.e_titulo_var.get(), 
                                                                self.view.e_descripcion_var.get())
        self.view.msj_show(resultado_validar_modificar)
        self.view.limpiar_registros()
        self.mostrar_db()

    def baja(self):
        pk = self.view.e_id_var.get()
        if pk == '':
            self.view.msj_show(pk)
        else:
            self.model_sqlAlchemy.baja_db(self.view.e_id_var.get())
            self.view.msj_show('baja_ok')
            self.view.limpiar_id()
            self.mostrar_db()
        self.view.limpiar_registros()
        

    def habilitar_busqueda(self):
        self.view.limpiar_id()
        self.view.limpiar_registros()
        self.view.edicion_campos('normal', 'disabled')
        #deshabilitar alta - baja - modificación
        self.view.btn_alta.config(state='disabled')
        self.view.btn_baja.config(state='disabled')
        self.view.btn_modificar.config(state='disabled')

    # def habilitar_alta(self):
    #     self.view.limpiar_id()
    #     self.view.limpiar_registros()
    #     self.view.edicion_campos('disabled', 'normal')
    #     self.view.btn_alta.config(state='normal')
    #     self.view.btn_baja.config(state='disabled')
    #     self.view.btn_modificar.config(state='disabled')



if __name__ == '__main__':
    root = Tk()
    app = Controller(root)
    app.mostrar_db() 
    root.mainloop()


