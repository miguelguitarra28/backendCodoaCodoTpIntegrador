from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from modelo.contacto_modelo import *


class ContactoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','correo','mensaje')




contacto_schema=ContactoSchema()            # El objeto producto_schema es para traer un producto
contactos_schema=ContactoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


@app.route('/contactos',methods=['GET'])
def get_Contactos():
    all_contactos=Contacto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=contactos_schema.dump(all_contactos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)


@app.route('/contactos/<id>',methods=['GET'])
def get_contacto(id):
    contacto=Contacto.query.get(id)
    return contacto_schema.jsonify(contacto)


@app.route('/contactos/<id>',methods=['DELETE'])
def delete_contacto(id):
    contacto=Contacto.query.get(id)
    db.session.delete(contacto)
    db.session.commit()                     # confirma el delete
    return contacto_schema.jsonify(contacto)







@app.route('/contactos/<id>' ,methods=['PUT'])
def update_contacto(id):
    contacto=Contacto.query.get(id)
 
    contacto.nombre=request.json['nombre']
    contacto.correo=request.json['correo']
    contacto.mensaje=request.json['mensaje']
    


    db.session.commit()    # confirma el cambio
    return contacto_schema.jsonify(contacto)    # y retorna un json con el producto











@app.route('/contactos', methods=['POST']) # crea ruta o endpoint
def create_contacto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    correo=request.json['correo']
    mensaje=request.json['mensaje']
    new_contacto=Contacto(nombre,correo,mensaje)
    db.session.add(new_contacto)
    db.session.commit() # confirma el alta
    return contacto_schema.jsonify(new_contacto)
        