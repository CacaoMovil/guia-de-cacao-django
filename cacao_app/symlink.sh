#!/bin/bash
# Usage: Creates a Symbolics links

cd ../_output
#if [ cd ../_output ]; then
#	echo "Ready"
#else
#	exit
#fi

# Define  function here

#Guia function
Guia () {
   	if [ -d "static/" ]
   		then
			echo "Already exist."
	else
   		ln -s ../static .
		echo "Created."
	fi
   	echo "==== Done Guia ==="
}

#Contenido function
Contenido () {
   	cd guia/
	DIRS="ls -d */"
	for DIR in $DIRS
		do
			if [ -d ${DIR} ]; then
				cd ${DIR} 
				cd contenido/
				if [ -d "static/" ]
   					then
						echo "Already exist."
				else
   					ln -s ../../../static .
					echo "Created."
					cd .. && cd ..
				fi
			else
				echo "Error"
			fi
			
	done
	echo "==== Done Contenido ==="
}

#Invoke Functions
Contenido
Guia 
