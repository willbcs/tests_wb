import requests
from datetime import datetime
import pytz
from PIL import Image
from io import BytesIO
import pandas as pd
from typing import Dict, List, Optional, Union

class ClimaTempo:
    def __init__(self, api_key: str):
        self.API_KEY = api_key
        self.BASE_URL = "https://api.openweathermap.org/data/2.5"
        self.WEATHER_ICONS = {
            "01d": "☀️", "01n": "🌙",
            "02d": "⛅", "02n": "⛅",
            "03d": "☁️", "03n": "☁️",
            "04d": "☁️", "04n": "☁️",
            "09d": "🌧️", "09n": "🌧️",
            "10d": "🌦️", "10n": "🌦️",
            "11d": "⛈️", "11n": "⛈️",
            "13d": "❄️", "13n": "❄️",
            "50d": "🌫️", "50n": "🌫️",
            "default": "🌤️"
        }
        self.ALERT_CONDITIONS = {
            "Thunderstorm": "⚠️ Tempestade",
            "Tornado": "⛔ Tornado",
            "Squall": "⚠️ Rajadas de Vento",
            "Rain": lambda x: "⚠️ Chuva Forte" if x > 10 else "🌧️ Chuva",
            "Snow": "❄️ Neve",
            "Extreme": "🚨 Condição Extrema",
            "Clear": lambda x: "☀️ Calor Extremo" if x > 35 else None,
            "Clouds": lambda x: "⚠️ Nebulosidade Perigosa" if x > 95 else None
        }
    
    def get_current_weather(self, city_name: str, unit: str = 'metric') -> Dict:
        """Obtém dados meteorológicos atuais com tratamento robusto de erros"""
        url = f"{self.BASE_URL}/weather"
        params = {
            'q': city_name,
            'appid': self.API_KEY,
            'units': unit,
            'lang': 'pt'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return self._process_current_data(response.json(), unit)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {str(e)}")
        except Exception as e:
            raise Exception(f"Erro ao processar dados: {str(e)}")
    
    def get_forecast(self, city_name: str, unit: str = 'metric') -> Dict:
        """Obtém previsão do tempo para 5 dias com 3h de intervalo"""
        url = f"{self.BASE_URL}/forecast"
        params = {
            'q': city_name,
            'appid': self.API_KEY,
            'units': unit,
            'lang': 'pt',
            'cnt': 40
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return self._process_forecast_data(data, unit)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {str(e)}")
        except Exception as e:
            raise Exception(f"Erro ao processar previsão: {str(e)}")
    
    def _process_current_data(self, data: Dict, unit: str) -> Dict:
        """Processa os dados atuais com informações adicionais"""
        temp = data['main']['temp']
        wind_speed = data['wind']['speed'] * 3.6  # m/s → km/h
        wind_gust = data['wind'].get('gust', 0) * 3.6
        
        alerts = self._check_alerts(
            data['weather'][0]['main'],
            temp,
            data.get('rain', {}).get('1h', 0),
            data['clouds']['all']
        )
        
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temp': temp,
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'sea_level': data['main'].get('sea_level'),
            'grnd_level': data['main'].get('grnd_level'),
            'wind_speed': wind_speed,
            'wind_gust': wind_gust,
            'wind_deg': data['wind'].get('deg', 0),
            'weather_desc': data['weather'][0]['description'].capitalize(),
            'weather_main': data['weather'][0]['main'],
            'weather_icon': self.WEATHER_ICONS.get(data['weather'][0]['icon'], self.WEATHER_ICONS['default']),
            'sunrise': self._timestamp_to_local(data['sys']['sunrise'], data['timezone']),
            'sunset': self._timestamp_to_local(data['sys']['sunset'], data['timezone']),
            'visibility': data.get('visibility', 0) / 1000,
            'clouds': data['clouds']['all'],
            'rain': data.get('rain', {}).get('1h', 0),
            'snow': data.get('snow', {}).get('1h', 0),
            'timezone_offset': data['timezone'],
            'coord': data['coord'],
            'alerts': alerts,
            'unit': unit,
            'wind_unit': 'km/h',
            'dt': self._timestamp_to_local(data['dt'], data['timezone'])
        }
    
    def _process_forecast_data(self, data: Dict, unit: str) -> Dict:
        """Processa dados de previsão com análise detalhada"""
        processed = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'coord': data['city']['coord'],
            'timezone_offset': data['city']['timezone'],
            'unit': unit,
            'wind_unit': 'km/h',
            'forecast': []
        }
        
        for item in data['list']:
            temp = item['main']['temp']
            wind_speed = item['wind']['speed'] * 3.6
            wind_gust = item['wind'].get('gust', 0) * 3.6
            rain = item.get('rain', {}).get('3h', 0)
            
            forecast_item = {
                'dt': item['dt'],
                'datetime': self._timestamp_to_local(item['dt'], data['city']['timezone']),
                'date': self._timestamp_to_local(item['dt'], data['city']['timezone'], date_only=True),
                'time': self._timestamp_to_local(item['dt'], data['city']['timezone'], time_only=True),
                'temp': temp,
                'feels_like': item['main']['feels_like'],
                'temp_min': item['main']['temp_min'],
                'temp_max': item['main']['temp_max'],
                'humidity': item['main']['humidity'],
                'pressure': item['main']['pressure'],
                'sea_level': item['main'].get('sea_level'),
                'grnd_level': item['main'].get('grnd_level'),
                'wind_speed': wind_speed,
                'wind_gust': wind_gust,
                'wind_deg': item['wind'].get('deg', 0),
                'weather_desc': item['weather'][0]['description'].capitalize(),
                'weather_main': item['weather'][0]['main'],
                'weather_icon': self.WEATHER_ICONS.get(item['weather'][0]['icon'], self.WEATHER_ICONS['default']),
                'pop': item.get('pop', 0) * 100,
                'rain': rain,
                'snow': item.get('snow', {}).get('3h', 0),
                'clouds': item['clouds']['all'],
                'visibility': item.get('visibility', 10000) / 1000,
                'alerts': self._check_alerts(
                    item['weather'][0]['main'],
                    temp,
                    rain,
                    item['clouds']['all']
                ),
                'is_day': item['sys']['pod'] == 'd'
            }
            processed['forecast'].append(forecast_item)
        
        return processed
    
    def _timestamp_to_local(self, timestamp: int, timezone_offset: int = None, 
                          date_only: bool = False, time_only: bool = False) -> str:
        """Converte timestamp para hora local com fuso horário"""
        dt = datetime.fromtimestamp(timestamp)
        if timezone_offset:
            timezone = pytz.FixedOffset(timezone_offset / 60)
            dt = dt.replace(tzinfo=pytz.utc).astimezone(timezone)
        
        if date_only:
            return dt.strftime('%Y-%m-%d')
        elif time_only:
            return dt.strftime('%H:%M')
        return dt.strftime('%Y-%m-%d %H:%M')
    
    def _check_alerts(self, weather_main: str, temp: float, 
                     rain: float = 0, clouds: float = 0) -> List[str]:
        """Verifica condições meteorológicas para alertas avançados"""
        alerts = []
        
        # Verifica condições específicas
        condition = self.ALERT_CONDITIONS.get(weather_main)
        if condition:
            if callable(condition):
                alert = condition(rain if weather_main == "Rain" else temp if weather_main == "Clear" else clouds)
                if alert:
                    alerts.append(alert)
            else:
                alerts.append(condition)
        
        # Verifica temperaturas extremas
        if temp > 35:
            alerts.append("🚨 Calor Extremo (>35°C)")
        elif temp < 5:
            alerts.append("❄️ Frio Extremo (<5°C)")
            
        # Verifica chuva intensa
        if rain > 20:
            alerts.append("⚠️ Chuva Muito Intensa (>20mm)")
        elif rain > 10:
            alerts.append("🌧️ Chuva Intensa (>10mm)")
            
        # Verifica ventos fortes
        return list(set(alerts))  # Remove duplicatas
    
    def get_country_flag(self, country_code: str) -> Optional[Image.Image]:
        """Obtém a bandeira do país com fallback"""
        if not country_code or len(country_code) != 2:
            return None
            
        flag_url = f"https://flagcdn.com/w160/{country_code.lower()}.png"
        try:
            response = requests.get(flag_url, timeout=5)
            if response.status_code == 200:
                return Image.open(BytesIO(response.content))
            
            # Fallback para API alternativa
            flag_url = f"https://countryflagsapi.com/png/{country_code}"
            response = requests.get(flag_url, timeout=5)
            if response.status_code == 200:
                return Image.open(BytesIO(response.content))
                
            return None
        except Exception:
            return None
    
    def calculate_comfort_index(self, temp: float, humidity: float, wind_speed: float) -> float:
        """Calcula índice de conforto térmico (0-100) com base em:
        - Temperatura
        - Umidade relativa
        - Velocidade do vento
        """
        # Ajusta para vento frio (Wind Chill)
        if temp < 10:
            wind_chill = 13.12 + 0.6215 * temp - 11.37 * (wind_speed**0.16) + 0.3965 * temp * (wind_speed**0.16)
            comfort = max(0, 100 - (10 - wind_chill) * 5 - (100 - humidity) * 0.2)
        
        # Ajusta para calor e umidade (Heat Index)
        elif temp > 27:
            heat_index = -8.784695 + 1.61139411 * temp + 2.338549 * humidity - 0.14611605 * temp * humidity
            comfort = max(0, 100 - (heat_index - 27) * 3 - humidity * 0.1)
        
        # Faixa de conforto
        else:
            comfort = 100 - abs(temp - 22) * 2 - abs(humidity - 60) * 0.1
            
        return max(0, min(100, round(comfort, 1)))
    
    def get_air_quality(self, lat: float, lon: float) -> Optional[Dict]:
        """Obtém dados de qualidade do ar para coordenadas específicas"""
        url = f"{self.BASE_URL}/air_pollution"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.API_KEY
        }
        
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            aqi_map = {
                1: "Bom",
                2: "Moderado",
                3: "Ruim para grupos sensíveis",
                4: "Ruim",
                5: "Muito Ruim"
            }
            
            main_data = data['list'][0]
            return {
                'aqi': main_data['main']['aqi'],
                'aqi_level': aqi_map.get(main_data['main']['aqi'], "Desconhecido"),
                'components': main_data['components'],
                'dt': self._timestamp_to_local(main_data['dt'])
            }
        except Exception:
            return None