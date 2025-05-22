#Versión inicial del módulo de análisis JPEG forense

#Descargar e instalar exiftool en tu ordenador
#https://exiftool.org/

#Descarga metadatos de una imagen jpg
exiftool imagen.jpeg

#Descarga tablas de cuantificación en valores hexadecimales
exiftool -v3 imagen.jpg


#Descarga metadatos de imagen jpg ordenados por categorias
exiftool -a -u -g1 + imagen.jpg 

#Descarga metadatos de imagen jpg ordenados por categorias y exporta archivo txt con información
exiftool -a -u -g1 + imagen.jpg > metadatos.txt




