import numpy as np
class Hypothesis():
    def HypothesisFunction(self,NodeValues,WeightArray):
        hypothesisArray = []
        for weightArray in WeightArray:
            NodeValues = np.array(NodeValues)
            WeightArray = np.array(weightArray)
            NextNodeValue = NodeValues * WeightArray
            SigmoidNodeValue = Hypothesis.Sigmoid("",sum(NextNodeValue))
            hypothesisArray.append(SigmoidNodeValue)
        return hypothesisArray
    def Sigmoid(self,Value):
        SigmoidValue = 1/(1 + np.exp(-Value))
        return SigmoidValue