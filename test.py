from locust import HttpLocust, TaskSet, task


class UserTasks(TaskSet):

    @task
    def index(self):
        self.client.get('/')

    @task
    def imovel(self):
        self.client.get('/does_not_exist')


class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://192.168.1.5"
    min_wait = 20 * 1000
    max_wait = 100 * 1000
    task_set = UserTasks
