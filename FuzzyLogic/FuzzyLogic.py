import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import string
import scipy as sc
from cmath import sqrt

data=sc.genfromtxt('data.tsv',delimiter='\t')

#input universe
actor = ctrl.Antecedent(np.arange(0, 6, 1), 'actor')
director = ctrl.Antecedent(np.arange(0, 6, 1), 'director')
genre = ctrl.Antecedent(np.arange(0,19,1), 'genre')
rating = ctrl.Consequent(np.arange(0, 11, 1), 'rating')

#membership functions
actor['low'] = fuzz.trapmf(actor.universe, [0,0,1,2])
actor['medium'] = fuzz.trapmf(actor.universe, [1,2,3,4])
actor['high'] = fuzz.trapmf(actor.universe, [3,4,5,5])
director['low'] = fuzz.trapmf(director.universe, [0,0,1,2])
director['medium'] = fuzz.trapmf(director.universe, [1,2,3,4])
director['high'] = fuzz.trapmf(director.universe, [3,4,5,5])
genre['low'] = fuzz.trapmf(genre.universe, [0,0,9,11])
genre['medium'] = fuzz.trapmf(genre.universe, [9,10,11,12])
genre['high'] = fuzz.trapmf(genre.universe, [10,12,18,18])
rating['poor'] = fuzz.trapmf(rating.universe, [0,0,2,3])
rating['Bavg'] = fuzz.trapmf(rating.universe, [2,3,4,5])
rating['avg'] = fuzz.trapmf(rating.universe, [4,5,6,7])
rating['high'] = fuzz.trapmf(rating.universe, [6,7,8,9])
rating['Vhigh'] = fuzz.trapmf(rating.universe, [8,9,10,10])

genre.view()
x=raw_input('> ')

#rules
rule1 = ctrl.Rule(genre['high'] & actor['high'] & director['high'], rating['Vhigh'])
rule2 = ctrl.Rule(genre['high'] & ((actor['medium'] & director['high']) | (actor['high'] & director['medium'])), rating['high'])
rule3 = ctrl.Rule(genre['high'] & ((actor['low'] & director['high']) | (actor['high'] & director['low'])), rating['avg'])
rule4 = ctrl.Rule(genre['high'] & actor['low'] & director['low'], rating['Bavg'])
rule5 = ctrl.Rule(genre['high'] & actor['medium'] & director['medium'], rating['avg'])
rule6 = ctrl.Rule(genre['high'] & ((actor['low'] & director['medium']) | (actor['medium'] & director['low'])), rating['Bavg'])
rule7 = ctrl.Rule(genre['low'] & actor['high'] & director['high'], rating['high'])
rule8 = ctrl.Rule(genre['low'] & ((actor['medium'] & director['high']) | (actor['high'] & director['medium'])), rating['avg'])
rule9 = ctrl.Rule(genre['low'] & ((actor['low'] & director['high']) | (actor['high'] & director['low'])), rating['Bavg'])
rule10 = ctrl.Rule(genre['low'] & actor['low'] & director['low'], rating['poor'])
rule11 = ctrl.Rule(genre['low'] & actor['medium'] & director['medium'], rating['Bavg'])
rule12 = ctrl.Rule(genre['low'] & ((actor['low'] & director['medium']) | (actor['medium'] & director['low'])), rating['poor'])
rule13 = ctrl.Rule(genre['medium'] & actor['high'] & director['high'], rating['high'])
rule14 = ctrl.Rule(genre['medium'] & ((actor['medium'] & director['high']) | (actor['high'] & director['medium'])), rating['high'])
rule15 = ctrl.Rule(genre['medium'] & ((actor['low'] & director['high']) | (actor['high'] & director['low'])), rating['avg'])
rule16 = ctrl.Rule(genre['medium'] & actor['low'] & director['low'], rating['poor'])
rule17 = ctrl.Rule(genre['medium'] & actor['medium'] & director['medium'], rating['avg'])
rule18 = ctrl.Rule(genre['medium'] & ((actor['low'] & director['medium']) | (actor['medium'] & director['low'])), rating['Bavg'])

#controller
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4, rule5, rule6,rule7, rule8, rule9,rule10, rule11, rule12])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

#Simulation
sum1=0
list1=[]
for i in data:
	tipping.input['actor'] = int(i[2])
	tipping.input['director'] = int(i[3])
	tipping.input['genre'] = int(i[7])
	tipping.compute()
	k=abs(tipping.output['rating']-int(i[8]))
	list1.append(k)
	sum1=sum1+k

avg=sum1/150
fi=open('FL.txt','w')
fi.write(str(avg)+'\n')
for i in list1:
	fi.write(str(i)+'\n')
print avg
