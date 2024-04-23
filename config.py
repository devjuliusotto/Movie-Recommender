import os

class Config:
    """Configurações gerais do aplicativo."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdasd234234'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
