from locust import HttpUser, task, between

class ReliabilityUser(HttpUser):
       wait_time = between(1, 2)  # Время ожидания между запросами

       @task
       def load_homepage(self):
           response = self.client.get("https://kivy.org/doc/stable/gettingstarted/installation.html")
           if response.status_code != 200:
               print(f"Error loading homepage: {response.status_code}")

       @task
       def load_another_page(self):
           response = self.client.get("https://kivy.org/doc/stable/gettingstarted/rules.html")
           if response.status_code != 200:
               print(f"Error loading rules page: {response.status_code}")
    
