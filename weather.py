import requests
import PySimpleGUI as sg

layout = [[sg.Text("Enter location to search the weather.")],
          [sg.Input(key='city')],
          [sg.Text(size=(40,1), key='weather_display')],
          [sg.Button('Search')]]

window = sg.Window('Weather', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    result1 = requests.get('https://www.metaweather.com/api/location/search/?query=' + values['city'])
    city_woeid = str(result1.json()[0]['woeid'])

    result2 = requests.get('https://www.metaweather.com/api/location/' + city_woeid)
    city_temp = str(round(result2.json()['consolidated_weather'][0]['the_temp']), 2)

    window['weather_display'].update('The weather in' + ' ' + values['city'] + ' is ' +  city_temp + ' degree celsius.')