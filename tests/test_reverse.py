import json

import pytest
from hamcrest import equal_to, assert_that

from framework.api import Api
from framework.asserts.dict_equals import assert_data_has_entries
from framework.contants import ApiConstants, FileConstants


class TestReverse:
    """Тестирование обратного (координаты->адрес) геокодирования."""

    @pytest.mark.parametrize(
        "lat, lon, expected_data_file",
        [
            pytest.param(
                '51.5006895', '-0.1245838', "../data/reverse_big_ben.json"
            ),
            pytest.param(
                '40.3965729', '-3.715302', "../data/reverse_calle_de_antonio_leyva.json"
            )
        ]
    )
    def test_reverse(self, lat, lon, expected_data_file):
        """
            Тестирование обратного геокодирования по широте и долготе.
        Args:
            lat: Широта геоточки.
            lon: Долгота геоточки.
            expected_data_file: Путь до файла с ожидаемыми данными.
        """
        status_code, response_locations = Api.reverse(
            ApiConstants.URL_REVERSE,
            lat,
            lon
        )
        assert_that(status_code, equal_to(ApiConstants.STATUS_CODE_SUCCESS))
        with open(expected_data_file, encoding=FileConstants.UTF_8_ENCODING) as json_file:
            data_from_file = json.load(json_file)
            assert_data_has_entries(response_locations, data_from_file)
