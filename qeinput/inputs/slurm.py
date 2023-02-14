import qeinput.formats as formats
from qeinput.inputs import InputBase


class SlurmJob(InputBase):
    shell = "bash"

    def __init__(self, partition,
                 nodes, ntasks, cpus_per_task,
                 output="std.out", error="std.err",
                 job_name="test"):
        super().__init__()

        shebang = formats.slurm["shebang"].format(
                shell=self.shell, partition=partition, nodes=nodes, ntasks=ntasks,
                cpus_per_task=cpus_per_task, output=output, error=error,
                job_name=job_name
                )
        self.text += shebang

    def change_shell(self, shell):
        self.shell = shell

    def add_text(self, text):
        self.text += text

    def add_srun(self, program, option, infile, outfile):
        string = formats.slurm["srun"].format(
                program=program, option=option,
                infile=infile, outfile=outfile
                )
        self.add(string)
