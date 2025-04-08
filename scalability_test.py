from locust import HttpUser, task, between

class ScalabilityUser(HttpUser):
       wait_time = between(1, 5)  

       @task
       def load_homepage(self):
           self.client.get("https://kivy.org/doc/stable/gettingstarted/installation.html")  

       @task
       def load_search(self):
           self.client.get("https://kivy.org/doc/stable/gettingstarted/rules.html")  
    
