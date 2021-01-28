import numpy as np
print(np.__version__)
class ActivationFunction():
    def SigmoidFunction(self,weightArray,Input):
        for pos in range(1,len(weightArray)):
            Product = weightArray[0] + (weightArray[pos] * Input)
            SigmoidValue = 1/(1 + np.exp(-Product))
            if SigmoidValue > 0.5:
                SigmoidValue = 1
            else:
                SigmoidValue = 0
            SecondLayerValue = SigmoidValue
        return SecondLayerValue
    def SigmoidFunctionOnlyNeedingOneValue(self,Product):
        SigmoidValue = 1 / (1 + np.exp(-Product))
        if SigmoidValue > 0.5:
            SigmoidValue = 1
        else:
            SigmoidValue = 0
        return SigmoidValue

#print(ActivationFunction.SigmoidValue("",5.5,1032,-30000))