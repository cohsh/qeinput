import textwrap

slurm = {}

slurm["shebang"] = textwrap.dedent('''#!/bin/{shell}
#SBATCH -p {partition}
#SBATCH -N {nodes}
#SBATCH -n {ntasks}
#SBATCH -c {cpus_per_task}
#SBATCH -o "{output}"
#SBATCH -e "{error}"
#SBATCH -J {job_name}

''')

slurm["srun"] = "srun {program} {option} < {infile} > {outfile}\n"
