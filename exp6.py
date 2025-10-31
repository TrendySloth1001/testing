# 6. Create a Bayesian Network for the given Problem Statement and draw inferences from it.
# (You can use any Belief and Decision Networks Tool for modeling Bayesian Networks). -i want example code for bayesian network using pgmpy library in pythonfrom pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD   
# Define the structure of the Bayesian Network
model = BayesianNetwork([('Rain', 'Traffic'),
                         ('Accident', 'Traffic'),
                         ('Traffic', 'Late')])
# Define the Conditional Probability Distributions (CPDs)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])  # P(Rain)
cpd_accident = TabularCPD(variable='Accident', variable_card=2, values=[[0.9], [0.1]])  # P(Accident)
cpd_traffic = TabularCPD(variable='Traffic', variable_card=2,
                             values=[[0.95, 0.8, 0.6, 0.1],
                                     [0.05, 0.2, 0.4, 0.9]],
                             evidence=['Rain', 'Accident'],
                             evidence_card=[2, 2])  # P(Traffic | Rain, Accident)
cpd_late = TabularCPD(variable='Late', variable_card=2,
                         values=[[0.9, 0.4],
                                 [0.1, 0.6]],
                         evidence=['Traffic'],
                         evidence_card=[2])  # P(Late | Traffic)
# Add CPDs to the model
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic, cpd_late)
# Verify the model
assert model.check_model()
# Perform inference
inference = VariableElimination(model)
# Query the probability of being late given that it is raining
query_result = inference.query(variables=['Late'], evidence={'Rain': 1})
print(query_result)
# Query the probability of traffic given that there is an accident
query_result_traffic = inference.query(variables=['Traffic'], evidence={'Accident': 1})
print(query_result_traffic) 