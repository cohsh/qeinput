# QEInput (Under Construction)
Python Package for automatic generation of Quantum ESPRESSO input files
## Install
```Shell
pip install .
```

## Sample
`./samples/silicon.py`
```Python
from qeinput.material import Material
from qeinput.inputs import InputPW

key = "Your API key of the the Materials Project"
Si = Material(key, "mp-149")
Si_input = InputPW(Si, "./pseudo_dir", [8, 8, 8])
Si_input.generate(Si.formula_pretty+".scf.in")
```

## Disclaimer
I am not responsible for any detriment caused by the use of this package.
