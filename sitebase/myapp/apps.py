from django.apps import AppConfig
import joblib


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'


class FranchiseClassifier(AppConfig):
    load_model = joblib.load('/home/tpah20/model.pkl')
