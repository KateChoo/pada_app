import requests
r = requests.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
r.encoding = "UTF-8"
data = r.json()
taipei_fun = data['result']['results']
with open('data.txt', 'w', encoding='utf-8') as file:
    for fun in taipei_fun:
            photo_http = 'http://www.travel.taipei/d_upload_ttn'
            first_photo = fun['file'].split(photo_http)[1]
            some_data = (f"{fun['stitle']}, {fun['longitude']}, {fun['latitude']}, {photo_http+first_photo}\n")
            #file.write({fun['stitle']}, {fun['longitude']}, {fun['latitude']}, {photo_http+first_photo}")
            file.write(some_data)