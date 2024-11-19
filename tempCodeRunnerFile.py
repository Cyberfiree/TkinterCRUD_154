def submit():
    
    try:
        nama_siswa = nama_var.get()
        biologi = int(biologi_var.get())
        fisika = int(fisika_var.get())
        inggris = int(inggris_var.get())
        
        if not nama_siswa:
            raise Exception("Nama siswa harus diisi")
        
        prediksi = calc_prediction(biologi, fisika, inggris)
        
        save_to_database(nama_siswa, biologi, fisika, inggris, prediksi)
        
        messagebox.showinfo("Sukses", "Data berhasil disimpan! \nPrediksi Fakultas: " + prediksi)
        clear_inputs()
        populate_table()
    except ValueError as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")
        
# Fungsi menangani tombol update
def update():
    try:
        if not selected_id.get():
            raise Exception("Pilih data yang akan diupdate",)
        
        id = int(selected_id.get())
        nama_siswa = nama_var.get()
        biologi = int(biologi_var.get())
        fisika = int(fisika_var.get())
        inggris = int(inggris_var.get())
        
        if not nama_siswa:
            raise ValueError("Nama siswa harus diisi")
        
        prediksi = calc_prediction(biologi, fisika, inggris)
        
        update_database(selected_id.get(), nama_siswa, biologi, fisika, inggris, prediksi)
        
        messagebox.showinfo("Sukses", "Data berhasil diperbarui!\nPrediksi Fakultas: " + prediksi)
        clear_inputs()
        populate_table()
    except Exception as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")