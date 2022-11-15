import json

import pytest
from hamcrest import assert_that, equal_to

from framework.api import Api
from framework.asserts.list_equals import assert_list_of_dicts_equals
from framework.contants import ApiConstants, FileConstants


class TestSearch:
    """Тестирование прямого (адрес->координаты) геокодирования."""

    @pytest.mark.parametrize(
        "search_query, expected_data_file",
        [
            pytest.param(
                'california', "../data/search_california.json"
            ),
            pytest.param(
                'big ben', "../data/search_big_ben.json"
            )
        ]
    )
    def test_search_by_query(self, search_query, expected_data_file):
        """
            Тестирование прямого геокодирования по запросу в свободной форме.
        Args:
            search_query: Строка запроса.
            expected_data_file: Путь до файла с ожидаемыми данными.
        """
        status_code, response_locations = Api.search_geo_by_query(
            ApiConstants.URL_SEARCH,
            search_query,
        )
        assert_that(status_code, equal_to(ApiConstants.STATUS_CODE_SUCCESS))
        with open(expected_data_file, encoding=FileConstants.UTF_8_ENCODING) as json_file:
            data_from_file = json.load(json_file)
            assert_list_of_dicts_equals(response_locations, data_from_file)

    @pytest.mark.parametrize(
        "street, limit, expected_data_file",
        [
            pytest.param(
                'calle de antonio leyva', -1, "../data/search_by_street_calle_de_antonio_leyva.json",
            ),
            pytest.param(
                'calle de antonio leyva', 2, "../data/search_by_street_calle_de_antonio_leyva_limit_2.json"
            ),
            pytest.param(
                'calle de antonio leyva', 0, "../data/search_by_street_calle_de_antonio_leyva_limit_0.json"
            )
        ]
    )
    def test_search_by_street(self, street, limit, expected_data_file):
        """
            Тестирование прямого геокодирования по улице.
        Args:
            street: Название улицы.
            limit: Максимальное значение количества записей в ответе из API.
            expected_data_file: Путь до файла с ожидаемыми данными.
        """
        status_code, response_locations = Api.search_geo_by_free_form_query(
            ApiConstants.URL_SEARCH,
            street=street,
            limit=limit
        )
        assert_that(status_code, equal_to(ApiConstants.STATUS_CODE_SUCCESS))
        with open(expected_data_file, encoding=FileConstants.UTF_8_ENCODING) as json_file:
            data_from_file = json.load(json_file)
            assert_list_of_dicts_equals(response_locations, data_from_file)

    @pytest.mark.parametrize(
        "street, city, expected_data_file",
        [
            pytest.param(
                'calle de antonio leyva', 'Madrid', "../data/search_by_street_calle_de_antonio_leyva_city_madrid.json",
            ),
            pytest.param(
                'calle de antonio leyva', 'London', "../data/empty.json"
            )
        ]
    )
    def test_search_by_street_and_city(self, street, city, expected_data_file):
        """
            Тестирование прямого геокодирования по улице и городу.
        Args:
            street: Название улицы.
            city: Название города.
            expected_data_file: Путь до файла с ожидаемыми данными.
        """
        status_code, response_locations = Api.search_geo_by_free_form_query(
            ApiConstants.URL_SEARCH,
            street=street,
            city=city
        )
        assert_that(status_code, equal_to(ApiConstants.STATUS_CODE_SUCCESS))
        with open(expected_data_file, encoding=FileConstants.UTF_8_ENCODING) as json_file:
            data_from_file = json.load(json_file)
            assert_list_of_dicts_equals(response_locations, data_from_file)

    @pytest.mark.parametrize(
        "city, country, expected_data_file",
        [
            pytest.param(
                'Moscow', '', "../data/search_by_city_moscow.json",
            ),
            pytest.param(
                'Moscow', 'Russia', "../data/search_by_city_moscow_contry_russia.json"
            )
        ]
    )
    def test_search_by_city(self, city, country, expected_data_file):
        """
        Тестирование прямого геокодирования по улице и стране.
        Args:
            city: Название города.
            country: Название страны.
            expected_data_file: Путь до файла с ожидаемыми данными.
        """
        status_code, response_locations = Api.search_geo_by_free_form_query(
            ApiConstants.URL_SEARCH,
            city=city,
            country=country
        )
        assert_that(status_code, equal_to(ApiConstants.STATUS_CODE_SUCCESS))
        with open(expected_data_file, encoding=FileConstants.UTF_8_ENCODING) as json_file:
            data_from_file = json.load(json_file)
            assert_list_of_dicts_equals(response_locations, data_from_file)
