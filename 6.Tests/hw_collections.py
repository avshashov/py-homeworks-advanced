def visits_from_russia():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    geo_logs_russia = []
    for element in geo_logs:
        for value in element.values():
            if 'Россия' in value:
                geo_logs_russia.append(element)

    return geo_logs_russia


def get_unique_ids():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    unique_ids = []

    for value in ids.values():
        unique_ids.extend(value)
    unique_ids = list(set(unique_ids))
    return unique_ids

def get_dict():
    lst = ['2018-01-01', 'yandex', 'cpc', 100]
    lst.reverse()
    dict_rand = {}
    for i in range(len(lst) - 1):
        if i == 0:
            dict_rand = {lst[1]: lst[0]}
        else:
            dict_rand = {lst[i + 1]: dict_rand}

    return dict_rand

