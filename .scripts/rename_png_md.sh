#!/bin/bash

#Recorremos todos los fichero .md"
find ../ -type f -name "*.md" | while read -r mdfile; do
#Recorremos las imágenes que contiene el .md
	grep -oP '!\[.*?\]\(\K.*?(?=\))' "$mdfile" | grep "%20" | while read -r imagen; do
		echo "fichero: $mdfile --- imagen: $imagen"
		ruta_nueva=$(echo "$imagen" | sed 's/%20/_/g')
		echo "ENCONTRADO old_imagen: $imagen --- new_imagen: $ruta_nueva"
		sed -i "s|$imagen|$ruta_nueva|g" "$mdfile"
	done
done
