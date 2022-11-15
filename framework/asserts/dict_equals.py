from hamcrest import assert_that, has_entries


def assert_data_has_entries(data, expected_entries):
    """
        Проверка значение в словаре.
    Args:
        data: Словарь для проверки.
        expected_entries: Словарь ожидаемых значений.
    """
    assert_that(data, has_entries(expected_entries), 'Параметры не соответствуют ожидаемым')
