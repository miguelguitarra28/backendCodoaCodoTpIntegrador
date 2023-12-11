from app import app, db



class Contacto(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    correo=db.Column(db.VARCHAR (100))
    mensaje=db.Column(db.String(100))
    
    def __init__(self,nombre,correo,mensaje):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.correo=correo
        self.mensaje=mensaje



with app.app_context():
    db.create_all()        