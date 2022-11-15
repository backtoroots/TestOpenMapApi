import json

from framework.http_request import HttpRequest


class Api:
    """Выполнение запросов к API OpenMapApi."""
    _FREE_FORM_QUERY_KEY = 'q'
    _QUERY_STREET_KEY = 'street'
    _QUERY_CITY_KEY = 'city'
    _QUERY_COUNTY_KEY = 'county'
    _QUERY_STATE_KEY = 'state'
    _QUERY_COUNTRY_KEY = 'country'
    _QUERY_POSTALCODE_KEY = 'postalcode'
    _LAT_KEY = 'lat'
    _LON_KEY = 'lon'
    _OUTPUT_FORMAT_KEY = 'format'
    _OUTPUT_LIMIT_KEY = 'limit'
    _OUTPUT_LANGUAGE_KEY = 'accept-language'

    @staticmethod
    def search_geo_by_query(url: str, query: str, limit: int = -1, output_format: str = 'json',
                            output_language: str = 'en-US'):
        """
            Выполнение запроса вида /search?q=<q>.
        Args:
            url: URL
            query: Строка запроса в свободной форме.
            limit: Максимальное значение количества записей в ответе из API.
            output_format: Формат данных из ответа.
            output_language: Используемый для данных из ответа язык.

        Returns:
            Код состояния HTTP ответа.
            Полученные в ответе данные.
        """
        params = {Api._FREE_FORM_QUERY_KEY: query}
        Api._form_output_params(params, limit, output_format, output_language)
        response = HttpRequest.http_get(url, params)
        return response.status_code, json.loads(response.content)

    @staticmethod
    def search_geo_by_free_form_query(url: str, street: str = '', city: str = '', county: str = '',
                                      state: str = '', country: str = '', postalcode: str = '', limit: int = -1,
                                      output_format: str = 'json',
                                      output_language: str = 'en-US'):
        """
            Выполнение запроса вида /search?params, где params:
                street=<housenumber> <streetname>
                city=<city>
                county=<county>
                state=<state>
                country=<country>
                postalcode=<postalcode>
        Args:
            url: URL
            street: Название улицы.
            city: Название города.
            county: Название округа.
            state: Название штата.
            country: Название страны.
            postalcode: Почтовый индекс.
            limit: Максимальное значение количества записей в ответе из API.
            output_format: Формат данных из ответа.
            output_language: Используемый для данных из ответа язык.

        Returns:
            Код состояния HTTP ответа.
            Полученные в ответе данные.
        """
        params = {key: value for (key, value) in
                  zip([
                      Api._QUERY_STREET_KEY,
                      Api._QUERY_CITY_KEY,
                      Api._QUERY_COUNTY_KEY,
                      Api._QUERY_STATE_KEY,
                      Api._QUERY_COUNTRY_KEY,
                      Api._QUERY_POSTALCODE_KEY,
                  ],
                      [street, city, county, state, country, postalcode]) if value != ''}

        Api._form_output_params(params, limit, output_format, output_language)

        response = HttpRequest.http_get(
            url,
            params
        )
        return response.status_code, json.loads(response.content)

    @staticmethod
    def reverse(url: str, lat: float, lon: float, limit: int = -1, output_format: str = 'json',
                output_language: str = 'en-US'):
        """
            Выполнение запроса вида /reverse?lat=<lat>&lon=<lon>.
        Args:
            url: URL
            lat: Широта геоточки.
            lon: Долгота геоточки.
            limit: Максимальное значение количества записей в ответе из API.
            output_format: Формат данных из ответа.
            output_language: Используемый для данных из ответа язык.

        Returns:
            Код состояния HTTP ответа.
            Полученные в ответе данные.
        """
        params = {Api._LAT_KEY: lat, Api._LON_KEY: lon}
        Api._form_output_params(params, limit, output_format, output_language)
        response = HttpRequest.http_get(url, params)
        return response.status_code, json.loads(response.content)

    @staticmethod
    def _form_output_params(params: dict, limit: int = -1, output_format: str = 'json',
                            output_language: str = 'en-US'):
        """
            Добавление дополнительных параметров к основному набору.
        Args:
            params: Словарь основных парамтеров.
            limit: Максимальное значение количества записей в ответе из API.
            output_format: Формат данных из ответа.
            output_language: Используемый для данных из ответа язык.

        """
        output_param_values = [limit, output_format, output_language]
        for count, param in enumerate([
            Api._OUTPUT_LIMIT_KEY, Api._OUTPUT_FORMAT_KEY, Api._OUTPUT_LANGUAGE_KEY
        ]):
            param_value = output_param_values[count]
            if param_value != str() and param_value != -1:
                params[param] = param_value
