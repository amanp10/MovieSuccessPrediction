import scipy as sc
import string
from pybrain.structure import FeedForwardNetwork,RecurrentNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

data=sc.genfromtxt('data.tsv',delimiter='\t')
ds1=SupervisedDataSet(6,1)
ds=SupervisedDataSet(6,1)
ds2=SupervisedDataSet(6,1)
for i in range(0,120):
	ds1.addSample(data[i][2:8],data[i][8])
for i in range(120,150):
	ds2.addSample(data[i][2:8],data[i][8])
for i in data:
	ds.addSample(i[2:8],i[8])

n=FeedForwardNetwork()
inLayer = LinearLayer(6)
hiddenLayer = SigmoidLayer(6)
outLayer = LinearLayer(1)
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()

trainer=BackpropTrainer(n,ds)
x=trainer.trainUntilConvergence(maxEpochs=30,continueEpochs=10,validationProportion=0.2)
z=n.params

fi=open('result.txt','a')
fi.write(str(x)+'\n'+str(z)+'\n\n')
print x
print z
