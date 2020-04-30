import random
import matplotlib.pyplot as plt
from celluloid import Camera as Camera
import numpy as np

# inisialisasi variabel scalar
jumlah_individu = 200
terinfeksi = jumlah_individu * 0.05
probabilitas_bergerak = 0.8
waktu_pemulihan = 10

# ukuran ruang simulasi
x_min = 0
y_min = 0
x_max = 20
y_max = 20

x_range = x_max - x_min
y_range = y_max - y_min

x_position = []
y_position = []

status_terinfeksi = []
status_imunitas = []
waktu_infeksi = []
total_infeksi = []

# menentukan arah bergerak dengan probabilitas bergerak 80%
def updatePosition(x, y):
    arah = random.random()
    if arah <= 0.2:
        x = x + 1
    elif arah <= 0.4:
        y = y - 1
    elif arah <= 0.6:
        x = x - 1
    elif arah <= 0.8:
        y = y + 1
    return [x, y]

# Boundary
def boundary(x, y):
    if (x > x_max):
        x = x - x_range
    elif (x < x_min):
        x = x + x_range
    elif (y > y_max):
        y = y - y_range
    elif (y < y_min):
        y = y + y_range
    return [x, y]

# ordinat orang sehat = orang sakit, maka terinfeksi
def cek_posisi(x, y, x_position, y_position):
    status = False
    i = 0
    while ((status == False) & (i < jumlah_individu)):
        if ((status_terinfeksi[i]) & (x_position[i] == x) & (y_position[i] == y)):
            status = True
        i = i + 1
    return status

# menentukan posisi awal dan status terinfeksi
for individu in range(jumlah_individu):
    x_position.append(random.randint(x_min, x_max))
    y_position.append(random.randint(y_min, x_max))

    if (individu < terinfeksi):
        status_terinfeksi.append(True)
    else:
        status_terinfeksi.append(False)

    status_imunitas.append(False)

    # inisialisasi waktu_infeksi
    waktu_infeksi.append(0)

Camera = Camera(plt.figure())
waktu = 0

while (terinfeksi > 0):
    waktu = waktu + 1
    x_health = []
    y_health = []
    x_infect = []
    y_infect = []

    for i in range(jumlah_individu):
        posisi_skrg = updatePosition(x_position[i], y_position[i])

        x = boundary(posisi_skrg[0], posisi_skrg[1])[0]
        y = boundary(posisi_skrg[0], posisi_skrg[1])[1]

        if (status_terinfeksi[i]):
            waktu_infeksi[i] = waktu_infeksi[i] + 1

        if (waktu_infeksi[i] == waktu_pemulihan):
            status_imunitas[i] = True
            terinfeksi = terinfeksi - 1

        if status_imunitas[i] == True:
            a = False
        else:
            a = True
        if status_terinfeksi[i] == True:
            b = False
        else:
            b = True

        # jika tidak memiliki imunitas dan belum terinfeksi dan berdekatan
        if (a & b & cek_posisi(x, y, x_position, y_position)):
            status_terinfeksi[i] = True
            terinfeksi = terinfeksi + 1

        x_position[i] = x
        y_position[i] = y

    total_infeksi.append(terinfeksi)

    # memisahkan ordinat individu terinfeksi dan tidak
    for j in range(jumlah_individu):
        if status_imunitas[j] or status_terinfeksi[j] == False:
            x_health.append(x_position[j])
            y_health.append(y_position[j])
        elif status_imunitas[j] == False and status_terinfeksi[j]:
            x_infect.append(x_position[j])
            y_infect.append(y_position[j])

    sehat = [x_health, y_health]
    animasi_sehat = np.c_[sehat]
    sakit = [x_infect, y_infect]
    animasi_sakit = np.c_[sakit]

    plt.subplot(1, 2, 1)
    plt.title("Penyebaran Virus")
    plt.scatter(*animasi_sehat, c="green", s=30, label="sehat")
    plt.scatter(*animasi_sakit, c="red", s=30, label="terinfeksi")


    plt.subplot(1, 2, 2)
    plt.title("Grafik Terinfeksi")
    plt.plot(total_infeksi, c="red")
    Camera.snap()

anim = Camera.animate(interval=1000)
plt.grid(True, which="both")
plt.xlabel("Hari")
plt.ylabel("Terinfeksi")
print('___________________Data___________________')
print("jumlah individu         :", jumlah_individu)
print("puncak total terinfeksi :", int(max(total_infeksi)))
print("total waktu pemulihan   :", waktu)

plt.show()