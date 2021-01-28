import numpy as np
from MultiClassClassification.LorryOrCar.SigmoidFunction import ActivationFunction
from MultiClassClassification.LorryOrCar.HiddenLayer import HiddenLayer
from MultiClassClassification.LorryOrCar.Decision import Decision
WeightMatrix = [[-30000,5.5],[-3500,4]]
Inputs = [1032,982,6800,5900]
def MakingPredictions(Input,WeightArray):
    SecondLayerValue = []
    SecondLayerValue.append(ActivationFunction.SigmoidFunction("",WeightArray,Input))
    return SecondLayerValue

def GettingAllSecondLayerValues():
    SecondLayerValues = []
    for ArrayPos in range(len(WeightMatrix)):
        WeightArray = WeightMatrix[ArrayPos]
        for x in range(len(Inputs)):
            try:
                SecondLayerValues[x] += MakingPredictions(Inputs[x], WeightArray)
            except IndexError:
                SecondLayerValues.append(MakingPredictions(Inputs[x], WeightArray))
    return SecondLayerValues

SecondLayerValuesMatrix = GettingAllSecondLayerValues()

def gettingTheOutputNumbers():
    PredictionsArray = []
    for SecondLayerArray in SecondLayerValuesMatrix:
        PredictionsArray.append(HiddenLayer.GivingBackMultiClassPrediction("",SecondLayerArray))
    return PredictionsArray

PredictionsMatrix = gettingTheOutputNumbers()

for Prediction in PredictionsMatrix:
    print(Decision.LorryOrCar("",Prediction))








    



                
            
                

