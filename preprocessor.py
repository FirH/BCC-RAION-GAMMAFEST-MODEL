import pandas as pd

def input_preprocessor(DC235, DC024, DC025, DC205, DC270a, DC237, DC214, DC142a, DC226) :
    print(DC235)
    df = pd.DataFrame()
    df['DC235'] = [DC235]
    df['DC024'] = [DC024]
    df['DC025'] = [DC025]
    df['DC205'] = [DC205]
    df['DC270a'] = [DC270a]
    df['DC237'] = [DC237]
    df['DC214'] = [DC214]
    df['DC142a'] = [DC142a]
    df['DC226'] = [DC226]

    df['DC235'] = df['DC235'].map({
        'Di Hunian Pribadi' : 1,
        'Di Lahan/Taman Pribadi' : 2,
        'Lainnya' : 3
    })

    df['DC024'] = df['DC024'].map({
        'Aceh' : 11,'Sumatera Utara' : 12,'Sumatera Barat' : 13,'Riau' : 14,'Jambi' : 15,'Sumatera Selatan' : 16,'Bengkulu' : 17,'Lampung' : 18,'Banga Belitung' : 19,'Kepulauan Riau' : 21,'Jakarta' : 31,'Jawa Barat' : 32,'Jawa Tengah' : 33,'Jawa Timur' : 35,'Yogyakarta' : 34,'Banten' : 36,'Bali' : 51,'Nusa Tenggara Barat' : 52,'Nusa Tenggara Timur' : 53,'Kalimantan Barat' : 61,'Kalimatan Tengah' : 62,'Kalimantan Selatan' : 63,'Kalimantan Timur' : 64,'Kalimantan Utara' : 65,'Sulawesi Utara' : 71,'Sulawesi Tengah' : 72,'Sulawesi Selatan' : 73,'Sulawesi Tenggara' : 74,'Gorontalo' : 75,'Sulawesi Barat' : 76,'Gorontalo' : 75,'Maluku' : 81,'Maluku Utara' : 82,'Papua' : 91,'Papua Barat' : 94
    })

    df['DC025'] = df['DC025'].map({
        'Perkotaan' : 1,
        'Pedesaan' : 2
    })

    df['DC205'] = df['DC205'].map({
        'Siram' : 10,'Siram Menuju Pipa Saluran Pembuangan' : 11,'Siram Menuju Septic Tank' : 12,'Siram Menuju Lubang Jamban' : 13,'Siram Menuju Tempat Lain' : 14,'Siram (Tempat Dituju Tidak Diketahui)' : 15,'Siram Tanpa Septic Tank' : 16,'Siram (Publik / Bersama)' : 17,'Lubang (Latrine)' : 20,'Lubang Terventilasi (Improved Latrine)' : 21,'Lubang Dengan Lempeng' : 22,'Lubang Tanpa Lempeng' : 23,'Tanpa Fasilitas' : 30,'Semak semak / Sungai / Lapangan / Pantai / Kolam' : 31,'Toilet Kompos' : 41,'Toilet Ember' : 42,'Toilet Gantung' : 43,'Lainnya' : 96
    })

    df['DC237'] = df['DC237'].map({
        'Ada' : 1,
        'Tidak' : 0
    })

    df['DC214'] = df['DC214'].map({
        'Alami' : 10,'Bambu / Palem / Batang Kayu' : 12,'Tanah' : 13,'Parsial' : 20,'Bambu Dengan Lumpur' : 21,'Batu Dengan Lumpur' : 22,'Tanah Liat Terbuka' : 23,'Plywood' : 24,'Kardus' : 25,'Kayu Yang Digunakan Kembali' : 26,'Dinding Utuh' : 30,'Anyaman Bambu' : 31,'Batu Dengan Semen' : 32,'Blok Semen' : 34,'Tanah Liat Tertutup' : 35,'Papan Kayu' : 36,'Kawat Plester' : 37,'Semen Bertulang Serat Kaca / Gipsum / Asbes' : 38,'Lainnya' : 96
    })
    df['DC226'] = df['DC226'].map({
        'Listrik' : 1,'LPG' : 2,'Gas Alami' : 3,'Biogas' : 4,'Kerosene' : 5,'Batu Bara, Gambut' : 6,'Arang' : 7,'Kayu' : 8,'Jerami / Semak / Rumput' : 9,'Tanaman Pertanian' : 10,'Kotoran Hewan' : 11,'Tidak Ada Kegiatan Memasak Di Rumah' : 95,'Lainnya' : 96
    })

    return df
