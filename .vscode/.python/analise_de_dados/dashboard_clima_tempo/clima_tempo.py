import requests
from datetime import datetime
import pytz
from PIL import Image
from io import BytesIO
import pandas as pd

class ClimaTempo:
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.BASE_URL = "https://api.openweathermap.org/data/2.5"
        self.WEATHER_ICONS = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Fog": "🌁",
            "Tornado": "🌪️"
        }
        self.ALERT_CONDITIONS = {
            "Thunderstorm": "⚠️ Tempestade",
            "Tornado": "⛔ Tornado",
            "Rain": "⚠️ Chuva Forte",
            "Snow": "❄️ Neve",
            "Extreme Heat": "🔥 Calor Extremo",
            "Extreme Cold": "❄️ Frio Extremo"
        }
    
    def get_current_weather(self, city_name, unit='metric'):
        """Obtém dados meteorológicos atuais"""
        url = f"{self.BASE_URL}/weather"
        params = {
            'q': city_name,
            'appid': self.API_KEY,
            'units': unit,
            'lang': 'pt'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return self._process_current_data(response.json(), unit)
        else:
            raise Exception(f"Erro ao obter dados: {response.json().get('message', 'Cidade não encontrada')}")
    
    def get_forecast(self, city_name, unit='metric'):
        """Obtém previsão do tempo para 5 dias"""
        url = f"{self.BASE_URL}/forecast"
        params = {
            'q': city_name,
            'appid': self.API_KEY,
            'units': unit,
            'lang': 'pt',
            'cnt': 40  # 40 períodos de 3 horas = 5 dias
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'list' in data and len(data['list']) > 0:
                return self._process_forecast_data(data, unit)
            else:
                raise Exception("Nenhum dado de previsão disponível")
        else:
            raise Exception(f"Erro ao obter previsão: {response.json().get('message', 'Cidade não encontrada')}")
    
    def _process_current_data(self, data, unit):
        """Processa os dados atuais da API"""
        wind_unit = 'km/h'
        wind_speed = data['wind']['speed'] * 3.6  # Convertendo para km/h
        
        processed = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': wind_speed,
            'wind_deg': data['wind'].get('deg', 0),
            'weather_desc': data['weather'][0]['description'].capitalize(),
            'weather_main': data['weather'][0]['main'],
            'weather_icon': self.WEATHER_ICONS.get(data['weather'][0]['main'], "🌤️"),
            'sunrise': self._timestamp_to_local(data['sys']['sunrise'], data['timezone']),
            'sunset': self._timestamp_to_local(data['sys']['sunset'], data['timezone']),
            'visibility': data.get('visibility', 0) / 1000,  # em km
            'clouds': data['clouds']['all'],
            'timezone_offset': data['timezone'],
            'coord': data['coord'],
            'alerts': self._check_alerts(data['weather'][0]['main'], data['main']['temp']),
            'unit': unit,
            'wind_unit': wind_unit
        }
        return processed
    
    def _process_forecast_data(self, data, unit):
        """Processa os dados de previsão da API"""
        wind_unit = 'km/h'
        processed = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'coord': data['city']['coord'],
            'timezone_offset': data['city']['timezone'],
            'unit': unit,
            'wind_unit': wind_unit,
            'forecast': []
        }
        
        for item in data['list']:
            wind_speed = item['wind']['speed'] * 3.6  # Convertendo para km/h
            
            forecast_item = {
                'datetime': self._timestamp_to_local(item['dt'], data['city']['timezone']),
                'date': self._timestamp_to_local(item['dt'], data['city']['timezone'], date_only=True),
                'time': self._timestamp_to_local(item['dt'], data['city']['timezone'], time_only=True),
                'temp': item['main']['temp'],
                'feels_like': item['main']['feels_like'],
                'humidity': item['main']['humidity'],
                'pressure': item['main']['pressure'],
                'wind_speed': wind_speed,
                'wind_deg': item['wind'].get('deg', 0),
                'weather_desc': item['weather'][0]['description'].capitalize(),
                'weather_main': item['weather'][0]['main'],
                'weather_icon': self.WEATHER_ICONS.get(item['weather'][0]['main'], "🌤️"),
                'pop': item.get('pop', 0) * 100,  # Probabilidade de precipitação em %
                'clouds': item['clouds']['all'],
                'alerts': self._check_alerts(item['weather'][0]['main'], item['main']['temp'])
            }
            processed['forecast'].append(forecast_item)
        
        return processed
    
    def _timestamp_to_local(self, timestamp, timezone_offset=None, date_only=False, time_only=False):
        """Converte timestamp para hora local"""
        dt = datetime.fromtimestamp(timestamp)
        if timezone_offset:
            timezone = pytz.FixedOffset(timezone_offset / 60)
            dt = dt.replace(tzinfo=pytz.utc).astimezone(timezone)
        
        if date_only:
            return dt.strftime('%Y-%m-%d')
        elif time_only:
            return dt.strftime('%H:%M')
        return dt.strftime('%Y-%m-%d %H:%M')
    
    def _check_alerts(self, weather_main, temp):
        """Verifica condições meteorológicas que merecem alerta"""
        alerts = []
        
        if weather_main in self.ALERT_CONDITIONS:
            alerts.append(self.ALERT_CONDITIONS[weather_main])
        
        if temp > 35:
            alerts.append(self.ALERT_CONDITIONS["Extreme Heat"])
        elif temp < 5:
            alerts.append(self.ALERT_CONDITIONS["Extreme Cold"])
        
        return alerts
    
    def get_country_flag(self, country_code):
        """Obtém a bandeira do país"""
        flag_url = f"https://flagcdn.com/w160/{country_code.lower()}.png"
        try:
            response = requests.get(flag_url)
            return Image.open(BytesIO(response.content))
        except:
            return None