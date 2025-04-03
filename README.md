# PY_MAPS_GOOGLE

## Descripción
PY_MAPS_GOOGLE es una aplicación diseñada para interactuar con la API de Google Maps, permitiendo realizar consultas como geocodificación, cálculo de rutas, búsqueda de lugares y más. Es ideal para desarrolladores que necesitan integrar funcionalidades de mapas en sus proyectos.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/PY_MAPS_GOOGLE.git
   cd PY_MAPS_GOOGLE
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu clave de API de Google Maps:
   - Crea un archivo `.env` en la raíz del proyecto.
   - Agrega la siguiente línea con tu clave de API:
     ```
     GOOGLE_MAPS_API_KEY=tu_clave_api
     ```

## Uso
1. Ejecuta el script principal:
   ```bash
   python main.py
   ```

2. Sigue las instrucciones en la terminal para realizar consultas a la API de Google Maps.

3. Personaliza las funcionalidades editando los scripts según tus necesidades.

## Requisitos
- Python 3.7 o superior.
- Una clave de API válida de Google Maps.

## Notas
- Asegúrate de habilitar los servicios necesarios en la consola de Google Cloud (como Geocoding API, Directions API, etc.).
- Consulta la documentación oficial de Google Maps para más detalles sobre las funcionalidades disponibles.