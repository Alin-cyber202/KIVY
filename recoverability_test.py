from locust import HttpUser, task, between
import time

class RecoverabilityUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_homepage(self):
        response = self.client.get("https://kivy.org/doc/stable/gettingstarted/intro.html")
        if response.status_code != 200:
            print(f"Error loading homepage: {response.status_code}")

    @task
    def induce_error(self):
        response = self.client.get("https://kivy.org/doc/stable/gettingstarted/nonexistent")
        if response.status_code != 404:
            print(f"Expected 404, got {response.status_code}.")
        else:
            print("Error induced successfully, waiting for recoverability...")
            time.sleep(5)  
            self.check_recoverability()

    def check_recoverability(self):
        response = self.client.get("https://kivy.org/doc/stable/gettingstarted/intro.html")
        if response.status_code == 200:
            print("System is back to normal.")
        else:
            print(f"System not recovered, current status: {response.status_code}.")
   