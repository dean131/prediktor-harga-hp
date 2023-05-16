from django.shortcuts import render

import joblib

def index(request):
    return render(request, 'index.html')

def classify(request):
    model = joblib.load('static\model_ml\model_knn_prediksi_harga_hp.pkl')

    data_test = request.POST.get('data_test')
    data_test = data_test.split()
    array_baru = []
    for angka in data_test:
        array_baru.append(float(angka))
    predict = model.predict([array_baru])

    match predict[0]:
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

    context = {
        'predict': predict,
        }
    return render(request, 'output.html', context)