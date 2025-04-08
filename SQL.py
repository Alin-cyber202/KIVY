import psycopg2
from kivy.app import App
from kivy.uix.label import Label

class KivyApp(App):
    def build(self):
        
        try:
            connection = psycopg2.connect(
                database="kivy_test",
                user="postgres",
                password="UOUYUHO",
                host="127.0.0.1",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            cursor.close()
            connection.close()
            return Label(text=f"PostgreSQL version: {db_version[0]}")
        except Exception as error:
            return Label(text=f"Error connecting to PostgreSQL: {error}")

if __name__ == '__main__':
    KivyApp().run()
   