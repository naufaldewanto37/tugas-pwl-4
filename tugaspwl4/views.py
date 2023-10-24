import jwt
from datetime import datetime, timedelta
from pyramid.view import view_config
from pyramid.response import Response
from passlib.hash import pbkdf2_sha256
from pyramid.httpexceptions import HTTPNotFound

# Simulated Database
USERS = {}

@view_config(route_name='register', renderer='json', request_method='POST')
def register(request):
    username = request.json_body.get('username')
    password = request.json_body.get('password')
    
    if not username or not password:
        return Response('Missing username or password', status=400)
        
    if username in USERS:
        return Response('User already exists', status=400)
    
    hashed = pbkdf2_sha256.hash(password)
    USERS[username] = hashed
    
    return {'status': 'User registered'}

@view_config(route_name='login', renderer='json', request_method='POST')
def login(request):
    username = request.json_body.get('username')
    password = request.json_body.get('password')
    
    if not username or not password:
        return Response('Missing username or password', status=400)
        
    hashed = USERS.get(username)
    
    if not hashed or not pbkdf2_sha256.verify(password, hashed):
        return Response('Wrong credentials', status=400)

    # Create token
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {"username": username, "exp": expiration}
    token = jwt.encode(payload, "qwert123", algorithm="HS256")
    
    return {'token': token}

@view_config(route_name='hello', renderer='string')
def hello_world(request):
    return "Hello, World!"

MOVIES = [
    {'id': 1, 'title': 'Inception', 'year': 2010},
    {'id': 2, 'title': 'The Matrix', 'year': 1999},
    {'id': 3, 'title': 'Avengers: Endgame', 'year': 2019},
    {'id': 4, 'title': 'The Godfather', 'year': 1972},
    {'id': 5, 'title': 'The Dark Knight', 'year': 2008},
    {'id': 6, 'title': 'Forrest Gump', 'year': 1994},
    {'id': 7, 'title': 'Fight Club', 'year': 1999},
    {'id': 8, 'title': 'Pulp Fiction', 'year': 1994},
    {'id': 9, 'title': 'Shawshank Redemption', 'year': 1994},
    {'id': 10, 'title': 'Interstellar', 'year': 2014}
]

from tugaspwl4 import db_connect
@view_config(route_name='movies', renderer='json', request_method='POST')
def create_movie(request):
    title = request.json_body.get('title')
    year = request.json_body.get('year')
    
    conn = db_connect()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO movies (title, year) VALUES (%s, %s)", (title, year))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return {'status': 'Movie created'}

@view_config(route_name='movies', renderer='json', request_method='GET')
def read_movies(request):
    conn = db_connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * from movies")
    movies = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return {'movies': movies}

@view_config(route_name='update_movie', renderer='json', request_method='PUT')
def update_movie(request):
    movie_id = int(request.matchdict['id'])
    
    # Mendapatkan data yang akan diupdate dari body request
    title = request.json_body.get('title')
    year = request.json_body.get('year')
    
    if not title or not year:
        return Response('Missing title or year', status=400)

    conn = db_connect()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE movies SET title=%s, year=%s WHERE id=%s", (title, year, movie_id))
        conn.commit()

        # Memeriksa apakah ada baris yang diperbarui
        if cursor.rowcount == 0:
            return Response('No movie found with the provided id', status=404)

        updated_movie = {'id': movie_id, 'title': title, 'year': year}
        return {'status': 'Movie updated', 'movie': updated_movie}
    
    except Exception as e:
        return Response('Error updating movie: {}'.format(str(e)), status=500)
    
    finally:
        cursor.close()
        conn.close()


from pyramid.httpexceptions import HTTPNotFound

@view_config(route_name='delete_movie', renderer='json', request_method='DELETE')
def delete_movie(request):
    movie_id = int(request.matchdict['id'])

    conn = db_connect()
    cursor = conn.cursor()

    try:
        # Mengecek apakah ada film dengan id yang diberikan
        cursor.execute("SELECT * FROM movies WHERE id = %s", (movie_id,))
        movie = cursor.fetchone()

        if movie is None:
            raise HTTPNotFound()

        # Menghapus film berdasarkan id
        cursor.execute("DELETE FROM movies WHERE id = %s", (movie_id,))
        conn.commit()

        return {'status': 'Movie deleted', 'movie': movie}

    except HTTPNotFound:
        return Response('Movie not found', status=404)

    except Exception as e:
        return Response('Error deleting movie: {}'.format(str(e)), status=500)

    finally:
        cursor.close()
        conn.close()


