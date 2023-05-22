from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'index.html')

def classify(request):
    algorithm = request.POST.get('algorithm')  # Mendapatkan pilihan algoritma dari permintaan POST

    if algorithm == 'kmeans':
        model = joblib.load('static\model_ml\kmeans_model.pkl')
    elif algorithm == 'knn':
        model = joblib.load('static/model_ml/model_knn_prediksi_harga_hp.pkl')
    else:
        return render(request, 'error.html', {'message': 'Invalid algorithm selection'})  # Menampilkan halaman error jika algoritma tidak valid

    data_test = request.POST.get('data_test')
    data_test = data_test.split()
    array_baru = []
    for angka in data_test:
        array_baru.append(float(angka))

    if algorithm == 'kmeans':
        cluster = model.predict([array_baru])

        if cluster == 0:
            predict = 'Low Cost'
        elif cluster == 1:
            predict = 'Medium Cost'
        elif cluster == 2:
            predict = 'High Cost'
        elif cluster == 3:
            predict = 'Very High Cost'
        else:
            predict = 'Unknown'

    elif algorithm == 'knn':
        predict = model.predict([array_baru])
        if predict == 0:
            predict = 'Low Cost'
        elif predict == 1:
            predict = 'Medium Cost'
        elif predict == 2:
            predict = 'High Cost'
        elif predict == 3:
            predict = 'Very High Cost'
        else:
            predict = 'Unknown'

    else:
        return render(request, 'error.html', {'message': 'Invalid algorithm selection'})  # Menampilkan halaman error jika algoritma tidak valid

    context = {
        'predict': predict,
    }
    return render(request, 'output.html', context)
