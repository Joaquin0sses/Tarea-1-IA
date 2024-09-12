#importación de matplotlib. La versión debe ser >= 3.3.4
import matplotlib as mpl
import matplotlib.pyplot as plt
print(mpl.__version__)

#importar pandas y numpy. numpy permite trabajar con arreglos, matrices y vectores. Pandas se utiliza para analizar manipular datos.
import numpy as np
import pandas as pd
print(pd.__version__)
print(np.__version__)

#importar pgmpy. Esta libreria permite crear, manipular e implementar grafos de modelos probabilísticos.
import pgmpy
print(pgmpy.__version__)

import bnlearn
print(bnlearn.__version__)
