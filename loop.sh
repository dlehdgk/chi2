#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mail-type=fail,end
#SBATCH --mail-user=dhlee1@sheffield.ac.uk

module load Anaconda3/2019.07
source activate cosmos
module load OpenMPI/4.0.3-GCC-9.3.0
module load OpenBLAS/0.3.9-GCC-9.3.0
module load CFITSIO/3.48-GCCcore-9.3.0

for beta in $(seq -1 0.1 1); do
  echo "Running for beta = $beta"
  sed -i '/^\s*override:\s*$/ {n;s|^\s*beta_DE:\s*.*|      beta_DE: '"$beta"'|;}' beta.yaml
  sed -i "s|^output:.*|output: ./beta/$beta|" beta.yaml
  cat beta.yaml
  
  source /users/smp24dhl/cosmo/code/planck/clik/bin/clik_profile.sh
  mpirun -np 1 cobaya-run beta.yaml
done
