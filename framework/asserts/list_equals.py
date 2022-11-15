from framework.asserts.dict_equals import assert_data_has_entries


def assert_list_of_dicts_equals(actual_list_of_items, expected_list_of_items):
    """
        Сравнение списков словарей.
    Args:
        actual_list_of_items: Список словарей для сравнения.
        expected_list_of_items: Ожидаемый список словарей.
    """
    for count, data in enumerate(actual_list_of_items):
        assert_data_has_entries(data, expected_list_of_items[count])
