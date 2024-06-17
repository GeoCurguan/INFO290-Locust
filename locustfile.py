from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_items(self):
        self.client.get("/items")

    @task
    def create_item(self):
        self.client.post("/items", json={"name": "test_item", "price": 10.99})