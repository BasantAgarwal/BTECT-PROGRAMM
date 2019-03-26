pso_max_iteration = 1000
goa_max_iteration = 100
goa_population_size = 30
pso_population_size = 30  # should be in multiple of 3.
no_of_classes = None
max_no_of_neurons = None  # initialize in GOA.py in method name give_random_solutions
minimum_no_of_present_features = 2  # if None, it will automatically set to (no_of_features/2) (GOA.py line 17)
CEE_weight = 0.3  # Cross_entropy error weightage
v_error_weight = 0.4  # validation error weightage
arch_penalty_weight = 0.2  # architecture penalty weightage
feature_penalty_weight = 0.1  # feature penalty weightage
