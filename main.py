from fastapi import FastAPI
#Importamos HTMLResponse para poder devolver HTML como respuesta
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

#Para el ejemplo del metodo POST, se agrega la libería Body, para pasar en el body los parametros
from fastapi import Body

app = FastAPI()
#Para agregar el título de la página
app.title = "Mi aplicación con FastApi"
#Para cambiar la versión
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category:str


#Creamos una variable llamada movies, tipo lista 
#Ahora se aumenta un elemento a la colección para ejemplificar 
movies = [
    {
        "id" : 1,
        "title" : "Avatar 1",
        "overview" : "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year" : 2009,
        "rating" : 7.8,
        "category" : "Accion"
    },
    {
        "id" : 2,
        "title" : "Avatar 2",
        "overview" : "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
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
'''
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
'''
#Ejemplo Parámetros Método POST con esquemas
@app.post('/movies/',tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

'''
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
'''

#Ejemplo put con esquemas
@app.put('/movies/{id}', tags=['movies'])
#Ojo el id, no se requiere como body
def update_movie(id: int, movie: Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return [item for item in movies]


#Ejemplo delete
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return [item for item in movies]
