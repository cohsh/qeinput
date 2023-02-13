# QEInput (Under Construction)
Python Package for automatic generation of Quantum ESPRESSO input files
and Slurm scripts.
## Install
```Shell
pip install .
```

## Sample
Generate a job script `job.sh` to run a pw.x (scf and nscf) calculation of silicon using data on Materials Project.

`./samples/generate_jobscript.py`
```Python
from qeinput.material import Material
from qeinput.inputs import SlurmJob, InputPWSCF, InputPWNSCF


def main():
    job = SlurmJob("PartitionName", 1, 128, 1)

    key = "Your API key of the Materials Project"

    Si = Material(key, "mp-149")
    prefix = Si.formula_pretty

    Si_input_scf = InputPWSCF(Si, "./pseudo_dir", 60, [8, 8, 8])
    Si_input_nscf = InputPWNSCF(Si, "./pseudo_dir", 60,
                                [[0.0, 0.0, 0.0], [0.5, 0.5, 0.5]], 10)

    Si_inputs = {"scf": Si_input_scf, "nscf": Si_input_nscf}

    for calc, Si_input in Si_inputs.items():
        infile = prefix + "." + calc + ".in"
        outfile = prefix + "." + calc + ".out"
        Si_input.generate(infile)

        job.add_srun("pw.x", "", infile, outfile)

    job.generate("job.sh")


if __name__ == "__main__":
    main()
```

## To be implemented
- pw.x (vc-relax)
- ph.x
- matdyn.x
- q2r.x
- epw.x

## Disclaimer
I am not responsible for any detriment caused by the use of this package.
