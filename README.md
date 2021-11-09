Instituto Tecnológico de Costa Rica <br>
Campus Tecnológico Local San Carlos <br>
Principios de Sistemas Operativos - II Semestre 2021 <br>

Proyecto creado por:
-  [![Github](https://img.shields.io/badge/Github-Eduardo_Binns-100000?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/EdBinns) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Eduardo_Binns-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/eduar-binns)
-  [![Github](https://img.shields.io/badge/GitHub-Anthony_Griffith-100000?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/AnthonyGriffith) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Anthony_Griffith-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/anthony-griffith/)
-   [![Github](https://img.shields.io/badge/GitHub-Andres_Mora-100000?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/amorabarrantes)[![LinkedIn](https://img.shields.io/badge/LinkedIn-Andres_Mora-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/andres-mora-barrantes-144475192/)

# Azure Cognitive Services
Cognitive Services pone la inteligencia artificial al alcance de todos los desarrolladores y científicos de datos. Con los modelos principales, se pueden desbloquear
diversos casos de uso. Basta con una llamada API para incorporar la capacidad de ver, escuchar, hablar, buscar, comprender y acelerar la toma de decisiones avanzadas 
en las aplicaciones. Permitaque los desarrolladores y científicos de datos de todos los niveles de conocimiento puedan agregar fácilmente características de inteligencia 
artificial a sus aplicaciones.

# Analizador de archivos multimedia con Azure Cognitive Services
Con este proyecto se tenían dos objetivos, primeramente poder analizar en base a una imagen de una persona los sentimientos que está refleja, lo cual podria ser bastante util a 
la hora de analizar por ejemplo, el efecto positivo o negativo que puede llegar a tener un producto o la atención que se le brinda a un cliente. Ademas, lo siguiente lo que se busca es
poder analizar algo similar al anterior, pero en este caso analizando texto. lo cual podría llegar a funcionar para el analisis de comentarios o reseñas que podría legar a tener
un servicio o producto.

Estrategia
------------
Utilizando los servicios que brinda Azure Cognitive Services, primero se analiza la cantidad de datos de antrada, para que de esta manera poder evaluar si se
requiere analizar estos archivos de forma concurente o de forma secuencial, en caso de ser necesario se dividira entre hilos, en caso contrario se utilizara de forma secuencial, para evitar el 
consumo de recursos que requiere la creación de hilos.

Tutorial
-------------
1: Clonar este repositorio de forma local.  
Vía http
``` 
https://github.com/AnthonyGriffith/Azure-Cognitive-Services-Analizer.git
```
Vía SSH
```
git@github.com:AnthonyGriffith/Azure-Cognitive-Services-Analizer.git
```
2: Con los siguientes comandos, se instalarían las herramientas necesarías para poder utilizar los servicios de azure.  
```python
pip install --upgrade azure-cognitiveservices-vision-face
``` 
```python
pip install azure-ai-textanalyticspip install azure-ai-textanalytics
``` 
```python
pip install Pillow
``` 
3: Ingresar los archcivos multimedia dentro de la carpeta media, según corresponda.  
4: Para poder usar las herramientas de FaceApi, es necesario poder las credenciales de Azure, y ponerlo en el archivo faceEmotions.py.
```
key = "<ENTER KEY>"
endpoint = "<ENTER ENDPONIT>"
```
5: Para poder usar las herramientas de TextAnalytics, es necesario poder las credenciales de Azure, y ponerlo en el archivo tetxSentiment.py.
```
credential = AzureKeyCredential("<ENTER KEY>")
endpoint = "<ENTER ENDPONIT>"
```
3: Para poder ejecutar el poryecto, solo es necesario darle  click derecho en cada archivo, y dar en click en Run.  
