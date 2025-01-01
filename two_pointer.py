# Two Pointer
# Problem: Cek apakah array memiliki dua elemen yang jumlahnya sama dengan target

def two_sum(nums, target):
    # Sort array jika belum terurut
    nums.sort()

    # Inisialisasi dua pointer
    left, right = 0, len(nums) - 1

    # Loop selama kedua pointer belum bertemu
    while left < right:

        # Hitung jumlah dari dua angka di posisi pointer
        current_sum = nums[left] + nums[right]
        
        # Jika jumlah sama dengan target, print hasil
        if current_sum == target:
            print(f"Pair found: {nums[left]}, {nums[right]}")
            return [nums[left], nums[right]]
        # jika jumlah terlalu kecil, geser pointer kiri ke kanan
        elif current_sum < target:
            left += 1
        # Jika jumlah terlalu besar, geser pointer kanan ke kiri
        else:
            right -= 1
    else:
        print('No Pair Found!')
    return None

# Call function
two_sum([2, 7, 11, 15], 18) # 7, 11

'''
Explaination
--------------
Kenapa hasil nya 7, 11 ?
dikarenakan pointer mencari nilai target katakanlah target 18
maka kedua pointer akan menghitung bagaiamana dari num itu menghasilkan nilai target
sehingga dalam process nya terdapat loop while jika pointer left kurang dari right maka:
- variable current_sum assing operator left + right
- jika terdapat suatu kondisi current_sum sama dengan nilai target maka akan di print
- jika current_sum kurang dari target maka menambahkan 1 nilai
- jika current_sum lebih besar dari target maka kurang 1 nilai
- dan jika tidak ada sama sekali nilai dalam nums yang match maka print No Pair found!
maka while atau looping tersebut selesai jika semua kondisi terpenuhi
'''