from locust import HttpUser, task, between

class StressUser(HttpUser):
       wait_time = between(1, 2)  # Время ожидания между запросами

       @task
       def load_homepage(self):
           self.client.get("https://kivy.org/doc/stable/gettingstarted/layouts.html")  

       @task
       def load_search(self):
           self.client.get("https://kivy.org/doc/stable/gettingstarted/rules.html") 
