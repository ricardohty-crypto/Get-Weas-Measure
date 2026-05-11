````markdown name=DEPLOY.md
# 🚀 Guía de Deployment

Diferentes formas de desplegar tu aplicación de mediciones.

## 📋 Contenido

1. [Streamlit Cloud](#streamlit-cloud-recomendado)
2. [Heroku](#heroku)
3. [DigitalOcean](#digitalocean)
4. [AWS](#aws)
5. [Local](#ejecución-local)

---

## ☁️ Streamlit Cloud (RECOMENDADO)

**Ventajas:**
- ✅ Gratis
- ✅ Muy fácil de configurar
- ✅ Actualizaciones automáticas desde GitHub
- ✅ Sin necesidad de tarjeta de crédito

### Pasos

1. **Ir a Streamlit Cloud**
   - Abre [https://share.streamlit.io](https://share.streamlit.io)
   - Inicia sesión con GitHub

2. **Crear nueva app**
   - Haz clic en "New app"
   - Selecciona:
     - **Repository:** `ricardohty-crypto/Get-Weas-Measure`
     - **Branch:** `main`
     - **Main file path:** `app.py`

3. **Deploy**
   - Haz clic en "Deploy"
   - Espera 2-3 minutos
   - ¡Tu app estará en línea!

4. **URL de tu app**
   ```
   https://[nombre-app].streamlit.app
   ```

### Configurar dominio personalizado

1. Compra un dominio (GoDaddy, Namecheap, etc.)
2. En Streamlit Cloud:
   - Ve a "Settings"
   - Agrega tu dominio personalizado
   - Configura los DNS según las instrucciones

---

## 🎪 Heroku

**Ventajas:**
- ✅ Fácil de usar
- ✅ Buena documentación
- ⚠️ Requiere tarjeta de crédito (dyno hours gratis limitados)

### Pasos

1. **Instalar Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku

   # Windows (descargar desde)
   https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Crear archivos necesarios**

   **Procfile:**
   ```
   web: streamlit run --server.port=$PORT app.py
   ```

   **runtime.txt:**
   ```
   python-3.10.12
   ```

3. **Crear app en Heroku**
   ```bash
   heroku login
   heroku create nombre-de-tu-app
   ```

4. **Desplegar**
   ```bash
   git push heroku main
   ```

5. **Ver logs**
   ```bash
   heroku logs --tail
   ```

6. **Tu app estará en**
   ```
   https://nombre-de-tu-app.herokuapp.com
   ```

### Notas sobre almacenamiento

⚠️ **IMPORTANTE:** Heroku tiene un sistema de archivos efímero. Los datos en `mediciones.xlsx` se perderán al reiniciar.

**Soluciones:**
- Usar una base de datos (PostgreSQL, MongoDB)
- Guardar en Google Drive
- Usar AWS S3

---

## 🌊 DigitalOcean

**Ventajas:**
- ✅ Buen rendimiento
- ✅ Control total del servidor
- ⚠️ Requiere $4-6 USD/mes

### Pasos

1. **Crear Droplet**
   - Ve a [digitalocean.com](https://digitalocean.com)
   - Crea un nuevo Droplet
   - Elige: Ubuntu 22.04 LTS, $4/mes

2. **SSH a tu servidor**
   ```bash
   ssh root@tu_ip
   ```

3. **Instalar dependencias**
   ```bash
   apt update
   apt install -y python3 python3-pip git
   ```

4. **Clonar repositorio**
   ```bash
   git clone https://github.com/ricardohty-crypto/Get-Weas-Measure.git
   cd Get-Weas-Measure
   ```

5. **Instalar Python packages**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Instalar y configurar Nginx**
   ```bash
   apt install -y nginx
   ```

7. **Crear archivo de configuración Nginx**
   ```
   /etc/nginx/sites-available/streamlit
   ```
   
   Contenido:
   ```nginx
   server {
       listen 80;
       server_name tu_dominio.com;

       location / {
           proxy_pass http://127.0.0.1:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

8. **Habilitar sitio**
   ```bash
   ln -s /etc/nginx/sites-available/streamlit /etc/nginx/sites-enabled/
   nginx -t
   systemctl restart nginx
   ```

9. **Ejecutar Streamlit (en background)**
   ```bash
   nohup streamlit run app.py --server.port 8501 &
   ```

10. **Acceder a tu app**
    ```
    http://tu_dominio.com
    ```

### SSL/HTTPS (Recomendado)

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d tu_dominio.com
```

---

## ☁️ AWS

**Ventajas:**
- ✅ Muy escalable
- ✅ Muchas opciones
- ⚠️ Puede ser caro
- ⚠️ Más complejo de configurar

### Opción 1: EC2

Similar a DigitalOcean:
1. Crea instancia EC2 (Ubuntu)
2. Sigue pasos de DigitalOcean
3. Configura Security Groups

### Opción 2: Elastic Beanstalk

1. Instalar AWS CLI
2. Crear archivo `.ebextensions/python.config`
3. Deploy con `eb create`

### Opción 3: Lambda + API Gateway

Para casos más avanzados. Consulta documentación oficial.

---

## 💻 Ejecución Local

### Requiere:
- Python 3.8+
- pip

### Pasos

```bash
# Clonar
git clone https://github.com/ricardohty-crypto/Get-Weas-Measure.git
cd Get-Weas-Measure

# Entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar
pip install -r requirements.txt

# Ejecutar
streamlit run app.py
```

### Con Docker

1. **Crear Dockerfile:**
   ```dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   CMD ["streamlit", "run", "app.py"]
   ```

2. **Build y run:**
   ```bash
   docker build -t mediciones .
   docker run -p 8501:8501 mediciones
   ```

---

## 📊 Comparativa de Opciones

| Opción | Costo | Facilidad | Almacenamiento | Escalabilidad |
|--------|-------|-----------|----------------|---------------|
| Streamlit Cloud | Gratis | ⭐⭐⭐⭐⭐ | Local | Media |
| Heroku | $0-50/mes | ⭐⭐⭐⭐ | Efímero ⚠️ | Media |
| DigitalOcean | $4-6/mes | ⭐⭐⭐ | Persistente | Alta |
| AWS | Variable | ⭐⭐ | Varios | Muy Alta |
| Local | Gratis | ⭐⭐⭐⭐ | Local | Baja |

---

## 🔄 Problemas Comunes

### 1. Aplicación muy lenta
- Aumenta recursos del servidor
- Optimiza queries a Excel
- Considera base de datos

### 2. Datos desaparecen en Heroku
- Usa base de datos
- O usa Streamlit Cloud

### 3. Error: "Port already in use"
```bash
# Cambiar puerto
streamlit run app.py --server.port 8502
```

### 4. CORS errors
- Configura headers en servidor
- O usa proxy

---

## 🔒 Seguridad

### Recomendaciones

1. **Usar HTTPS/SSL**
   - Especialmente en producción
   - Usar Let's Encrypt (gratis)

2. **Autenticación**
   - Considerar agregar login
   - Proteger datos sensibles

3. **Backups**
   - Hacer backup regular de `mediciones.xlsx`
   - Guardar en Google Drive o S3

4. **Monitoreo**
   - Configurar alertas
   - Revisar logs regularmente

---

## 📞 Soporte

Si tienes problemas:

1. Revisa logs
2. Consulta documentación de Streamlit
3. Abre issue en GitHub

---

**¡Feliz deployment! 🎉**
````
