# Get Weas Measure 📊

Sistema completo de gestión de mediciones con interfaz web interactiva.

## 🎯 Características

✅ **Registro de Mediciones** - Interfaz intuitiva para agregar nuevos datos  
✅ **Almacenamiento en Excel** - Todos los datos se guardan automáticamente  
✅ **Panel de Control** - Dashboard con métricas y tendencias  
✅ **Análisis Avanzado** - Estadísticas, gráficos e insights  
✅ **Sistema de Alertas** - Notificaciones cuando se exceden límites  
✅ **Filtros y Búsqueda** - Encuentra datos fácilmente  
✅ **Exportación** - Descarga reportes en CSV  
✅ **Historial Completo** - Acceso a todos los registros  

---

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes Python)

### Instalación Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/ricardohty-crypto/Get-Weas-Measure.git
cd Get-Weas-Measure

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 🌐 Deployment en Streamlit Cloud (RECOMENDADO)

### Paso 1: Preparar repositorio
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Paso 2: Deploy
1. Ve a [https://share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con GitHub
3. Selecciona tu repositorio
4. Elige `app.py` como main file
5. ¡Haz clic en Deploy!

Tu aplicación estará disponible en minutos.

---

## 📖 Guía de Uso

### 📈 Panel Principal
- Visualiza métricas generales
- Monitorea alertas activas
- Consulta la última medición

### ➕ Nueva Medición
- Completa el formulario con los datos
- Selecciona tipo, ubicación y unidad
- Agrega notas si es necesario
- ¡Guarda automáticamente en Excel!

### 📋 Historial
- Visualiza todas tus mediciones
- Filtra por tipo, ubicación o fecha
- Exporta datos como CSV

### 📊 Análisis
- Estadísticas detalladas (promedio, máximo, mínimo, etc.)
- Gráficos interactivos
- Análisis por ubicación

### ⚙️ Configuración
- Información del sistema
- Opciones de mantenimiento
- Revisión de límites de alerta

---

## 📊 Estructura del Proyecto

```
Get-Weas-Measure/
├── app.py                      # Aplicación principal (Streamlit)
├── gestor_mediciones.py        # Lógica de gestión de datos
├── config.py                   # Configuración de tipos y límites
├── requirements.txt            # Dependencias Python
├── README.md                   # Este archivo
├── DEPLOY.md                   # Guía de deployment
├── .gitignore                  # Archivos a ignorar
└── mediciones.xlsx             # Base de datos (se crea automáticamente)
```

---

## ⚙️ Configuración Personalizada

Edita `config.py` para personalizar:

### Agregar nuevo tipo de medición
```python
TIPOS_MEDICIONES = [
    "Temperatura",
    "Mi Medición Custom",  # ← Agregar aquí
    ...
]
```

### Modificar límites de alerta
```python
LIMITES_ALERTA = {
    "Temperatura": 50.0,    # Cambiar este valor
    ...
}
```

### Agregar nuevas ubicaciones
```python
UBICACIONES = [
    "Laboratorio A",
    "Mi Ubicación Custom",  # ← Agregar aquí
    ...
]
```

---

## 📁 Datos

Los datos se almacenan en `mediciones.xlsx` con las siguientes columnas:

| Campo | Descripción |
|-------|-----------|
| Tipo | Tipo de medición |
| Valor | Valor numérico |
| Unidad | Unidad de medida |
| Ubicacion | Lugar donde se midió |
| Usuario | Quién realizó la medición |
| Fecha | Fecha del registro |
| Hora | Hora del registro |
| Notas | Observaciones adicionales |
| Timestamp | Marca de tiempo automática |

---

## 🆘 Troubleshooting

### Error: "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Error: "Permission denied"
```bash
chmod +x app.py
```

### La aplicación es lenta
- Verifica que el archivo Excel no sea muy grande
- Considera archivar datos antiguos

### Los datos no se guardan
- Verifica permisos de escritura en la carpeta
- Asegúrate que Excel no esté abierto en otra aplicación

---

## 🔒 Seguridad

- Los datos se almacenan localmente en tu máquina
- Haz backups regulares de `mediciones.xlsx`
- No compartas el archivo si contiene datos sensibles

---

## 📝 Licencia

Este proyecto está disponible bajo licencia MIT.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Abre un issue o pull request para sugerencias.

---

## 📞 Soporte

Si tienes preguntas o problemas:
1. Revisa la guía de deployment (`DEPLOY.md`)
2. Consulta la documentación de Streamlit: https://docs.streamlit.io
3. Abre un issue en GitHub

---

**¡Gracias por usar Get Weas Measure! 🎉**

Hecho con ❤️ | 2026
