#!/bin/bash

#Encontrar desde la raiz de la carpeta las carpetas que se llamen adjuntos
dirs=$(find ../ -type d -name "adjuntos")

while read -r dir; do
	echo "Doing directory $dir"
	list_files=$(find $dir -type f -name "*.png" )
	while read -r file; do
		base_file=$(basename "$file")
		echo "$base_file"
		if [[ "$base_file" == Pasted* ]]; then
			if [[ "$base_file" == *" "* ]]; then
				new_name_file=$(echo "$file" | sed 's/ /_/g')
				echo "ENCONTRAD --> old file: $file ---- new file: $new_name_file"
				mv "$file" "$new_name_file"
			fi
		fi
		
	done <<< $list_files
done <<< $dirs

#Debug
#echo $dirs
echo "Process suscessfull"



