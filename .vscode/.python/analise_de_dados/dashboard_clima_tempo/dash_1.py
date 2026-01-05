import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from clima_tempo_1 import ClimaTempo
from PIL import Image
from io import BytesIO
import json
from streamlit_lottie import st_lottie
from typing import Dict, List, Optional

# Configuração da página
st.set_page_config(
    page_title="Dashboard Meteorológico Avançado",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)
    
# Lista de cidades
CITIES = [
    # Capitais do Mundo (adicionadas 15 novas)
    'Abu Dhabi', 'Accra', 'Addis Ababa', 'Algiers', 'Andorra la Vella', 'Ankara', 'Antananarivo', 'Asunción', 'Athens', 'Baghdad',
    'Baku', 'Bamako', 'Bangkok', 'Banjul', 'Beijing', 'Beirut', 'Belgrade', 'Berlin', 'Bern', 'Bishkek',
    'Bogotá', 'Brasília', 'Bratislava', 'Brazzaville', 'Bridgetown', 'Bucharest', 'Budapest', 'Buenos Aires', 'Cairo',
    'Canberra', 'Caracas', 'Castries', 'Chisinau', 'Colombo', 'Conakry', 'Copenhagen', 'Dakar', 'Damascus', 'Dhaka',
    'Dili', 'Dodoma', 'Doha', 'Dublin', 'Dushanbe', 'Freetown', 'Gaborone', 'Georgetown', 'Hanoi', 'Harare',
    'Havana', 'Helsinki', 'Islamabad', 'Jakarta', 'Jerusalem', 'Juba', 'Kabul', 'Kampala', 'Kathmandu',
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
    'Amsterdam', 'Barcelona', 'Belfast', 'Birmingham', 'Boston', 'Brisbane', 'Brno', 'Cape Town',
    'Chicago', 'Dallas', 'Dubai', 'Frankfurt', 'Glasgow', 'Guangzhou', 'Hamburg', 'Houston',
    'Istanbul', 'Johannesburg', 'Kolkata', 'Las Vegas', 'Leeds', 'Liverpool', 'Los Angeles', 'Lyon', 'Manchester', 'Melbourne',
    'Miami', 'Milan', 'Montreal', 'Munich', 'Nagoya', 'Naples', 'New York', 'Osaka', 'Philadelphia', 'Prague',
    'Quebec City', 'Rio de Janeiro', 'Rotterdam', 'San Diego', 'San Francisco', 'Sapporo', 'Seattle', 'Shanghai',
    'Shenzhen', 'Singapore', 'Sydney', 'Taipei', 'Toronto', 'Vancouver', 'Venice', 'Warsaw', 'Zurich',
    'Adelaide', 'Auckland', 'Bangalore', 'Bangkok', 'Barcelona', 'Berlin', 'Bogotá', 'Brisbane', 'Buenos Aires', 'Cairo',
    'Cape Town', 'Caracas', 'Casablanca', 'Copenhagen', 'Delhi', 'Detroit', 'Dhaka', 'Doha', 'Dubai',
    'Dublin', 'Geneva', 'Guadalajara', 'Guatemala City', 'Havana', 'Helsinki', 'Ho Chi Minh City', 'Hong Kong', 'Houston',

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
@st.cache_data
def load_lottie_file(filepath: str) -> Optional[Dict]:
    """Carrega arquivo Lottie com cache"""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

def display_weather_alert(alerts: List[str]) -> None:
    """Exibe alertas meteorológicos formatados (sem repetições)"""
    if alerts:
        unique_alerts = list(dict.fromkeys(alerts))  # Remove duplicatas mantendo a ordem
        with st.container():
            st.markdown("### ⚠️ Alertas e Avisos")
            cols = st.columns(3)
            for i, alert in enumerate(unique_alerts[:3]):  # Mostra até 3 alertas únicos
                with cols[i % 3]:
                    if "⚠️" in alert or "🚨" in alert:
                        st.error(alert)
                    elif "❄️" in alert or "🌧️" in alert:
                        st.warning(alert)
                    else:
                        st.info(alert)

def display_current_weather(data: Dict) -> None:
    """Exibe os dados atuais com layout aprimorado"""
    st.markdown(f"## 🌍 Condições Atuais em {data['city']}, {data['country']}")
    
    # Layout principal
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        # Bandeira e informações básicas
        flag_img = clima.get_country_flag(data['country'])
        if flag_img:
            st.image(flag_img, width=120)
        
        st.metric("Temperatura", f"{data['temp']:.1f}°C", 
                 f"{data['temp_max']:.1f}°C / {data['temp_min']:.1f}°C")
        st.metric("Sensação Térmica", f"{data['feels_like']:.1f}°C")
        
        # Índice de conforto
        comfort = clima.calculate_comfort_index(
            data['temp'], data['humidity'], data['wind_speed'])
        comfort_color = "green" if comfort > 70 else "orange" if comfort > 40 else "red"
        st.markdown(f"**Conforto Térmico:** <span style='color:{comfort_color}'>"
                   f"{comfort:.0f}/100</span>", unsafe_allow_html=True)
    
    with col2:
        # Condições principais
        st.markdown(f"<h1 style='text-align: center; font-size: 3.5rem;'>{data['weather_icon']} "
                   f"{data['weather_desc']}</h1>", unsafe_allow_html=True)
        
        # Gráfico de radar multivariado
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=[data['temp'], data['humidity'], data['wind_speed'], 
              data['clouds'], data['pressure']/10],
            theta=['Temperatura', 'Umidade', 'Vento', 'Nebulosidade', 'Pressão'],
            fill='toself',
            name='Condições Atuais'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            height=300,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig, use_container_width=True, use_container_height=True)
    
    with col3:
        # Informações detalhadas
        st.metric("Umidade", f"{data['humidity']}%")
        st.metric("Pressão", f"{data['pressure']} hPa")
        st.metric("Vento", f"{data['wind_speed']:.1f} km/h", 
                 f"Rajadas: {data.get('wind_gust', 0):.1f} km/h")
        st.metric("Visibilidade", f"{data['visibility']:.1f} km")
        
        try:
            # Extrair apenas a parte do horário (assumindo formato 'YYYY-MM-DD HH:MM')
            sunrise_time = data['sunrise'].split()[1] if isinstance(data['sunrise'], str) else ""
            sunset_time = data['sunset'].split()[1] if isinstance(data['sunset'], str) else ""
            
            st.metric("Nascer do Sol", sunrise_time)
            st.metric("Pôr do Sol", sunset_time)
        except (ValueError, KeyError, AttributeError) as e:
            st.error(f"Erro ao processar horários do sol: {e}")
    
    # Linha divisória
    st.markdown("---")
    
    # Seção secundária
    col4, col5 = st.columns(2)
    
    with col4:
        # Mapa de localização
        st.subheader("🗺️ Localização")
        st.components.v1.iframe(f"https://www.openstreetmap.org/export/embed.html?bbox={data['coord']['lon']-0.1}%2C{data['coord']['lat']-0.1}%2C{data['coord']['lon']+0.1}%2C{data['coord']['lat']+0.1}&layer=mapnik&marker={data['coord']['lat']}%2C{data['coord']['lon']}", height=400)

    
    with col5:
        st.markdown("### 🌬️ Direção do Vento")

        wind_deg = data.get("wind_deg", 0)
        wind_speed = data["wind_speed"]

        # Criando DataFrame com ponto central e seta (linha de direção)
        df_arrow = pd.DataFrame({
            "r": [0, wind_speed],
            "theta": [0, wind_deg]
        })

        wind_fig = go.Figure()

        wind_fig.add_trace(go.Scatterpolar(
            r=df_arrow["r"],
            theta=df_arrow["theta"],
            mode="lines+markers",
            line=dict(color="darkred", width=4),
            marker=dict(size=8),
            name=f"{wind_deg:.0f}°"
        ))

        # Definindo os pontos cardeais
        cardeais = ['N', 'NE', 'L', 'SE', 'S', 'SO', 'O', 'NO', 'N']
        angulos = [0, 45, 90, 135, 180, 225, 270, 315, 360]

        wind_fig.update_layout(
            polar=dict(
                angularaxis=dict(
                    direction="clockwise",
                    rotation=90,
                    tickvals=angulos,     # Posições angulares
                    ticktext=cardeais,    # Rótulos correspondentes
                    tickmode='array',      # Usar array personalizado
                    tickfont=dict(color="crimson")
                ),
                radialaxis=dict(
                    range=[0, max(10, wind_speed + 1)],
                    tickfont=dict(color="crimson") # Define a cor dos números do eixo radial para vermelho
                )
            ),
            showlegend=False,
            height=350,
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.plotly_chart(wind_fig, use_container_width=True)

def display_forecast(data: Dict) -> None:
    """Exibe previsão do tempo com visualizações avançadas"""
    st.markdown("## 📅 Previsão para 5 Dias")
    
    # Processa os dados para DataFrame
    df = pd.DataFrame(data['forecast'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Agregação diária
    df_daily = df.groupby('date').agg({
        'temp': ['mean', 'min', 'max'],
        'humidity': 'mean',
        'wind_speed': 'max',
        'pop': 'max',
        'rain': 'sum',
        'weather_main': lambda x: x.mode()[0],
        'weather_icon': lambda x: x.mode()[0]
    }).reset_index()
    
    df_daily.columns = ['Data', 'Temp Média', 'Temp Mín', 'Temp Máx', 
                       'Umidade', 'Vento Máx', 'Chuva %', 'Chuva Total', 
                       'Condição', 'Ícone']
    
    # Seção 1: Resumo Diário
    st.markdown("### 🌤️ Resumo Diário")
    cols = st.columns(5)
    for i, row in df_daily.iterrows():
        with cols[i % 5]:
            with st.container(border=True):
                st.markdown(f"**{row['Data']}**")
                st.markdown(f"{row['Ícone']} {row['Condição']}")
                st.metric("Máx/Mín", f"{row['Temp Máx']:.1f}°C / {row['Temp Mín']:.1f}°C")
                st.metric("Chuva", f"{row['Chuva Total']:.1f}mm" if row['Chuva Total'] > 0 else "-")
                st.metric("Vento", f"{row['Vento Máx']:.1f} km/h")
    
    st.markdown("---")
    
    # Seção 2: Gráficos Detalhados
    st.markdown("### 📊 Análise Detalhada")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Temperatura", "Chuva e Umidade", "Vento", "Radar Diário"
    ])
    
    with tab1:
        fig_temp = go.Figure()
        fig_temp.add_trace(go.Scatter(
            x=df['datetime'], y=df['temp'],
            name='Temperatura',
            line=dict(color='red', width=2),
            mode='lines+markers'
        ))
        fig_temp.add_trace(go.Scatter(
            x=df['datetime'], y=df['feels_like'],
            name='Sensação Térmica',
            line=dict(color='orange', width=2, dash='dot')
        ))
        fig_temp.update_layout(
            title='Variação de Temperatura (°C)',
            yaxis_title='Temperatura (°C)',
            hovermode='x unified'
        )
        st.plotly_chart(fig_temp, use_container_width=True)
    
    with tab2:
        fig_rain = go.Figure()
        fig_rain.add_trace(go.Bar(
            x=df['datetime'], y=df['rain'],
            name='Chuva (mm)',
            marker_color='blue'
        ))
        fig_rain.add_trace(go.Scatter(
            x=df['datetime'], y=df['humidity'],
            name='Umidade (%)',
            yaxis='y2',
            line=dict(color='green')
        ))
        fig_rain.update_layout(
            title='Precipitação e Umidade',
            yaxis=dict(title='Chuva (mm)'),
            yaxis2=dict(title='Umidade (%)', overlaying='y', side='right'),
            hovermode='x unified'
        )
        st.plotly_chart(fig_rain, use_container_width=True)
    
    with tab3:
        fig_wind = px.scatter_polar(
            df, r='wind_speed', theta='wind_deg',
            color='wind_speed', size='wind_gust',
            color_continuous_scale='thermal',
            title='Direção e Intensidade do Vento'
        )
        st.plotly_chart(fig_wind, use_container_width=True)
    
    with tab4:
        fig_radar = go.Figure()
        
        for day in df_daily['Data'].unique()[:3]:  # Mostra até 3 dias
            day_data = df[df['date'] == day]
            fig_radar.add_trace(go.Scatterpolar(
                r=[
                    day_data['temp'].mean(),
                    day_data['humidity'].mean(),
                    day_data['wind_speed'].max(),
                    day_data['pop'].max(),
                    day_data['rain'].sum()
                ],
                theta=['Temp', 'Umidade', 'Vento', 'Chuva%', 'Precip'],
                name=day,
                fill='toself'
            ))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            title="Comparação Diária (Médias)"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

def display_comparison(cities: List[str]) -> None:
    """Exibe comparação entre cidades com análise multivariada"""
    if len(cities) < 2:
        st.info("🔍 Adicione pelo menos 2 cidades para comparação")
        return
    
    st.markdown(f"## 🆚 Comparando {len(cities)} Cidades")
    
    # Botão para limpar comparação
    if st.button("❌ Limpar Comparação", type='primary'):
        st.session_state.compare_cities = []
        st.rerun()
    
    # Obtém dados de todas as cidades
    all_data = []
    for city in cities:
        try:
            data = clima.get_current_weather(city)
            all_data.append(data)
        except Exception as e:
            st.error(f"Erro ao obter dados para {city}: {str(e)}")
            continue
    
    if len(all_data) < 2:
        st.warning("Nenhuma cidade válida para comparação")
        return
    
    # Cria DataFrame para análise
    df = pd.DataFrame(all_data)
    
    # Layout de abas
    tab1, tab2, tab3 = st.tabs([
        "Visão Geral", "Análise Térmica", "Radar Comparativo"
    ])
    
    with tab1:
        # Tabela comparativa
        st.dataframe(
            df[['city', 'country', 'temp', 'humidity', 'wind_speed', 'weather_desc']]
            .rename(columns={
                'city': 'Cidade',
                'country': 'País',
                'temp': 'Temp (°C)',
                'humidity': 'Umidade (%)',
                'wind_speed': 'Vento (km/h)',
                'weather_desc': 'Condição'
            }),
            hide_index=True,
            use_container_width=True
        )
    
    with tab2:
        # Gráfico de comparação térmica
        fig = go.Figure()
        
        for data in all_data:
            fig.add_trace(go.Bar(
                x=[data['city']],
                y=[data['temp']],
                name=data['city'],
                text=[f"{data['temp']:.1f}°C"],
                textposition='auto',
                marker_color=px.colors.sequential.Teal[-3]
            ))
        
        fig.update_layout(
            title='Comparação de Temperatura',
            yaxis_title='Temperatura (°C)',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Heatmap de variáveis
        st.markdown("### 🔥 Mapa de Calor de Variáveis")
        fig_heat = px.imshow(
            df[['temp', 'humidity', 'wind_speed', 'pressure']].T,
            labels=dict(x="Cidade", y="Variável", color="Valor"),
            x=df['city'],
            y=['Temp', 'Umidade', 'Vento', 'Pressão'],
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    
    with tab3:
        # Radar multivariado
        st.markdown("### 📊 Radar Comparativo")
        
        categories = ['Temperatura', 'Umidade', 'Vento', 'Nebulosidade', 'Pressão']
        
        fig_radar = go.Figure()
        
        for data in all_data:
            fig_radar.add_trace(go.Scatterpolar(
                r=[data['temp'], data['humidity'], data['wind_speed'],
                  data['clouds'], data['pressure']/10],
                theta=categories,
                name=f"{data['city']} ({data['country']})",
                fill='toself'
            ))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            showlegend=True
        )
        st.plotly_chart(fig_radar, use_container_width=True)

# Inicialização do app
clima = ClimaTempo("69ddec2d6c8acd5a481e1c6959e64262")

# Session State
if 'history' not in st.session_state:
    st.session_state.history = []
if 'compare_cities' not in st.session_state:
    st.session_state.compare_cities = []

# Sidebar
with st.sidebar:
    st.title("🌦️ Navegação")
    
    # Seletor de visualização
    tab = st.radio(
        "Modo de Visualização:",
        ["Visão Atual", "Previsão Completa", "Comparar Cidades"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.title("🔍 Seleção")
    
    # Seletor de cidade
    selected_city = st.selectbox(
        "Escolha uma cidade:",
        CITIES,
        index=CITIES.index('São Paulo')
    )
    
    # Botões de ação
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📌 Adicionar ao Histórico", help="Guarda a cidade no histórico"):
            if selected_city not in st.session_state.history:
                st.session_state.history.append(selected_city)
                anim = load_lottie_file("confirm.json")
                if anim:
                    st_lottie(anim, height=80, key="hist_add", loop=False)
                st.toast(f"{selected_city} adicionada ao histórico")
            else:
                st.warning("A Cidade já foi adicionada!")

    with col2:
        if st.button("🆚 Adicionar para Comparar", help="Adiciona para comparação múltipla"):
            if selected_city not in st.session_state.compare_cities:
                if len(st.session_state.compare_cities) < 5:
                    st.session_state.compare_cities.append(selected_city)
                    anim = load_lottie_file("confirm.json")
                    if anim:
                        st_lottie(anim, height=80, key="comp_add", loop=False)
                    st.toast(f"{selected_city} adicionada para comparação")
                else:
                    anim = load_lottie_file("denied.json")
                    if anim:
                        st_lottie(anim, height=80, key="comp_deny", loop=False)
                    st.error("Máximo de 5 cidades para comparação")
            else:
                st.warning("A Cidade já foi adicionada!")
    st.markdown("---")
    
    # Histórico rápido
    if st.session_state.history:
        st.title("📌 Histórico")
        for city in reversed(st.session_state.history[-5:]):
            if st.button(city, key=f"hist_{city}"):
                selected_city = city
    
    st.markdown("---")
    
    # Configurações
    st.title("⚙️ Configurações")
    unit_system = st.radio(
        "Sistema de Unidades:",
        ["Métrico (°C, km/h)", "Imperial (°F, mph)"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("Desenvolvido por [William Bruno](https://github.com/willbcs)")
    st.markdown("Dados: [OpenWeatherMap](https://openweathermap.org)")

# Conteúdo principal
st.title("🌦️ Dashboard Meteorológico Avançado")

try:
    if tab == "Visão Atual":
        current_data = clima.get_current_weather(selected_city, 'metric' if unit_system.startswith('Métrico') else 'imperial')
        display_weather_alert(current_data['alerts'])
        display_current_weather(current_data)
    
    elif tab == "Previsão Completa":
        forecast_data = clima.get_forecast(selected_city, 'metric' if unit_system.startswith('Métrico') else 'imperial')
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