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
