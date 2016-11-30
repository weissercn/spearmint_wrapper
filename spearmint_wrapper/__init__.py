import sys
import os
working_dir = os.getcwd()
sys.path.insert(0, '.')
sys.path.insert(0, working_dir )

import optimise_hyperparam
import setup_optimise_hyperparam
from optimise_hyperparam import spearmint_example


