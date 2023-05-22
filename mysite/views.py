from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'index.html')

def classify(request):
    algorithm = request.POST.get('algorithm')  # Mendapatkan pilihan algoritma dari permintaan POST

    data_test = request.POST.get('data_test')
    data_test = data_test.split()
    array_test = []
    for angka in data_test:
        array_test.append(float(angka))

    match algorithm:
        case 'kmeans':
            model = joblib.load('static\model_ml\kmeans_model.pkl')
            cluster = model.predict([array_test])
            match cluster:
                case 0:
                    predict = 'Low Cost'
                case 1:
                    predict = 'Medium Cost'
                case 2:
                    predict = 'High Cost'
                case 3:
                    predict = 'Very High Cost'
                case _:
                    predict = 'Unknown'
        case 'knn':
            model = joblib.load('static\model_ml\model_knn_prediksi_harga_hp.pkl')
            predict = model.predict([array_test])
            match predict:
                case 0:
                    predict = 'Low Cost'
                case 1:
                    predict = 'Medium Cost'
                case 2:
                    predict = 'High Cost'
                case 3:
                    predict = 'Very High Cost'
                case _:
                    predict = 'Unknown'
        case _:
            return render(request, 'error.html', {'message': 'Invalid algorithm selection'})  # Menampilkan halaman error jika algoritma tidak valid
        
    context = {
        'predict': predict,
    }
    return render(request, 'output.html', context)
