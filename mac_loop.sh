#!/bin/bash

for beta in $(seq -0.1 0.001 0.1); do
  echo "Running for beta = $beta"
  sed -i '/^\s*beta_DE:\s*$/ {n;s|^\s*value:\s*.*|    value: '"$beta"'|;}' beta.yaml
  sed -i "s|^output:.*|output: ./beta/$beta-beta|" beta.yaml
  
  source /users/smp24dhl/cosmo/code/planck/clik/bin/clik_profile.zsh
  mpirun -np 1 cobaya-run beta.yaml
done
