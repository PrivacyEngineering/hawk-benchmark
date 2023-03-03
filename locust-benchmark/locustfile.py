import base64

from locust import HttpUser, TaskSet, task
from random import randint, choice


class WebTasks(TaskSet):

    @task
    def load(self):
        #base64string = base64.b64encode("user:password".encode()) #dXNlcjpwYXNzd29yZA==

        #catalogue = self.client.get("/catalogue").json()
        #category_item = choice(catalogue)
        #item_id = category_item["id"]

        #self.client.get("/")
        self.client.get("/login", headers={"Authorization":"Basic dXNlcjpwYXNzd29yZA=="})#"Basic %s" % base64string})
        self.client.get("/customers")
        self.client.get("/cards")
        self.client.get("/addresses")
        #self.client.delete("/cart")
        #self.client.post("/cart", json={"id": item_id, "quantity": 1})
        #self.client.get("/basket.html")
        #self.client.post("/orders")


class Web(HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0