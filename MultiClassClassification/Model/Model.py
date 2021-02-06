from MultiClassClassification.Model.Hypothesis import Hypothesis
weightmatrix = [[[1,4],[2,5],[3,6]],[[7,10,13],[8,11,14],[9,12,15]]]
Inputs = [[3,4],[6,7]]
NextLayer = Inputs[0]
for x in range(len(weightmatrix)):
    NextLayer = Hypothesis.HypothesisFunction("",NextLayer,weightmatrix[x])
    print(NextLayer)
