import petab
import fides
import matplotlib.pyplot as plt
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import petab.visualize
import pypesto.visualize as visualize

# import to petab
petab_problem = petab.Problem.from_yaml(
    
   "../Kholodenko_PE_DetailedBalance/EGFR/EGFR.yaml"    #state the exact folder contains the yaml file
)
importer = pypesto.petab.PetabImporter(petab_problem)
# import to pypesto
problem = importer.create_problem()
model = importer.create_model(verbose=False)

# create optimizer object which contains all information for doing the optimization
options = {'maxiter':1000}
optimizer = optimize.FidesOptimizer(options=options)
#optimizer = optimize.ScipyOptimizer(method="TNC")
engine = pypesto.engine.MultiProcessEngine()



result = optimize.minimize(
    problem=problem, optimizer=optimizer, n_starts=200, engine=engine
)
from pypesto.visualize.model_fit import visualize_optimized_model_fit
pp1 = visualize_optimized_model_fit(petab_problem=petab_problem, result=result)
plt.savefig("Optimization_DB1.png")

#visualize.waterfall(result, scale_y="lin")
#plt.savefig("Waterfall_lin_1.png")
visualize.waterfall(result, scale_y="log10")
plt.savefig("Waterfall_DB1.png")
visualize.waterfall(result, offset_y=None, scale_y="lin")
plt.savefig("Waterfalllin_DB1.png")
visualize.parameters(result)
plt.savefig("Parameters_DB1.png")

zz = result.optimize_result.as_dataframe(["fval", "x"])
print (zz)


mle = result.optimize_result.list[0]['x']
print('MLE is :')
print(mle)










