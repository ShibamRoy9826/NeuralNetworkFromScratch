## A dummy neuron to understand about the concepts
# Random inputs,weights and biases
inputs = [1,2,2.2,1.5]

weights = [[-1,0.1,1,-2.4,1.3],
           [-0.7,0.2,-2.2,-1.9],
           [-1.2,0.5,-2.2,1.7]]

biases = [1.1,2.1,3,1]

layer_ouputs=[]

# A Very naive approach of calculating output of neuron
for w,b in zip(weights,biases):
    output=0
    for inp,weight in zip(inputs,weights):
        ouput+=inp*weight
    output+=b
    layer_ouputs.append(output)
print(layer_ouputs)
