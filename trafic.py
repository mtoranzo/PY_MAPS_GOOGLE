# python -m venv venv
# ./venv/Scripts/Activate.ps1
# pip install -r requirements.txt
# python here.py
# deactivate

import requests

# Reemplaza 'TU_CLAVE_DE_API' con tu clave de API de Google Maps
API_KEY = 'TU_CLAVE_DE_API'

# Coordenadas de puntos de interés
locations = [
    {"name": "Santo Domingo", "lat": 18.4861, "lng": -69.9312},  # Capital, alto tráfico y centros comerciales
    {"name": "Santiago", "lat": 19.4500, "lng": -70.7000},  # Segunda ciudad más grande, importante comercialmente
    {"name": "Punta Cana", "lat": 18.5820, "lng": -68.4057},  # Destino turístico principal
    {"name": "Puerto Plata", "lat": 19.7732, "lng": -70.6944},  # Destino turístico en la costa norte
    {"name": "La Romana", "lat": 18.4231, "lng": -68.9711},  # Área turística, incluyendo Casa de Campo
    {"name": "Higuey", "lat": 18.5775, "lng": -68.7064},  # Ciudad cercana a la zona turística de Punta Cana
    {"name": "Boca Chica", "lat": 18.4639, "lng": -69.6094},  # Playa popular y de fácil acceso desde Santo Domingo
    {"name": "Samaná", "lat": 19.2131, "lng": -69.3375},  # Destino turístico en el noreste
    {"name": "Barahona", "lat": 18.2197, "lng": -71.1206},  # Región sur con alto potencial turístico
    {"name": "La Vega", "lat": 19.2172, "lng": -70.5356},  # Ciudad central, conocida por sus festividades
    {"name": "San Cristóbal", "lat": 18.4333, "lng": -70.1167},  # Ciudad cerca de Santo Domingo
    {"name": "San Pedro de Macorís", "lat": 18.4578, "lng": -69.2983},  # Importante ciudad industrial y comercial
    {"name": "San Juan de la Maguana", "lat": 18.8017, "lng": -71.2139},  # Ciudad importante en el suroeste
    {"name": "Azua", "lat": 18.4358, "lng": -70.7361},  # Ciudad de importancia agrícola
    {"name": "Montecristi", "lat": 19.8189, "lng": -71.6547},  # Área en la costa norte
    {"name": "El Seibo", "lat": 18.6897, "lng": -68.9297},  # Región este, cerca de la zona turística
    {"name": "La Altagracia", "lat": 18.8000, "lng": -68.5250},  # Provincia con importantes puntos turísticos
    {"name": "Santiago Rodríguez", "lat": 19.2340, "lng": -71.1761},  # Región agrícola y cultural
    {"name": "Las Terrenas", "lat": 19.1981, "lng": -69.4242},  # Destino turístico en la península de Samaná
    {"name": "Nagua", "lat": 19.3422, "lng": -69.8500},  # Ciudad costera en el noreste
    {"name": "Pedernales", "lat": 18.1361, "lng": -71.7500},  # Región sur, conocida por su belleza natural
    {"name": "Cotuí", "lat": 19.0733, "lng": -70.2350},  # Ciudad en el centro del país
    {"name": "Villa Mella", "lat": 18.5550, "lng": -69.9325},  # Zona suburbana de Santo Domingo
    {"name": "Bani", "lat": 18.2542, "lng": -70.3219},  # Ciudad en la región sur
    {"name": "Salcedo", "lat": 19.2411, "lng": -70.5250},  # Ciudad en la región norte
    {"name": "Constanza", "lat": 18.9222, "lng": -70.8917},  # Destino turístico en las montañas
    {"name": "Santo Domingo Este", "lat": 18.4730, "lng": -69.8650},  # Ciudad con alto desarrollo urbano
    {"name": "Santo Domingo Oeste", "lat": 18.4764, "lng": -69.9316},  # Zona metropolitana de la capital
    {"name": "Santo Domingo Norte", "lat": 18.5325, "lng": -69.8544},  # Zona suburbana de la capital
    {"name": "Jarabacoa", "lat": 19.1167, "lng": -70.6333},  # Ciudad montañosa conocida por su clima fresco
    {"name": "Moca", "lat": 19.3933, "lng": -70.5250},  # Ciudad agrícola en la región norte
    {"name": "Bonao", "lat": 18.9333, "lng": -70.4167},  # Ciudad en el centro del país
    {"name": "San Francisco de Macorís", "lat": 19.3000, "lng": -70.2500},  # Ciudad importante en la región noreste
    {"name": "Neiba", "lat": 18.4811, "lng": -71.4194}  # Ciudad en la región suroeste
]

def get_traffic_speed(location):
    # Coordenadas del punto de interés
    lat = location['lat']
    lng = location['lng']
    
    # Coordenadas de un punto cercano para simular una ruta
    nearby_lat = lat + 0.01
    nearby_lng = lng + 0.01
    
    # URL de la API de Google Maps Roads
    url = f'https://roads.googleapis.com/v1/snapToRoads?path={lat},{lng}|{nearby_lat},{nearby_lng}&interpolate=true&key={API_KEY}'
    
    # Realizar la solicitud a la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        
        # Verificar si se obtuvieron puntos de la ruta
        if 'snappedPoints' in data:
            print(f"Información del tráfico en la zona de {location['name']}:")
            for point in data['snappedPoints']:
                print(f"Coordenadas: {point['location']['latitude']}, {point['location']['longitude']}")
                print(f"Distancia desde el inicio: {point['originalIndex']} metros")
        else:
            print(f"No se pudo obtener información del tráfico para la zona de {location['name']}")
    else:
        print(f"Error al obtener información del tráfico para la zona de {location['name']}")

# Obtener información del tráfico en las zonas de los puntos de interés
for location in locations:
    get_traffic_speed(location)