import requests

def get_data(place, forecast_days):
    API_key="bc91e52e55fae6334befb0e212670af4"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response=requests.get(url)
    content=response.json()

    times = []
    temp = []

    for i in range(forecast_days*8):
        times.append(content["list"][i]["dt_txt"])
        temp_cel=content["list"][i]["main"]["temp"]-273.15
        temp.append(temp_cel)

    return times, temp

print(get_data("Tokyo", 1))


