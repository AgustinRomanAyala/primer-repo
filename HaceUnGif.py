import imageio.v3 as ima3

filenames = ['dari1.jpg', 'dari2.jpg', 'dari3.jpg', 'dari4.jpg', 'dari5.jpg', 'dari6.jpg', 'dari7.jpg']

images = []

for filename in filenames:
    images.append(ima3.imread(filename))

ima3.imwrite('Dari1.gif', images, duration = 500, loop = 0)