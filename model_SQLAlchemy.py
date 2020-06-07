import re
from datetime import datetime
# Import create_engine, MetaData
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
#https://docs.sqlalchemy.org/en/13/orm/tutorial.html

################################################################################
################# Declare a Mapping ##########################################
###############################################################################

metadata = MetaData()
Base = declarative_base()

# Declaro la Tabla 
class Producto(Base):

    __tablename__ = 'producto_1'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(500))
    descripcion = Column(String(500))
    fecha = Column(DateTime(timezone=True), default=func.now())

#################################################################################
################# Connecting  to  MYSQL ###################################################
################################################################################
# https://docs.sqlalchemy.org/en/13/dialects/mysql.html

def  create_session():
    USR = 'root'
    PWD = ''
    DataBase = 'SQLAlchemy'
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(USR, PWD, DataBase))
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return DBSession()


from sqlalchemy_utils import database_exists, create_database





#########################################################################
###########  Creating Session ##########################################
##########################################################################

#https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_tutorial.pdf

class Modelo():
    
    #Session = sessionmaker(bind=engine)
    #session = Session()


    def create_db(self):
        # USR = 'root'
        # PWD = ''
        engine = create_engine('mysql://root:@localhost:3306/prueba_6')
        if not database_exists(engine.url):
            create_database(engine.url)
        print(database_exists(engine.url))


    session= create_session()

###################################################################
##########  Alta de Registros - Adding Objects ###################
######################################################################

    def alta_db(self, titulo_entry, descripcion_entry):
        new_product = Producto( titulo = titulo_entry,
                                descripcion = descripcion_entry )
        self.session.add(new_product)
        self.session.commit()

    #funcion validar e insertar
    def validar_insertar(self, e_titulo_var, e_descripcion_var):
        if e_titulo_var == '' or e_descripcion_var == '':
            return 'sin_datos'
        if self.validar(e_titulo_var):
            self.alta_db(e_titulo_var, e_descripcion_var)
            return 'alta_ok'
        else:
            return 'validacion_erronea'

##################################################################### 
######################### Listar  #####################################
#####################################################################  
   
    def list_bd(self):
        result = self.session.query(Producto).all()
        return result

##################################################################### 
######################### Buscar  ####################################
##################################################################### 

    def buscar(self, pk):
        resultado = self.session.query(Producto).get(pk)
        return resultado

##################################################################### 
######################### Baja  #####################################
#####################################################################  

    def baja_db(self, pk):
        x = self.session.query(Producto).get(pk)
        print(x)
        self.session.delete(x)
        self.session.commit()

#################################################################
############ Updating Object ###################################
##################################################
    
    def modificar_db(self, pk, titulo_entry, descripcion_entry ):
        #session.Producto.update().where(Producto.id == pk).values( titulo =titulo_entry, descripcion = descripcion_entry )
        self.session.query(Producto).filter(Producto.id == pk).update({'titulo' : titulo_entry, 'descripcion' :descripcion_entry })
        self.session.commit()


    def validar_modificar(self, pk, tit, descri):
        if tit == '' or descri == '' or pk == '':
            return 'sin_datos'
        elif self.validar(tit):
            self.modificar_db( pk, tit, descri)
            return 'modificacion_ok'
        else:
            return 'validacion_erronea'


    ##########################################################
    ################ Validaciones al Formulario ##############
    #########################################################
    
    # valido el titulo
    def validar(self, atributo):
        patron = "^[A-Za-z]+(?:[ -][A-Za-z]+)*$"
        if re.fullmatch(patron, atributo):
            return True
        
 
    def verificar_campos_completos(self,  titulo, descripcion):
        if  titulo == '' or descripcion == '':
            return 'sin_datos'

#productos = Crud()
#productos.baja_db(2)

