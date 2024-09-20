

from flask import Flask

from mongoengine import connect

def init_db(app: Flask):
    app.config['MONGODB_SETTINGS'] = {

     'host': 'mongodb+srv://nagvanshi:nagvanshi123@cluster0.82qda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    

    }
   
    connect(host=app.config['MONGODB_SETTINGS']['host'])




