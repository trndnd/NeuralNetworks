from ModelReworked.DataBaseCalls import Weights
import numpy as np
class FeedForward():
    def GettingNodeValueMatrix(self,InputArray):
        WeightMatrix = Weights.CallingTheWeights("")
        Array = [1]
        for Input in InputArray:
            Array.append(Input)
        NodeValueMatrix = [Array]
        for ValuePointer in range(len(WeightMatrix)):
            LayerValues = [1]
            LayerValues = FeedForward.GettingLayerValues("",NodeValueMatrix[ValuePointer],WeightMatrix[ValuePointer])
            NodeValueMatrix.append(LayerValues)
        return NodeValueMatrix

    def GettingLayerValues(self,NodeLayerValues,WeightArray):
        LayerValues = [1]
        for weights in WeightArray:
            NodeValue = np.matmul(NodeLayerValues,weights)
            NodeValue = FeedForward.sigmoid("",NodeValue)
            LayerValues.append(NodeValue)
        return LayerValues

    def sigmoid(self,Value):
        SigmoidValue = 1/(1 + np.exp(-Value))
        return SigmoidValue

'''
Inputs = [1,.3, .9, .4, .6]
NodeValueMatrix = FeedForward.GettingWeightMatrix("",Inputs)
print(NodeValueMatrix)
'''