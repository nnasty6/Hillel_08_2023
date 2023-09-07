import requests

# response = requests.get("https://pokeapi.co/api/v2/pokemon/12")
# data = response.json()
# print(f"pokemon is {data['name']}")


# requests.get(...)
# getattr(requests, "get")(...)


class ApiClient:
    ALLOWED_METHODS: list[str] = ["get"]

    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_response(self, method: str, endpoint: str) -> dict:
        if method not in self.ALLOWED_METHODS:
            raise NotImplementedError(f"Method {method} is not implemented")

        callback = getattr(requests, method)
        # url = self.base_url + endpoint
        url = "".join([self.base_url, endpoint])
        response = callback(url)

        # response.raise_for_status()

        try:
            return response.json()
        except Exception:
            raise Exception("HTTP request Error")


class ApiClientContext:
    def __init__(self, base_url: str) -> None:
        self._client: ApiClient | None = None
        self._base_url: str = base_url

    def __enter__(self):
        self._client = ApiClient(base_url=self._base_url)
        return self._client

    def __exit__(self, exc_type, exc_value, tb):
        print(f"⚠ ⚠ ⚠ Unexpected client's response: {exc_value}")
        print("Closing the client")
        # self._client.close()


# poke_api_client = ApiClient(base_url="https://pokeapi.co/api/v2")
# ditto_data = poke_api_client.get_response(
#     method="get", endpoint="/pokemon/ditto"
# )
with ApiClientContext(base_url="https://pokeapi.co/api/v2ee") as client:
    ditto_data = client.get_response(method="get", endpoint="/pokemon/ditto")
    print(f"Fetch pokemon: {ditto_data['name']}")
