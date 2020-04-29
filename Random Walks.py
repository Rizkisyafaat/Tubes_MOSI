import random

#inisialisasi variabel scalar
jumlah_individu = 200
terinfeksi = jumlah_individu * 0.05
probabilitas_bergerak = 0.8
waktu_pemulihan = 10


#ukuran ruang simulasi
x_min = 0
y_min = 0
x_max = 20
y_max = 20

x_range = x_max-x_min
y_range = y_max-y_min
x_position = []
y_position = []

status_terinfeksi=[]
status_imunitas=[]
waktu_infeksi=[]

def updatePosition(x,y):
    arah = random.random()
    if arah <= 0.2:
        x = x + 1
    elif arah <= 0.4:
        y = y - 1
    elif arah <= 0.6:
        x = x - 1
    elif arah <= 0.8:
        y = y + 1
    return [x,y]

for individu in range(jumlah_individu):
    x_position.append(random.randint(x_min,x_max))
    y_position.append(random.randint(y_min,x_max))

    #status terinfeksi
    if (individu < terinfeksi):
        status_terinfeksi.append(True)
    else:
        status_terinfeksi.append(False)

    # initial status imune
    status_imunitas.append(False)

    # initial waktu_infeksi
    waktu_infeksi.append(0)

while (terinfeksi > 0):
    for i in range(jumlah_individu):
        updatePosition(x_position[i],y_position[i])
