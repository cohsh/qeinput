# QEInput (Under Construction)
Python Package for automatic generation of Quantum ESPRESSO input files
## Install
```Shell
pip install .
```

## Sample
Generate a job script `job.sh` to run a pw.x (scf) calculation of silicon using data on Materials Project.

`./samples/generate_jobscript.py`
```Python
from qeinput.material import Material
from qeinput.inputs import SlurmJob
from qeinput.inputs import InputPW

key = "Your API key of the Materials Project"

Si = Material(key, "mp-149")

Si_input = InputPW(Si, "scf", "./pseudo_dir", [8, 8, 8], 60)
prefix = Si.formula_pretty
pw_infile = prefix + ".scf.in"
pw_outfile = prefix + ".scf.out"
Si_input.generate(pw_infile)

job = SlurmJob("PartitionName", 1, 128, 1)
job.add_srun("pw.x", "", pw_infile, pw_outfile)
job.generate("job.sh")
```

## To be implemented
- pw.x
- ph.x
- matdyn.x
- q2r.x
- epw.x

## Disclaimer
I am not responsible for any detriment caused by the use of this package.
