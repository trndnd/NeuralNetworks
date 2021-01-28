
class Decision():
    def LorryOrCar(self,PredictionArray):
        Prediction = ""
        if PredictionArray == [1,0]:
            Prediction = "Lorry"
        else:
            Prediction = "Car"
        return Prediction
