import time, random
from locust import HttpUser, task, between

class FoobarUser(HttpUser):

    """
    Demo implementation to work with the associated
    test API foobar: v1 
    """

    api_ver = "v1"
    api_base = "api"
    wait_time = between(1, 3)

    @task(2)
    def request_bar(self):
        wait_time = between(1, 5)

        with self.client.get(f'{self._get_request_base()}/bar', catch_response=True) as response:

            if response.statusCode == 200:

                # Introduce random failure
                chance = random.randint(1, 10)

                if chance == 3:
                    response.failure("Intermittent failure")
                else:
                    response.success("Success")

    @task(1)
    def request_foo(self):
        wait_time = between(1, 2)

        endpoint = f'{self._get_request_base()}/foo'

        query_param = "query"
        payload = "foobar"

        self.client.get(f'{endpoint}?{query_param}={payload}', name=endpoint)
    
    def _get_request_base(self):
        return f'/{self.api_base}/{self.api_ver}'
