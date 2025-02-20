# Logan Richan
# ph295

from numpy.linalg import solve
from numpy import array

#Resistances in Ohms
RAB=2
RBC=3
RCD=2
RDE=1
REF=4
RFG=3
RBF=5
RCE=2

Vt=12 # Voltage in V

#Ax=b
A = array([[RAB+RFG, RBF, 0,       0,   0      ],
           [RAB+RFG, 0,   RBC+REF, RCE, 0      ],
           [RAB+RFG, 0,   RBC+REF, 0,   RCD+RDE],
           [1,      -1,  -1,       0,   0      ],
           [0,       0,   1,      -1,  -1      ]], float)

b = array([Vt, Vt, Vt, 0, 0], float)

x = solve(A,b)
print(x)
