# Documentación

## Requisitos
1.- Python 3<br>
2.- Pip cómo gestor de paquetes (para poder seguir esta guía) <br>

## Instalación

1.- Clonación del repositorio

```
$ git clone https://github.com/GeoCurguan/INFO290-Locust.git
```
2.- Ir al directorio del proyecto <br>
3.- Instalar dependencias 
```
$ pip install -r requirements.txt
```


## Ejecución de pruebas
1.- Abrir dos terminales en el proyecto <br>
2.- Ejecutar la API
```
$ uvicorn main:app
```
3.- Ejecutar Locust
```
locust -f locustfile.py --host http://127.0.0.1:8000
```

4.- Abrir el navegador e ir al dashboard de Locust (por defecto: http://localhost:8089/)
