
#!/bin/bash
#SBATCH -p i8cpu
#SBATCH -N 1
#SBATCH -n 128
#SBATCH -c 1
#SBATCH -o "std.out"
#SBATCH -e "std.err"
#SBATCH -J test
