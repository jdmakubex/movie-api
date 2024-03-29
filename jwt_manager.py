#Importamos la librería que instalamos previamente con: pip install pyjwt
from jwt import encode
from jwt import decode
#Creamos una función que recibe como parámetro un diccionario
def create_token(data: dict):
    #procesamos el método encode, pasandole parametros
    # en payload, cargamos los datos que vienen en el diccionario como argumento
    # en key la llave para decodificar
    # y el tipo de algoritmo de codificación
    token: str= encode(payload=data,key="my_secrete_key",algorithm="HS256")
    return token

#Función para valida token, donde recibimos el token 
def validate_token(token: str)->dict:
    #procesamos el token que recibimos, nos ayudamos de la clave secreta y el algoritmo de decodificacion
    data: dict = decode(token,key="my_secrete_key", algorithms=['HS256'])
    return data