'''
       I need to learn sql for this part as we initialize the weights here and also call on it when we do initialize it
       the weight array should look something like this [[[1,2],[1,2],[1,2]],[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]]
       The Arrays inside of the array are the weights [[1,2],[1,2],[1,2]]
       This indicates to use that we are currently are in a layer with 2 nodes and the next layer should have 3 nodes
       [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
       This indicates to us that we have 3 nodes in our current layer which is the same as the next layer as the previous
       layer. They need to be this way to work with our algorithms. The next layer has 4 nodes since there are 4 arrays in
       the current array.
'''
from ModelReworked.DataBaseCalls import Weights
import numpy as np
from ModelReworked.FeedForwarding import FeedForward
class BackPropagation():
    def Training(self,Inputs,ExpectedOutputs):
        WeightMatrix = Weights.CallingTheWeights("")
        #for pos in range(len(Inputs)):


    #This gets the error of the output this has to go at the start
    #Checked
    def OutputError(self,expectedOutputs,predictions):
        error_Array = []
        for pos in range(1,len(expectedOutputs)):
            error = predictions[pos] - expectedOutputs[pos - 1]
            error_Array.append(error)
        print(f"The output error is {error_Array}")
        return error_Array
    #This gets the error of a single hidden layer using the previous hidden layer
    #Checked
    def errorValuesHiddenlayer(self,weightsArray,errorArray,nodeValuesActivatedVector):
        hiddenLayerError = []
        for ValuePos in range(len(nodeValuesActivatedVector)):
            error = 0
            for WeightPos in range(len(errorArray)):
                error += weightsArray[WeightPos][ValuePos] * errorArray[WeightPos]
            DeriavtiveOfNodeValue = nodeValuesActivatedVector[ValuePos] * (1 - nodeValuesActivatedVector[ValuePos])
            print(DeriavtiveOfNodeValue)
            error *= DeriavtiveOfNodeValue
            hiddenLayerError.append(error)
        return hiddenLayerError

    #This creates the capital delta array which is the same dimensions of an array so its [[1,2],[3,4],[5,6]]
    #Checked
    def capitalDelta(self,NodeValuesArray,errorVector):
        CapitalDelta3dArray = []
        for error in errorVector:
            CapitalDeltaArray = []
            for nodeValue in NodeValuesArray:
                CapitalDelta = nodeValue * error
                CapitalDeltaArray.append(CapitalDelta)
            CapitalDelta3dArray.append(CapitalDeltaArray)
        return CapitalDelta3dArray


    def PartialDerivatives3dArray(self,CapitalDelta3dArray,Weights3dArray,NodeValues,DataInBatch):
        PartialDerivative3dArray = []
        for pos in range(len(NodeValues)):
            PartialDerivativeArray = []
            for ArrayValue in range(len(Weights3dArray[pos])):
                CurrentNodeValue = NodeValues[pos]
                if  CurrentNodeValue == 0:
                    PartialDerivative = 1/DataInBatch * CapitalDelta3dArray[pos][ArrayValue]
                    PartialDerivativeArray.append(PartialDerivative)
                else:
                    PartialDerivative = 1/DataInBatch * CapitalDelta3dArray[pos][ArrayValue]
                    PartialDerivativeReg = PartialDerivative * 1/(2 * DataInBatch) * Weights3dArray[pos][ArrayValue]
                    PartialDerivativeArray.append(PartialDerivativeReg)
            PartialDerivative3dArray.append(PartialDerivativeArray)
        return PartialDerivative3dArray

    def GettingWeights(self,PartialDerivativeMatrix,weightsMatrix):
        for LayerPointer in range(len(PartialDerivativeMatrix)):
            for ArrayPointer in range(len(PartialDerivativeMatrix)):
                for valueInArray in range(len(PartialDerivativeMatrix[ArrayPointer])):
                    weightsMatrix[LayerPointer][ArrayPointer][valueInArray] -= PartialDerivativeMatrix[LayerPointer][ArrayPointer][valueInArray]
            return weightsMatrix
Inputs = [[3,4,6,2],[3,5,7,1]]
#expectedOutputs = [[1,0,0],[1,0,0]]
#BackPropagation.Training("",Inputs,expectedOutputs)
'''
#Testing hiddenLayererror function and it works mathematically
w = [[.1,.7,.3],[.1,.2,.7]]
error = [.3,.6]
NodeValues = [1,.7,.3]
print(BackPropagation.errorValuesHiddenlayer("",w,error,NodeValues))
'''

#Testing capitalDelta array which also works mathematically


NodeValueMatrix = FeedForward.GettingNodeValueMatrix("",Inputs[0])
errorArray = [0.2,0.3,0.2]
print(NodeValueMatrix[-2])
capitalDeltaArray = BackPropagation.capitalDelta("",NodeValueMatrix[-2],errorArray)
print(capitalDeltaArray)
WeightMatrix = Weights.CallingTheWeights("")
print(WeightMatrix[2])


#Testing partialDerivativeFunction to check if it works mathematically

PartialDerivativeArray1 = BackPropagation.PartialDerivatives3dArray("",capitalDeltaArray,WeightMatrix[-1],NodeValueMatrix[-1],len(Inputs))
PartialDerivativeArray2 = BackPropagation.PartialDerivatives3dArray("",capitalDeltaArray,WeightMatrix[-1],NodeValueMatrix[-2],len(Inputs))
print(PartialDerivativeArray1)
print(PartialDerivativeArray2)

