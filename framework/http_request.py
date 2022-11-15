import requests


class HttpRequest:
    @staticmethod
    def http_get(url, params):
        """
            Выполнение HTTP GET запроса.
        Args:
            url: URL
            params: Параметры запроса.

        Returns:
            Объект ответа на HTTP GET запрос.
        """
        return requests.get(
            url,
            params,
            allow_redirects=False,
        )
