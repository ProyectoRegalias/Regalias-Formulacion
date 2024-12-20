from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.router.Usuario import usuario
from app.router.arbol_problema import arbol_problema
from app.router.arbol_objetivo import arbol_objetivo
from app.router.chat import chat, chat_ia
import key
import google.generativeai as genai

db = SQLAlchemy()
genai.configure(api_key=key.clave)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://uo8anz1qxxd08ucp:638cBXuoPtaleuf6Gp96@localhost:5000'
                                             '/bsq8dwiuljmfpdmfeygi')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.secret_key = 'mondongo'

    # Registro de los blueprints
    app.register_blueprint(usuario)
    app.register_blueprint(chat_ia)
    app.register_blueprint(arbol_problema)
    app.register_blueprint(arbol_objetivo)

    return app
