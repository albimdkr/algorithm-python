# Sliding Show
# Temukan sub array dengan jumlah maksimum dari panjang tertentu

def sliding_show(nums, k):
    # Init varianle untuk penyimpan jumlah maksimum
    max_sum = 0
    current_sum = 0
    
    # Hitung jumlah awal untuk jendela pertama
    print(f"range K: {k}")
    for i in range(k):
        current_sum += nums[i] 
        print(f"processing first count: {current_sum}")
    
    # simpan current_sum sebagai max_sum
    max_sum = current_sum
    print(f"Save current_sum to max_sum: {max_sum}")
    
    # Geser jendela sepanjang array
    for i in range(k, len(nums)):
        # Tambahkan elemen baru dan kurang elemen lama
        current_sum += nums[i] - nums[i - k]
        print(f"processing move: {current_sum}")
        
        # Perbarui jumlah maksimum jika perlu
        max_sum = max(max_sum, current_sum)
    
    print(f"Maximum sum of subarray of length {k} is {max_sum}")
    return None

sliding_show([1,3,2,5,1,1,7], 4) # 4 is 14

'''
Explaination
--------------
Kenapa nilai k=4 panjangan subrarray nya = 14 ?
Init max_sum dan current_sum = 0
Kemudian setelah di ini, hitung nilai pertama dengan loop
rentang dalam variable nilai k=4 berarti kondisi memenuhi nya itersi nya sampai 4 kali
- Iterasi 1: cari indeks array $nums pertama[0] maka = 1 kemudian hitung $current_sum = 1
- Iterasi 2: cari indeks array $nums kedua[1] maka = 3 kemudian hittung $current_sum + 3 = 4
- Iterasi 3: cari indeks array $nums ketiga[2] maka = 2 kemudian hitung $current_sum + 2 = 6
- Iterasi 4: cari indeks array $nums keempat[3] maka = 5 berarti hitung $current_sum + 5 = 11
Kemudian assign si current_sum nya menjadi max_sum = 11, kenapa 11? karena dari jumlah iterasi maks 4 kali dan hasil akhir nya 11
'''