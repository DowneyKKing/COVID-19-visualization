# -*- coding: utf-8 -*-
import json


output_path = "C:\\Users\\74116\\Desktop\\"
max_confirmed = 0
max_deaths = 0
max_recovered = 0


def get_json():
    file_path = "C:\\Users\\74116\\Desktop\\timeseries.json"
    with open(file_path, 'r', encoding='utf8') as f:
        json_data = json.load(f)
        f.close()
    return json_data


def get_data_series(arg):
    countries, date, confirmed, deaths, recovered = [], [], [], [], []
    for i in get_json().keys():
        countries.append(i)
        records = get_json()[i][-1]
        confirmed.append(records['confirmed'])
        deaths.append(records['deaths'])
        recovered.append(records['recovered'])
    if arg == "confirmed":
        nums = confirmed
    elif arg == "deaths":
        nums = deaths
    elif arg == "recovered":
        nums = recovered
    else:
        nums = ""
    data = [list(z) for z in zip(countries, nums)]
    global max_confirmed, max_deaths, max_recovered
    max_confirmed = max(confirmed)
    max_recovered = max(recovered)
    max_deaths = max(deaths)
    return data


