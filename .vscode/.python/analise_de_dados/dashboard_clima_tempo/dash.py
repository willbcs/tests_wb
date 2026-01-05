import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from clima_tempo import ClimaTempo
from PIL import Image
from io import BytesIO
import json
from streamlit_lottie import st_lottie

# Configuração da página
st.set_page_config(
    page_title="Dashboard Meteorológico Avançado",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# Lista de cidades
CITIES = [
    # Capitais do Mundo (adicionadas 15 novas)
    'Abu Dhabi', 'Accra', 'Addis Ababa', 'Algiers', 'Andorra la Vella', 'Ankara', 'Antananarivo', 'Asunción', 'Athens', 'Baghdad',
    'Baku', 'Bamako', 'Bangkok', 'Banjul', 'Beijing', 'Beirut', 'Belgrade', 'Berlin', 'Bern', 'Bishkek',
    'Bogotá', 'Brasília', 'Bratislava', 'Brazzaville', 'Bridgetown', 'Brussels', 'Bucharest', 'Budapest', 'Buenos Aires', 'Cairo',
    'Canberra', 'Caracas', 'Castries', 'Chisinau', 'Colombo', 'Conakry', 'Copenhagen', 'Dakar', 'Damascus', 'Dhaka',
    'Dili', 'Dodoma', 'Doha', 'Dublin', 'Dushanbe', 'Edinburgh', 'Freetown', 'Gaborone', 'Georgetown', 'Hanoi',
    'Harare', 'Havana', 'Helsinki', 'Islamabad', 'Jakarta', 'Jerusalem', 'Juba', 'Kabul', 'Kampala', 'Kathmandu',
    'Khartoum', 'Kiev', 'Kigali', 'Kingston', 'Kinshasa', 'Kuala Lumpur', 'Kuwait City', 'La Paz', 'Libreville', 'Lima',
    'Lisbon', 'Ljubljana', 'Lome', 'London', 'Luanda', 'Lusaka', 'Luxembourg', 'Madrid', 'Majuro', 'Malabo',
    'Male', 'Managua', 'Manama', 'Manila', 'Mansoura', 'Maputo', 'Marigot', 'Maseru', 'Mbabane', 'Mexico City',
    'Minsk', 'Mogadishu', 'Monaco', 'Monrovia', 'Montevideo', 'Moroni', 'Moscow', 'Muscat', 'Nairobi', 'Nassau',
    'New Delhi', 'Niamey', 'Nicosia', 'Nouakchott', 'Nukuʻalofa', 'Oslo', 'Ottawa', 'Ouagadougou', 'Panama City', 'Paramaribo',
    'Paris', 'Phnom Penh', 'Podgorica', 'Port Louis', 'Port Moresby', 'Port Vila', 'Port-au-Prince', 'Porto-Novo', 'Prague', 'Praia',
    'Pretoria', 'Pyongyang', 'Quito', 'Rabat', 'Reykjavik', 'Riga', 'Riyadh', 'Rome', 'Roseau', 'San José',
    'San Marino', 'San Salvador', 'Sana', 'Santiago', 'São Tomé', 'Sarajevo', 'Seoul', 'Singapore', 'Skopje', 'Sofia',
    'Stockholm', 'Sucre', 'Taipei', 'Tallinn', 'Tashkent', 'Tbilisi', 'Tegucigalpa', 'Tehran', 'Thimphu', 'Tirana',
    'Tokyo', 'Tripoli', 'Tunis', 'Ulaanbaatar', 'Vaduz', 'Valletta', 'Vatican City', 'Victoria', 'Vienna', 'Vientiane',
    'Vilnius', 'Warsaw', 'Washington, D.C.', 'Wellington', 'Windhoek', 'Yamoussoukro', 'Yaoundé', 'Yerevan', 'Zagreb', 'Zurich',
    
    # Principais Cidades do Mundo 
    'Amsterdam', 'Barcelona', 'Belfast', 'Birmingham', 'Boston', 'Brisbane', 'Brno', 'Brussels', 'Budapest', 'Cape Town',
    'Chicago', 'Dallas', 'Dubai', 'Edinburgh', 'Frankfurt', 'Glasgow', 'Guangzhou', 'Hamburg', 'Hong Kong', 'Houston',
    'Istanbul', 'Johannesburg', 'Kolkata', 'Las Vegas', 'Leeds', 'Liverpool', 'Los Angeles', 'Lyon', 'Manchester', 'Melbourne',
    'Miami', 'Milan', 'Montreal', 'Munich', 'Nagoya', 'Naples', 'New York', 'Osaka', 'Philadelphia', 'Prague',
    'Quebec City', 'Rio de Janeiro', 'Rotterdam', 'San Diego', 'San Francisco', 'Santiago', 'Sapporo', 'Seattle', 'Seoul', 'Shanghai',
    'Shenzhen', 'Singapore', 'Sydney', 'Taipei', 'Toronto', 'Vancouver', 'Venice', 'Vienna', 'Warsaw', 'Zurich',
    'Adelaide', 'Auckland', 'Bangalore', 'Bangkok', 'Barcelona', 'Berlin', 'Bogotá', 'Brisbane', 'Buenos Aires', 'Cairo',
    'Cape Town', 'Caracas', 'Casablanca', 'Chicago', 'Copenhagen', 'Delhi', 'Detroit', 'Dhaka', 'Doha', 'Dubai',
    'Dublin', 'Edinburgh', 'Geneva', 'Guadalajara', 'Guatemala City', 'Havana', 'Helsinki', 'Ho Chi Minh City', 'Hong Kong', 'Houston'

    # Capitais do Brasil (completas)
    'Aracaju', 'Belém', 'Belo Horizonte', 'Boa Vista', 'Brasília', 'Campo Grande', 'Cuiabá', 'Curitiba', 'Florianópolis', 'Fortaleza',
    'Goiânia', 'João Pessoa', 'Macapá', 'Maceió', 'Manaus', 'Natal', 'Palmas', 'Porto Alegre', 'Porto Velho', 'Recife',
    'Rio Branco', 'Rio de Janeiro', 'Salvador', 'São Luís', 'São Paulo', 'Teresina', 'Vitória',
    
    # Principais Cidades do Brasil (adicionadas 20 novas)
    'Anápolis', 'Aparecida de Goiânia', 'Araguaína', 'Arapiraca', 'Barreiras', 'Bauru', 'Blumenau', 'Camaçari', 'Campina Grande', 'Campinas',
    'Caxias do Sul', 'Chapecó', 'Contagem', 'Criciúma', 'Divinópolis', 'Dourados', 'Feira de Santana', 'Franca', 'Governador Valadares', 'Guarulhos',
    'Ilhéus', 'Ipatinga', 'Itabuna', 'Jaboatão dos Guararapes', 'Jacareí', 'Joinville', 'Juazeiro do Norte', 'Juiz de Fora', 'Jundiaí', 'Limeira',
    'Londrina', 'Luziânia', 'Mauá', 'Mossoró', 'Niterói', 'Osasco', 'Parauapebas', 'Paulista', 'Pelotas', 'Petrolina',
    'Petrópolis', 'Pindamonhangaba', 'Piracicaba', 'Poços de Caldas', 'Pontes e Lacerda', 'Praia Grande', 'Ribeirão Preto', 'Rondonópolis', 'Santa Maria', 'Santana do Livramento',
    'Santarém', 'Santo André', 'Santos', 'São Bernardo do Campo', 'São Carlos', 'São José do Rio Preto', 'São José dos Campos', 'São Leopoldo', 'Sorocaba', 'Taboão da Serra',
    'Taubaté', 'Uberaba', 'Uberlândia', 'Várzea Grande', 'Viamão', 'Vitória da Conquista', 'Volta Redonda', 'Votorantim',

]
# Inicializa o cliente da API
clima = ClimaTempo("69ddec2d6c8acd5a481e1c6959e64262")

# Session State para histórico
if 'history' not in st.session_state:
    st.session_state.history = []
if 'compare_cities' not in st.session_state:
    st.session_state.compare_cities = []

# Sidebar
with st.sidebar:
    st.header("🌍 Navegação")
    tab = st.radio("Selecione a visualização:", 
                  ["Visão Atual", "Previsão Completa", "Comparar Cidades"])
    
    st.header("🔍 Seleção de Cidade")
    selected_city = st.selectbox("Escolha uma cidade:", CITIES, index=CITIES.index('São Paulo'))
    
    if tab != "Comparar Cidades":
        if st.button("Adicionar ao histórico"):
            if selected_city not in st.session_state.history:
                st.session_state.history.append(selected_city)
    
    if st.button("Adicionar para comparação"):
        if selected_city not in st.session_state.compare_cities:
            if len(st.session_state.compare_cities) < 3:
                st.session_state.compare_cities.append(selected_city)
                try:
                    confirm_animation = load_lottie_file("confirm.json")
                    
                    # Container com CSS para centralização
                    container = st.container()
                    with container:
                        st.markdown(
                            """
                            <style>
                                .centered {
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                    flex-direction: column;
                                }
                            </style>
                            <div class="centered">
                            """,
                            unsafe_allow_html=True
                        )
                        
                        st_lottie(
                            confirm_animation,
                            speed=1,
                            reverse=False,
                            loop=False,
                            quality="high",
                            height=150,
                            width=260,
                            key="confirm"
                        )
                        st.success(f"{selected_city} adicionada para comparação!")
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.success(f"{selected_city} adicionada para comparação!")
            else:
                try:
                    denied_animation = load_lottie_file("denied.json")
                    
                    # Container com CSS para centralização
                    container = st.container()
                    with container:
                        st.markdown(
                            """
                            <style>
                                .centered {
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                    flex-direction: column;
                                }
                            </style>
                            <div class="centered">
                            """,
                            unsafe_allow_html=True
                        )
                        
                        st_lottie(
                            denied_animation,
                            speed=1,
                            reverse=False,
                            loop=False,
                            quality="high",
                            height=150,
                            width=260,
                            key="denied"
                        )
                        st.error("Limite máximo de 3 cidades para comparação atingido!")
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error("Limite máximo de 3 cidades para comparação atingido!")
        else:
            st.warning(f"{selected_city} já está na lista de comparação")
    
    st.markdown("---")
    st.header("⚙️ Configurações")
    st.markdown("Unidades: °C e km/h")
    
    st.markdown("---")
    if st.session_state.history:
        st.header("📌 Histórico")
        for city in reversed(st.session_state.history[-5:]):
            if st.button(city):
                selected_city = city
    
    st.markdown("---")
    st.markdown("### Sobre")
    st.markdown("Dashboard meteorológico com dados em tempo real e previsão do tempo.")
    st.markdown("Dados fornecidos por [OpenWeatherMap](https://openweathermap.org)")
    st.markdown("Desenvolvido por [William Bruno](https://github.com/willbcs)")

# Funções auxiliares
def display_weather_alert(alerts):
    if alerts:
        unique_alerts = []
        seen_alerts = set()
        
        for alert in alerts:
            if alert not in seen_alerts:
                seen_alerts.add(alert)
                unique_alerts.append(alert)
        
        if unique_alerts:
            st.warning("### ⚠️ Alertas Meteorológicos")
            for alert in unique_alerts:
                st.error(alert)

def display_current_weather(data):
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        flag_img = clima.get_country_flag(data['country'])
        if flag_img:
            st.image(flag_img, width=100)
        st.metric("Temperatura", f"{data['temp']:.1f}°C")
        st.metric("Sensação Térmica", f"{data['feels_like']:.1f}°C")
        st.metric("Umidade", f"{data['humidity']}%")
    
    with col2:
        st.subheader(f"{data['weather_icon']} Condições Atuais em {data['city']}")
        st.markdown(f"**{data['weather_desc']}**")
        
        # Gráfico de radar para vento
        df_wind = pd.DataFrame({
            'Direção': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N'],
            'Velocidade': [data['wind_speed']] * 9
        })
        
        fig_wind = px.line_polar(
            df_wind, r='Velocidade', theta='Direção', 
            line_close=True, title="Direção do Vento",
            template="plotly_dark"
        )
        fig_wind.update_traces(fill='toself')
        st.plotly_chart(fig_wind, use_container_width=True)
    
    with col3:
        st.metric("Pressão Atmosférica", f"{data['pressure']} hPa")
        st.metric("Velocidade do Vento", f"{data['wind_speed']:.1f} km/h")
        st.metric("Nebulosidade", f"{data['clouds']}%")
        st.metric("Visibilidade", f"{data['visibility']:.1f} km")
        st.metric("Nascer do Sol", data['sunrise'])
        st.metric("Pôr do Sol", data['sunset'])
    
    # Mapa da localização
    st.markdown("---")
    st.subheader("🗺️ Localização")
    st.components.v1.iframe(f"https://www.openstreetmap.org/export/embed.html?bbox={data['coord']['lon']-0.1}%2C{data['coord']['lat']-0.1}%2C{data['coord']['lon']+0.1}%2C{data['coord']['lat']+0.1}&layer=mapnik&marker={data['coord']['lat']}%2C{data['coord']['lon']}", height=400)

def display_forecast(data):
    try:
        st.subheader("📅 Previsão para 5 Dias")
        
        # Verificação robusta dos dados de entrada
        if not data or not isinstance(data, dict) or not data.get('forecast'):
            st.warning("Dados de previsão indisponíveis ou em formato inválido.")
            return
            
        # Pré-processamento dos dados
        processed_data = []
        for forecast in data['forecast']:
            # Garante que todos os campos obrigatórios existam
            if not all(key in forecast for key in ['date', 'temp', 'humidity', 'wind_speed', 'pop']):
                st.error("Estrutura de dados incompleta na previsão.")
                return
                
            # Converte probabilidade de chuva para porcentagem se necessário
            pop = forecast['pop']
            if pop <= 1:  # Se estiver entre 0-1, converte para 0-100
                pop = pop * 100
                
            processed_data.append({
                'date': forecast['date'],
                'temp': forecast['temp'],
                'temp_min': forecast.get('temp_min', forecast['temp'] - 2),  # Fallback
                'temp_max': forecast.get('temp_max', forecast['temp'] + 2),  # Fallback
                'humidity': forecast['humidity'],
                'wind_speed': forecast['wind_speed'],
                'pop': pop,
                'weather_main': forecast.get('weather_main', 'N/A'),
                'weather_icon': forecast.get('weather_icon', '❓')
            })
        
        # Cria DataFrame com os dados processados
        df_forecast = pd.DataFrame(processed_data)
        
        # Agrupa por dia para os cards
        df_daily = df_forecast.groupby('date').agg({
            'temp_min': 'min',
            'temp_max': 'max',
            'humidity': 'mean',
            'wind_speed': 'mean',
            'pop': 'max',
            'weather_main': lambda x: x.mode()[0] if not x.mode().empty else 'N/A',
            'weather_icon': lambda x: x.mode()[0] if not x.mode().empty else '❓'
        }).reset_index()
        
        # Renomeia colunas para exibição
        df_daily.columns = ['Data', 'Temp Mín', 'Temp Máx', 'Umidade', 'Vento', 'Chuva', 'Condição', 'Ícone']
        
        # Exibe cards com a previsão diária
        st.markdown("### Previsão Diária")
        cols = st.columns(5)
        for i, row in df_daily.head(5).iterrows():  # Mostra apenas 5 dias
            with cols[i]:
                st.markdown(f"#### {row['Data']}")
                st.markdown(f"{row['Ícone']} {row['Condição']}")
                st.metric("Máxima", f"{row['Temp Máx']:.1f}°C")
                st.metric("Mínima", f"{row['Temp Mín']:.1f}°C")
                st.metric("Chuva", f"{row['Chuva']:.0f}%")
        
        # Gráficos de evolução
        st.markdown("---")
        st.subheader("📊 Análise Detalhada")
        
        # Gráfico 1: Temperatura
        fig_temp = px.line(
            df_daily,
            x='Data',
            y=['Temp Máx', 'Temp Mín'],
            labels={'value': 'Temperatura (°C)', 'variable': 'Legenda'},
            title="Variação de Temperatura",
            color_discrete_map={'Temp Máx': 'red', 'Temp Mín': 'blue'}
        )
        fig_temp.update_traces(
            line=dict(width=2.5),
            marker=dict(size=8)
        )
        st.plotly_chart(fig_temp, use_container_width=True)
        
        # Gráfico 2: Umidade e Chuva
        fig_humidity = go.Figure()
        fig_humidity.add_trace(go.Bar(
            x=df_daily['Data'],
            y=df_daily['Umidade'],
            name='Umidade (%)',
            marker_color='lightblue'
        ))
        fig_humidity.add_trace(go.Scatter(
            x=df_daily['Data'],
            y=df_daily['Chuva'],
            name='Chuva (%)',
            line=dict(color='red'),
            yaxis='y2'
        ))
        fig_humidity.update_layout(
            title='Umidade e Probabilidade de Chuva',
            yaxis=dict(title='Umidade (%)', range=[0, 100]),
            yaxis2=dict(title='Chuva (%)', overlaying='y', side='right', range=[0, 100]),
            hovermode='x unified'
        )
        st.plotly_chart(fig_humidity, use_container_width=True)
        
        # Gráfico 3: Vento
        fig_wind = px.bar(
            df_daily,
            x='Data',
            y='Vento',
            title='Velocidade do Vento (km/h)',
            labels={'Vento': 'Velocidade (km/h)'},
            color='Vento',
            color_continuous_scale='greens'
        )
        st.plotly_chart(fig_wind, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erro ao processar previsão: {str(e)}")
        st.write("Dados recebidos para diagnóstico:", data)  # Debug

def display_comparison(cities):
    # Mensagem quando não há cidades suficientes
    if len(cities) < 2:
        st.info("Adicione cidades para comparação usando o menu lateral")
        return
    
    st.subheader("🆚 Comparação entre Cidades")
    
    # Botão para limpar comparação (versão compatível com todas versões do Streamlit)
    if st.button("❌ Limpar todas as cidades da comparação"):
        st.session_state.compare_cities = []
        # Solução compatível com todas versões:
        if hasattr(st, 'rerun'):
            st.rerun()
        elif hasattr(st, 'experimental_rerun'):
            st.experimental_rerun()
        else:
            raise Exception("Função de rerun não disponível")
        return
    
    # Resto da implementação da comparação
    try:
        all_data = []
        for city in cities:
            try:
                data = clima.get_current_weather(city)
                all_data.append(data)
            except Exception as e:
                st.error(f"Erro ao obter dados para {city}: {str(e)}")
                continue
        
        if len(all_data) < 2:
            st.warning("É necessário pelo menos 2 cidades válidas para comparação")
            return
        
        # [Mantenha aqui todo o resto do seu código de comparação]
        # Gráficos de comparação, tabelas, etc.
        
    except Exception as e:
        st.error(f"Erro ao processar comparação: {str(e)}")
    
    # Gráfico de comparação 1: Temperatura e Sensação Térmica
    fig_temp = go.Figure()
    for data in all_data:
        fig_temp.add_trace(go.Bar(
            x=[f"{data['city']} ({data['country']})"],
            y=[data['temp']],
            name=f"{data['city']} - Temp",
            text=[f"{data['temp']:.1f}°C"],
            textposition='auto'
        ))
        fig_temp.add_trace(go.Bar(
            x=[f"{data['city']} ({data['country']})"],
            y=[data['feels_like']],
            name=f"{data['city']} - Sensação",
            text=[f"{data['feels_like']:.1f}°C"],
            textposition='auto',
            marker=dict(line=dict(width=2, color='black'))
        ))
    
    fig_temp.update_layout(
        title='Comparação de Temperatura (°C)',
        barmode='group',
        showlegend=True
    )
    st.plotly_chart(fig_temp, use_container_width=True)
    
    # Gráfico de comparação 2: Umidade e Vento
    fig_humidity_wind = go.Figure()
    for data in all_data:
        fig_humidity_wind.add_trace(go.Scatterpolar(
            r=[data['humidity'], data['wind_speed'], data['clouds'], data['pressure']/10],
            theta=['Umidade', 'Vento', 'Nebulosidade', 'Pressão'],
            name=f"{data['city']} ({data['country']})",
            fill='toself'
        ))
    
    fig_humidity_wind.update_layout(
        title='Comparação de Variáveis Meteorológicas',
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True
    )
    st.plotly_chart(fig_humidity_wind, use_container_width=True)
    
    # Gráfico de comparação 3: Radar multivariado
    categories = ['Temperatura', 'Sensação', 'Umidade', 'Vento', 'Nebulosidade']
    
    fig_radar = go.Figure()
    for data in all_data:
        fig_radar.add_trace(go.Scatterpolar(
            r=[data['temp'], data['feels_like'], data['humidity'], 
              data['wind_speed'], data['clouds']],
            theta=categories,
            name=f"{data['city']} ({data['country']})",
            fill='toself'
        ))
    
    fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max(40, max([d['temp'] for d in all_data]) + 10)]
        )
    ),
    title="Comparação Multivariada",
    showlegend=True
)
    st.plotly_chart(fig_radar, use_container_width=True)


# Conteúdo principal
st.title("🌦️ Dashboard Meteorológico Avançado")

try:
    if tab == "Visão Atual":
        current_data = clima.get_current_weather(selected_city)
        display_weather_alert(current_data['alerts'])
        display_current_weather(current_data)
    
    elif tab == "Previsão Completa":
        forecast_data = clima.get_forecast(selected_city)
        display_weather_alert([alert for item in forecast_data['forecast'] for alert in item['alerts']])
        display_current_weather(clima.get_current_weather(selected_city))
        display_forecast(forecast_data)
    
    elif tab == "Comparar Cidades":
        if st.session_state.compare_cities:
            display_comparison(st.session_state.compare_cities)
        else:
            st.info("Adicione cidades para comparação usando o menu lateral")

except Exception as e:
    st.error(f"Erro ao obter dados meteorológicos: {str(e)}")

# Rodapé
st.markdown("---")
st.caption(f"Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.caption("Dados fornecidos por OpenWeatherMap")
