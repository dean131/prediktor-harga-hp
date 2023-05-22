from django.shortcuts import render
from .predict import predict_func
import joblib

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def classify(request):
    algorithm = request.POST.get('algorithm')

    data_test = request.POST.get('data_test')
    data_test = data_test.split()
    array_test = []
    for angka in data_test:
        array_test.append(float(angka))

    match algorithm:
        case 'kmeans':
            model = joblib.load('static\model_ml\kmeans_model.pkl')
            predict = model.predict([array_test])
            predict = predict_func(predict)
        case 'knn':
            model = joblib.load('static\model_ml\model_knn_prediksi_harga_hp.pkl')
            predict = model.predict([array_test])
            predict = predict_func(predict)
        case 'dt':
            model = joblib.load('static\model_ml\model_dt_prediksi_harga_hp.pkl')
            predict = model.predict([array_test])
            predict = predict_func(predict)
        case 'nb':
            model = joblib.load('static\model_ml\model_nb_prediksi_harga_hp.pkl')
            predict = model.predict([array_test])
            predict = predict_func(predict)
        case 'rf':
            model = joblib.load('static\model_ml\model_rf_prediksi_harga_hp.pkl')
            predict = model.predict([array_test])
            predict = predict_func(predict)
        case _:
            return render(request, 'error.html', {'message': 'Invalid algorithm selection'})
        
    context = {
        'predict': predict,
    }
    return render(request, 'output.html', context)
