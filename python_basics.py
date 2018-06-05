# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# find common elements in multiple lists
set.intersection(*[set(list) for list in p])
