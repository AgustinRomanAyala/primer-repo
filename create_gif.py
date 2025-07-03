import imageio.v3 as iio

#En nuestro programa de Python, crearemos una lista que contenga las ubicaciones de los archivos de imagen. 
filenames = ['team-pic1.png', 'team-pic2.png']

#También necesitamos crear una lista vacía que se usará para almacenar los datos de imagen de estos archivos.
images = []
#A continuación, usemos un forbucle para recorrer las rutas de los archivos y 
#leer las imágenes usando el método imageiode la biblioteca .imread()
for filename in filenames:
    images.append(iio.imread(filename))
#Por último, usemos el .imwrite()método para convertir las imágenes en un GIF:
#'team.gif': Este es el nombre que desea darle a su nuevo archivo GIF.
#images: La lista que contiene los datos de la imagen.
#duration = 500: Cuánto tiempo debe mostrarse cada imagen en el GIF, en milisegundos.
#loop = 0: ¿Cuántas veces debe repetirse el GIF (0 significa que se repite indefinidamente)?
iio.imwrite('team.gif', images, duration = 500, loop = 0)

