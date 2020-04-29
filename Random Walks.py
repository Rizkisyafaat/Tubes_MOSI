import random
import matplotlib.pyplot as plt
from celluloid import Camera as Camera
import numpy as np

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

status_terinfeksi = []
status_imunitas = []
waktu_infeksi = []
total_infeksi = []

animasi = []

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

# Boundary
def boundary(x,y):
    if (x > x_max):
        x = x - x_range
    elif (x < x_min):
        x = x + x_range
    elif (y > y_max):
        y = y - y_range
    elif (y < y_min):
        y = y + y_range
    return[x,y]

# jarak orang sehat dan orang sakit = dekat (ketularan)
def cek_posisi(x,y,x_position,y_position):
    status = False
    i = 0
    while ((status == False) & (i < jumlah_individu)):
        if ((status_terinfeksi[i]) & (x_position[i] == x) & (y_position[i] == y)):
            status = True
        i = i + 1
    return status



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

Camera = Camera(plt.figure())

while (terinfeksi > 0):
    for i in range(jumlah_individu):
        posisi_skrg = updatePosition(x_position[i],y_position[i])

        x = boundary(posisi_skrg[0], posisi_skrg[1])[0]
        y = boundary(posisi_skrg[0], posisi_skrg[1])[1]

        if (status_terinfeksi[i]):
            waktu_infeksi[i] = waktu_infeksi[i] + 1

        if (waktu_infeksi[i] > waktu_pemulihan):
             status_imunitas[i] = True
             waktu_infeksi[i] = 0
             terinfeksi = terinfeksi - 1

        if status_imunitas[i] == True:
            a = False
        else:
            a = True
        if status_terinfeksi[i] == True:
            b = False
        else:
            b = True

        if (a & b & cek_posisi(x, y, x_position, y_position)):
            # plt.subplot(1, 2, 1)
            # plt.scatter(*animasi, c="red", s=50)
            status_terinfeksi[i] = True
            terinfeksi = terinfeksi + 1

        x_position[i] = x
        y_position[i] = y

        koordinat = [x_position,y_position]
        animasi = np.c_[koordinat]

    total_infeksi.append(terinfeksi)

    plt.figure(1)
    plt.subplot(1, 2, 1)
    plt.scatter(*animasi, c="green", s=50)
    plt.title("Simulasi Random Walk Penyebaran Virus")
    plt.subplot(1, 2, 2)
    plt.plot(total_infeksi, c="blue")
    Camera.snap()


anim = Camera.animate(interval=1000)
plt.grid(True,which="both")
plt.legend()
plt.title("Grafik Penyebaran Virus")

plt.show()