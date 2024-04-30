from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def add_note(self):
        self.client.post('/add', json={'title': 'Test Note', 'content': 'Test Content'})

    @task
    def view_notes(self):
        self.client.get('/')

if __name__ == '__main__':
    import os
    os.system('locust -f locustfile.py')
