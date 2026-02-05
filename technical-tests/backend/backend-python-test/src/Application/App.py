from src.Services.ApiService import ApiService


class App:
    def __init__(self):
        self._api_service = ApiService()

    def api_service(self) -> ApiService:
        return self._api_service
