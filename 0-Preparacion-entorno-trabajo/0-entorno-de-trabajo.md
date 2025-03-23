
# Entorno

En esta ocasión vamos a trabajar con un IDE como visual code y una distribución como Anaconda


## Versión de python 

Para conocer que versión de python usar podemos tener esta página de referencia https://docs.python.org/3/ donde podemos encontrar las distintas versiones.

*  Importante conocer la versión que queremos usar

![Pasted image 20250321234915.png](Pasted%20image%2020250321234915.png)


## Instalación de Anaconda

Utilizaremos Anaconda que es una distribución gratuita y de código abierto ( un conjunto de software preempaquetado, muchas librerías o paquetes adicionales ) que proporciona un entorno para trabajar con Python y R de manera más eficiente en áreas de análisis de datos, ciencias de datos y machine learning.



Para instalar Anaconda [Enlace](https://www.anaconda.com/download/success) y [Documentacion](https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation:how-do-i-verify-my-installers-integrity)


Si no queremos el entorno base podemos desactivarlo:

* conda config --set auto_activate_base false


### Comandos en Anacanda

* https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf


![conda-cheatsheet.pdf](conda-cheatsheet.pdf)



**ENTORNO GRÁFICO**

* Lanzar entorno gráfico
	* anaconda-navigator -> ./anaconda-navigator

**CREAR ENTORNO VIRTUALES**

* Creando entorno virtuales
	* conda create --name [nombre_del_entorno] python=[3.8]
* Listar entorno virtual
	* conda env list
* Activar entorno virtual 
	* conda activate [nombre_del_entorno]
* Desactivar entorno virtual
	* conda deactivate


**CONSULTAR ENTORNO VIRTUALES**

* Lista paquetes de un entorno virtual
	* conda list -n [nombre_entorno]
* Exportar los paquetes del entorno a un archivo
	* conda env export -n [nombre_entorno] > entorno.yml
* Restaurar
	* conda env create -f entorno.yml

**PAQUETES PYTHON**

* instalar paquetes **dentro del entorno virtual**
	* conda install numpy pandas matplotlib
	* pip install tensorflow
* Listar los paquetes de python
	* conda list

**ACTUALIZACIONES**

* Actualizaciónes de conda
	* conda update conda
	* conda update --all

