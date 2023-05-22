def predict_func(pred):
    match pred:
        case 0:
            pred = 'Low Cost'
        case 1:
            pred = 'Medium Cost'
        case 2:
            pred = 'High Cost'
        case 3:
            pred = 'Very High Cost'
        case _:
            pred = 'Unknown'
    return pred