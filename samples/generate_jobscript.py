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
