from qeinput.material import Material
from qeinput.inputs import InputPW

key = "Your API key of the the Materials Project"
Si = Material(key, "mp-149")
Si_input = InputPW(Si, "./pseudo_dir", [8, 8, 8])
Si_input.generate(Si.formula_pretty+".scf.in")
