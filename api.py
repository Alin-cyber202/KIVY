from kivy.app import App
from kivy.uix.label import Label
from flask import Flask, jsonify

flask_app = Flask(__name__)

@flask_app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Kivy API!"})

@flask_app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"greeting": "Welcome to the Kivy API!"})

class MyKivyApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    # Запуск Flask API в отдельном потоке
    from threading import Thread
    Thread(target=flask_app.run, kwargs={'port': 5000}).start()
    MyKivyApp().run()
   