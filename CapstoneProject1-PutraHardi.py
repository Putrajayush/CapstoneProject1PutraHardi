data_siswa = {
    '13516001': {'Nama': 'Putra Hardi Ramadhan', 'Gender': 'Laki-laki', 'Kota': 'Jakarta', 'Program Studi': 'Teknik Informatika', 'Tahun Ajaran': 2016},
    '13516002': {'Nama': 'Rizky Andyno', 'Gender': 'Laki-laki', 'Kota': 'Bandung', 'Program Studi': 'Teknik Informatika', 'Tahun Ajaran': 2016},
    '13616001': {'Nama': 'Muhammad Falih', 'Gender': 'Laki-laki', 'Kota': 'Jakarta', 'Program Studi': 'Teknik Elektro', 'Tahun Ajaran': 2016},
    '13616002': {'Nama': 'Sarah Azzahra', 'Gender': 'Perempuan', 'Kota': 'Bandung', 'Program Studi': 'Teknik Elektro', 'Tahun Ajaran': 2016},
    '17016001': {'Nama': 'Tata Hetiandanti', 'Gender': 'Perempuan', 'Kota': 'Depok', 'Program Studi': 'Seni Rupa', 'Tahun Ajaran': 2016},
    '17017001': {'Nama': 'Yasmine Febrina', 'Gender': 'Perempuan', 'Kota': 'Yogyakarta', 'Program Studi': 'Seni Rupa', 'Tahun Ajaran': 2017},
    '17117001': {'Nama': 'Marcel Richir', 'Gender': 'Laki-laki', 'Kota': 'Depok', 'Program Studi': 'Teknik Mesin', 'Tahun Ajaran': 2017},
}


program_studi_dict = {
    '135': 'Teknik Informatika',
    '136': 'Teknik Elektro',
    '170': 'Seni Rupa',
    '171': 'Teknik Mesin',
    '172': 'Matematika'
}

def read_data():
    while True:
        print("\n[1] Memperlihatkan Semua Data Siswa\n[2] Cari Data Berdasarkan NIM\n[3] Tampilkan Data Berdasarkan Program Studi\n[4] Tampilkan Data Berdasarkan Tahun Ajaran\n[5] Kembali ke Menu Utama")
        choice = input("Pilih opsi: ")
        
        if choice == '1':  # Memperlihatkan Semua Data Siswa, mengiterasi semua dictionary
            for nim, details in data_siswa.items():
                print(f"NIM: {nim}, Nama: {details['Nama']}, Gender: {details['Gender']}, Kota: {details['Kota']}, Program Studi: {details['Program Studi']}, Tahun Ajaran: {details['Tahun Ajaran']}")
        
        elif choice == '2':  # Memperlihatkan Data berdasarkan NIM, melakukan search pada NIM yang dimasukkan
            nim = input("Masukkan NIM: ")
            if nim in data_siswa:
                details = data_siswa[nim]
                print(f"NIM: {nim}, Nama: {details['Nama']}, Gender: {details['Gender']}, Kota: {details['Kota']}, Program Studi: {details['Program Studi']}, Tahun Ajaran: {details['Tahun Ajaran']}")
            else:
                print("Data tidak ditemukan. Silakan coba lagi.")
        
        elif choice == '3':  # Memperlihatkan Data Berdasarkan Kode Program Studi
            print("Pilih Program Studi:")
            for code, name in program_studi_dict.items():
                print(f"{code}: {name}")
            program_studi_code = input("Masukkan kode Program Studi: ")
            
            #Melakukan search pada Kode Program Studi di Dictionary
            if program_studi_code in program_studi_dict:
                program_studi = program_studi_dict[program_studi_code]
                found = False
                #Menampilkan Seluruh Data pada Program Studi yang dimasukkan
                for nim, details in data_siswa.items():
                    if details['Program Studi'].lower() == program_studi.lower():
                        print(f"NIM: {nim}, Nama: {details['Nama']}, Gender: {details['Gender']}, Kota: {details['Kota']}, Program Studi: {details['Program Studi']}, Tahun Ajaran: {details['Tahun Ajaran']}")
                        found = True
                if not found:
                    print(f"Tidak ada data untuk Program Studi {program_studi}.")
            else:
                print("Kode Program Studi tidak valid.")
        
        elif choice == '4':  # Memperlihatkan Data Berdasarkan Tahun Ajaran
            #Melakukan pengecekan tahun ajaran, harus lebih dari 2000
            try:
                tahun_ajaran = int(input("Masukkan Tahun Ajaran (harus tahun 2000 atau lebih): "))
                if tahun_ajaran < 2000:
                    print("Tahun Ajaran tidak valid. Harus 2000 atau lebih.")
                else:
                    found = False
                    #Menampilkan Seluruh Data pada Tahun Ajaran yang dimasukkan
                    for nim, details in data_siswa.items():
                        if details['Tahun Ajaran'] == tahun_ajaran:
                            print(f"NIM: {nim}, Nama: {details['Nama']}, Gender: {details['Gender']}, Kota: {details['Kota']}, Program Studi: {details['Program Studi']}, Tahun Ajaran: {details['Tahun Ajaran']}")
                            found = True
                    if not found:
                        print(f"Tidak ada data untuk Tahun Ajaran {tahun_ajaran}.")
            except ValueError:
                print("Tahun Ajaran harus berupa angka.")
        
        elif choice == '5':  # Kembali ke menu utama
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")




def generate_nim(program_studi_code, tahun_ajaran):
    # Mengubah Tahun ajaran menjadi string dengan 2 digit dibelakang
    tahun_digits = str(tahun_ajaran)[-2:]

    # Menghitung banyak jumlah siswa yang ada pada Program Studi dan Tahun Ajaran yang sama
    existing_students = [
        nim for nim in data_siswa.keys()
        if nim.startswith(program_studi_code + tahun_digits)
    ]
    
    # Memberikan 3 digit terakhir pada NIM baru, +1 apabila sudah ada siswa, 001 apabila siswa pertama
    if existing_students:
        last_three_digits = int(existing_students[-1][-3:]) + 1
    else:
        last_three_digits = 1
    last_three_digits_str = f'{last_three_digits:03d}'

    # Menggabungkan semua digit, Program Studi, Tahun ajaran dan 3 digit terakhir
    new_nim = program_studi_code + tahun_digits + last_three_digits_str
    return new_nim


def create_data():
    while True:
        print("\n[1] Menambahkan Data Siswa\n[2] Kembali ke menu")
        choice = input("Pilih opsi: ")
        if choice == '2':
            break
        elif choice == '1':
            # Meminta masukkan kode Program Studi
            print("Pilih Program Studi:")
            for code, name in program_studi_dict.items():
                print(f"{code}: {name}")
            program_studi_code = input("Masukkan kode Program Studi: ")
            
            # Memvalidasi masukkan kode Program Studi
            if program_studi_code not in program_studi_dict:
                print("Program Studi tidak valid.")
                continue
            
            # Memvalidasi masukkan tahun ajaran, harus diatas 2000
            while True:
                tahun_ajaran = int(input("Masukkan Tahun Ajaran (harus setelah 2000): "))
                if tahun_ajaran >= 2000:
                    break
                else:
                    print("Tahun Ajaran tidak valid. Harus setelah tahun 2000.")
            
            # Generate NIM
            nim = generate_nim(program_studi_code, tahun_ajaran)
            print(f"NIM yang dihasilkan: {nim}")
            
            # Masukkan Nama
            nama = input("Masukkan Nama: ")

            # Masukkan Gender, dan validasi gender
            while True:
                gender = input("Masukkan Gender (Laki-laki/Perempuan): ").capitalize()
                if gender in ['Laki-laki', 'Perempuan']:
                    break
                else:
                    print("Input tidak valid. Masukkan 'Laki-laki' atau 'Perempuan'.")

            #Masukkan Kota
            kota = input("Masukkan Kota: ")
            program_studi = program_studi_dict[program_studi_code]
            
            # Menyimpan data kedalam Dictionary
            data_siswa[nim] = {
                'Nama': nama,
                'Gender': gender,
                'Kota': kota,
                'Program Studi': program_studi,
                'Tahun Ajaran': tahun_ajaran
            }
            print(f"Data berhasil ditambahkan dengan NIM: {nim}")

            print("\n[1] Menambahkan Data Siswa lagi\n[2] Kembali ke menu")
            choice = input("Pilih opsi: ")
            if choice == '2':
                break

def update_data():
    while True:
        print("\n[1] Mengubah Data Siswa\n[2] Kembali ke menu")
        choice = input("Pilih opsi: ")
        if choice == '2':
            break
        elif choice == '1':
            nim = input("Masukkan NIM yang ingin diubah: ")
            if nim in data_siswa:
                print(f"Data saat ini: {data_siswa[nim]}")

                # Meminta nama baru (Kosong jika ingin sama)
                nama = input(f"Masukkan Nama baru (biarkan kosong jika tetap {data_siswa[nim]['Nama']}): ") or data_siswa[nim]['Nama']

                # Meminta gender baru dan validasi gender (Kosong jika ingin sama)
                while True:
                    gender = input(f"Masukkan Gender baru (Laki-laki/Perempuan) (biarkan kosong jika tetap {data_siswa[nim]['Gender']}): ").capitalize() or data_siswa[nim]['Gender']
                    if gender in ['Laki-laki', 'Perempuan']:
                        break
                    else:
                        print("Input tidak valid. Masukkan 'Laki-laki' atau 'Perempuan'.")

                # Meminta kota baru (Kosong jika ingin sama)
                kota = input(f"Masukkan Kota baru (biarkan kosong jika tetap {data_siswa[nim]['Kota']}): ") or data_siswa[nim]['Kota']

                # Mengambil program studi dan tahun ajaran dari NIM, agar NIM bisa langsung diubah otomatis apabila program studi dan tahun ajaran diubah
                current_program_studi_code = nim[:3]
                current_tahun_ajaran = int('20' + nim[3:5])  # Extracting year

                # Meminta Program Studi Baru dan Tahun Ajaran Baru, serta validasi masukkan
                while True:
                    print("Pilih Program Studi baru (biarkan kosong jika tidak berubah):")
                    for code, name in program_studi_dict.items():
                        print(f"{code}: {name}")
                    new_program_studi_code = input("Masukkan kode Program Studi: ") or current_program_studi_code

                    if new_program_studi_code in program_studi_dict:
                        break
                    else:
                        print("Kode Program Studi tidak valid. Coba lagi.")

                # Validasi Tahun Ajaran yang baru
                while True:
                    try:
                        new_tahun_ajaran = input(f"Masukkan Tahun Ajaran baru (biarkan kosong jika tetap {current_tahun_ajaran}): ")
                        new_tahun_ajaran = int(new_tahun_ajaran) if new_tahun_ajaran else current_tahun_ajaran
                        if new_tahun_ajaran >= 2000:
                            break
                        else:
                            print("Tahun Ajaran tidak valid. Harus setelah tahun 2000.")
                    except ValueError:
                        print("Tahun Ajaran tidak valid, coba lagi.")

                # Generate NIM apabila Program Studi dan Atau Tahun Ajaran Berubah
                if new_program_studi_code != current_program_studi_code or new_tahun_ajaran != current_tahun_ajaran:
                    new_nim = generate_nim(new_program_studi_code, new_tahun_ajaran)
                    print(f"NIM telah berubah dari {nim} menjadi {new_nim}.")

                    # Update data siswa di Dictionary apabila NIM berubah
                    data_siswa[new_nim] = {
                        'Nama': nama,
                        'Gender': gender,
                        'Kota': kota,
                        'Program Studi': program_studi_dict[new_program_studi_code],
                        'Tahun Ajaran': new_tahun_ajaran
                    }

                    # Menghapus NIM yang sebelumnya
                    del data_siswa[nim]
                else:
                    # Menyimpan data siswa di Dictionary apabila NIM tidak berubah
                    data_siswa[nim] = {
                        'Nama': nama,
                        'Gender': gender,
                        'Kota': kota,
                        'Program Studi': program_studi_dict[new_program_studi_code],
                        'Tahun Ajaran': new_tahun_ajaran
                    }

                print("Data berhasil diperbarui.")
            else:
                print("Data tidak ditemukan.")

            print("\n[1] Mengubah Data Siswa lagi\n[2] Kembali ke menu")
            choice = input("Pilih opsi: ")
            if choice == '2':
                break



def delete_data():
    while True:
        print("\n[1] Menghapus Data Siswa\n[2] Kembali ke menu utama")
        choice = input("Pilih opsi: ")
        if choice == '2':
            break
        #Mencari NIM dari siswa yang ingin dihapus datanya, sekaligus menanyakan sekali lagi apalah ingin dihapus
        elif choice == '1':
            nim = input("Masukkan NIM yang ingin dihapus: ")
            if nim in data_siswa:
                confirm = input(f"Apakah Anda yakin ingin menghapus data dengan NIM {nim}? (y/n): ").lower()
                if confirm == 'y':
                    del data_siswa[nim]
                    print("Data berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Data tidak ditemukan.")

            print("\n[1] Menghapus Data Mahasiswa lagi\n[2] Kembali ke menu")
            choice = input("Pilih opsi: ")
            if choice == '2':
                break

def main_menu():
    while True:
        print("\nMenu Utama:")
        print("[1] Memperlihatkan Data Siswa\n[2] Menambahkan Data Siswa\n[3] Mengubah Data Siswa\n[4] Menghapus Data Siswa\n[5] Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            read_data()
        elif choice == '2':
            create_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main_menu()
