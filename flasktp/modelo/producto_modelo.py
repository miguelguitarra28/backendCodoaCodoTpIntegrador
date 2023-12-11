from app import app, db   #,ma




class Producto(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    imagen=db.Column(db.String(400))
    marca=db.Column(db.String(100))
    categoria=db.Column(db.String(50))
    def __init__(self,nombre,precio,stock,imagen,marca,categoria):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.stock=stock
        self.imagen=imagen
        self.marca=marca
        self.categoria=categoria




    #  si hay que crear mas tablas , se hace aqui




with app.app_context():
    db.create_all()