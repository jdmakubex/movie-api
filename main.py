from fastapi import FastAPI
#Importamos HTMLResponse para poder devolver HTML como respuesta y JSONResponse para Json
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from fastapi import Path
from fastapi import Query
from typing import List

#Para el ejemplo del metodo POST, se agrega la libería Body, para pasar en el body los parametros
from fastapi import Body

app = FastAPI()
#Para agregar el título de la página
app.title = "Mi aplicación con FastApi"
#Para cambiar la versión
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field (min_length=5, max_length=15)
    overview: str = Field (min_length=15, max_length=50)
    year: int = Field (default=2015 , le=2023)
    rating: float = Field (ge=1, le=10)
    category:str = Field (min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example":{
                    "id": 1,
                    "title": "Mi película",
                    "overview": "Descripción de la película",
                    "year": 2022,
                    "rating": 5,
                    "category": "Comedia"              
            }
        }


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
@app.get('/movies', tags=['movies'], response_model=list[Movie],status_code=200)
def get_movies() -> list[Movie]:
    #Aquí retornamos el listado contenido en la variable movies., respuesta tipo HTML
    #return [item for item in movies]
    #En ste ejemplo retornamos el listado como JSON
    return JSONResponse(status_code=200, content=movies)

#Con esta ruta se hace el ejemplo de parámetros con ruta
@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id : int = Path(ge=1, le=2000))-> Movie:
    for item in movies:
        if item["id"] == id:
            #return item, es para retornar respuesta como HMTL
            #return item
            #Este ejemplo es para retornar como JSON
            return JSONResponse (status_code=200, content=item)
    return JSONResponse (status_code=404, content= []) 

'''
#Ejemplo Parámetros Query
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category :str, year: int):
    for item in movies:
            #Esta es una forma de listar y retornar todos los elementos
            return [item for item in movies if item['category'] == category and item['year'] == year]
    return []
'''

#Ejemplo Parámetros Query  #Ejemplo de tipo de repuesta Lista
@app.get('/movies/', tags=['movies'],  response_model=list[Movie])
def get_movies_by_category(category :str =Query(min_length=5, max_length=15)) -> List[Movie]:
    for item in movies:
            #Esta es una forma de listar y retornar todos los elementos por HTML
            #return [item for item in movies if item['category'] == category]
            #ahora vamos a retornar el valor con JSON
            data = [item for item in movies if item['category'] == category]
            return JSONResponse(content=data)





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
@app.post('/movies/',tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    #return movies #Esto retornaba la respuesta como HTML
    return JSONResponse (status_code=201 ,content={"message":"se ha registrado la película"})

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
@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
#Ojo el id, no se requiere como body
def update_movie(id: int, movie: Movie) -> dict:
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse (content={"message":"se ha modificado la película"})


#Ejemplo delete    #Ejemplo de tipo de respuesta diccionario
@app.delete('/movies/{id}', tags=['movies'],  response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            #return [item for item in movies]
            return JSONResponse (status_code=200, content={"message":"se ha borrado la película"})
