from MultiClassClassification.LorryOrCar.SigmoidFunction import ActivationFunction
class HiddenLayer():
    def GivingBackMultiClassPrediction(self,SecondLayer):
        OutputLayerValues = []
        Prediction = []
        #This gets the value for teh lorry as both values have to be a 1 for it to be a lorry so thats why this performs a and function
        SecondLayerNode1 = -30
        for x in range(len(SecondLayer)):
            SecondLayerNode1 += (SecondLayer[x] * 20)
        SecondLayerNode2 = -10
        #this finds the valuefor the car so it performs a or function as only the bottom one needs to be a one for it to be a car
        SecondLayerNode2 += (-20 * SecondLayer[0]) + (SecondLayer[1] * 20)
        Prediction.append(ActivationFunction.SigmoidFunctionOnlyNeedingOneValue("",SecondLayerNode1))
        Prediction.append(ActivationFunction.SigmoidFunctionOnlyNeedingOneValue("",SecondLayerNode2))
        return Prediction

