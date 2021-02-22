from pymongo import MongoClient
from random import randint
class Weights():
    def InitilizeWeightsMatrix(self,NumberOfInputs,NumberOfOutPuts,NumberOfhiddenLayers,HiddenLayerSize):
        weightMatrix = []
        if NumberOfhiddenLayers != 0:
            InputWeightArray = Weights.InitilizingWeightArray("",NumberOfInputs,HiddenLayerSize)
        else:
            InputWeightArray = Weights.InitilizingWeightArray("",NumberOfInputs,NumberOfOutPuts)
        weightMatrix.append(InputWeightArray)
        for x in range(NumberOfhiddenLayers):
            if x == NumberOfhiddenLayers - 1:
                Weight3dArray = Weights.InitilizingWeightArray("",HiddenLayerSize,NumberOfOutPuts)
                weightMatrix.append(Weight3dArray)
            else:
                Weight3dArray = Weights.InitilizingWeightArray("",HiddenLayerSize,HiddenLayerSize)
                weightMatrix.append(Weight3dArray)
        Weights.AddingMatrixToDb("",weightMatrix)

    def InitilizingWeightArray(self,CurretLayerSize,sizeOfNezxtLayer):
        Weight3dArray = []
        bias = randint(1,9)/10
        for x in range(sizeOfNezxtLayer):
            #This starts with a random bias so the fist number in the array is the bias
            WeightArray = [bias]
            for y in range(CurretLayerSize):
                randomNumber = randint(1,9)/10
                WeightArray.append(randomNumber)
            Weight3dArray.append(WeightArray)
        return Weight3dArray

    def AddingMatrixToDb(self,WeightMatrix):
        client = MongoClient('localhost', 27017)
        db = client.MongoWithPython
        collection = db.Arrays
        query = {"_id": "Aaron"}
        replacement_data = {"WeightMatrix": WeightMatrix}
        collection.replace_one(query, replacement_data)

    def CallingTheWeights(self):
        client = MongoClient('localhost', 27017)
        db = client.MongoWithPython
        collection = db.Arrays
        result = collection.find_one()
        return result["WeightMatrix"]
Weights.InitilizeWeightsMatrix("",2,1,0,0)
print(Weights.CallingTheWeights(""))
