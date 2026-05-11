# Configuración de Get Weas Measure

# Tipos de mediciones disponibles
TIPOS_MEDICIONES = [
    "Temperatura",
    "Presión",
    "Humedad",
    "Velocidad",
    "Distancia",
    "Peso",
    "Voltaje",
    "Corriente",
    "pH",
    "Concentración"
]

# Ubicaciones de medición
UBICACIONES = [
    "Laboratorio A",
    "Laboratorio B",
    "Oficina",
    "Almacén",
    "Campo",
    "Exterior",
    "Sala de Pruebas"
]

# Unidades de medida
UNIDADES = [
    "°C",
    "°F",
    "K",
    "Pa",
    "kPa",
    "Bar",
    "psi",
    "%",
    "m/s",
    "km/h",
    "m",
    "cm",
    "mm",
    "kg",
    "g",
    "lb",
    "V",
    "mV",
    "A",
    "mA",
    "Ω",
    "kΩ",
    "pH",
    "ppm",
    "%w/w",
    "mol/L"
]

# Límites de alerta para cada tipo de medición
LIMITES_ALERTA = {
    "Temperatura": 40.0,
    "Presión": 100.0,
    "Humedad": 80.0,
    "Velocidad": 50.0,
    "Distancia": 100.0,
    "Peso": 500.0,
    "Voltaje": 220.0,
    "Corriente": 10.0,
    "pH": 7.5,
    "Concentración": 100.0
}

# Configuración de la interfaz
TITULO_APP = "Get Weas Measure"
SUBTITULO_APP = "Plataforma de Gestión de Mediciones"
ICONO_APP = "📊"

# Colores personalizados (paleta de colores)
COLORES = {
    "primario": "#667eea",
    "secundario": "#764ba2",
    "exito": "#10b981",
    "peligro": "#ef4444",
    "advertencia": "#f59e0b"
}

# Configuración de almacenamiento
ARCHIVO_DATOS = "mediciones.xlsx"
HOJA_EXCEL = "Mediciones"

# Número de registros a mostrar por página
REGISTROS_POR_PAGINA = 50

# Formato de fechas
FORMATO_FECHA = "%Y-%m-%d"
FORMATO_HORA = "%H:%M:%S"

# Idioma
IDIOMA = "es"  # español

# Usuario por defecto
USUARIO_DEFECTO = "Admin"
