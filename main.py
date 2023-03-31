from fastapi import FastAPI
#Importamos HTMLResponse para poder devolver HTML como respuesta
from fastapi.responses import HTMLResponse

#Para el ejemplo del metodo POST, se agrega la libería Body, para pasar en el body los parametros
from fastapi import Body

app = FastAPI()
#Para agregar el título de la página
app.title = "Mi aplicación con FastApi"
#Para cambiar la versión
app.version = "0.0.1"

#Creamos una variable llamada movies, tipo lista 
#Ahora se aumenta un elemento a la colección para ejemplificar 
movies = [
    {
        "id" : 1,
        "title" : "Avatar 1",
        "overview" : "En un exuberante planeta llado Pandora viven los Na'vi, seres que ...",
        "year" : 2009,
        "rating" : 7.8,
        "category" : "Accion"
    },
    {
        "id" : 2,
        "title" : "Avatar 2",
        "overview" : "En un exuberante planeta llado Pandora viven los Na'vi, seres que ...",
        "year" : 2009,
        "rating" : 7.8,
        "category" : "Accion"
    }
]

#Para cambiar agregar etiquetas para añadir mas rutas
@app.get("/",tags=['home'])
def read_root():
    #return {"Hello" : "World!"}
    return HTMLResponse('<h1>Hello World</h1>')

#Creamos una nueva ruta que se llamará movies
@app.get('/movies', tags=['movies'])
def get_movies():
    #Aquí retornamos el listado contenido en la variable movies.
    return [item for item in movies]

#Con esta ruta se hace el ejemplo de parametros con ruta
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id : int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

#Ejemplo Parámetros Query
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category :str, year: int):
    for item in movies:
            #Esta es una forma de listar y retornar todos los elementos
            return [item for item in movies if item['category'] == category and item['year'] == year]
    return []

#Ejemplo Parámetros Método POST
@app.post('/movies/',tags=['movies'])
def create_movie(id :int = Body() ,title : str = Body(), overview : str = Body(), year : int = Body(), rating : float = Body(), category : str = Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview":overview,
        "year":year,
        "rating":rating,
        "category":category
    })
    return title

#Ejemplo put
@app.put('/movies/{id}', tags=['movies'])
#Ojo el id, no se requiere como body
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return [item for item in movies]

#Ejemplo delete
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return [item for item in movies]
