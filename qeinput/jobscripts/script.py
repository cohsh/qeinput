from qeinput.consts import Shebang


class JobScript:
    shebang = Shebang().SLURM

    def __init__(self, file_name, partition, shell="bash",
                 nodes=1, ntasks=128, cpus_per_task=1,
                 output="std.out", error="std.err",
                 job_name="test"):

        self.file_name = file_name

        string = self.shebang.format(
                shell=shell, partition=partition, nodes=nodes, ntasks=ntasks,
                cpus_per_task=cpus_per_task, output=output, error=error,
                job_name=job_name
                )

        with open(self.file_name, mode="w") as f:
            f.write(string)
