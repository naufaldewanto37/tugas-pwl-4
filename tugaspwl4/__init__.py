from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_jwt.policy import JWTAuthenticationPolicy
import pymysql

def db_connect():
    return pymysql.connect(host='localhost', user='root', password='', db='pyramidtest')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    
    authn_policy = JWTAuthenticationPolicy('qwert123', http_header='Authorization')
    authz_policy = ACLAuthorizationPolicy()
    
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.add_route('hello', '/hello')
    config.add_route('movies', '/movies')
    config.add_route('update_movie', '/movies/{id}', request_method='PUT')
    config.add_route('delete_movie', '/movies/{id}', request_method='DELETE')
    config.scan('.views')
    return config.make_wsgi_app()
