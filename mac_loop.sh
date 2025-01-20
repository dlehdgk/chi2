#!/bin/bash

for b in $(seq 0.000 0.0001 0.002); do
  echo "Running for beta = $b"

  # Update the beta_DE value in the params file
  sed -i '' -e '/^[[:space:]]*beta_DE:[[:space:]]*$/{
    n
    s|^[[:space:]]*value:[[:space:]]*.*|    value: '"$b"'|
  }' beta.yaml

  # Update the output directory
  sed -i '' -e "s|^output:.*|output: ./beta/$b-beta|" beta.yaml

  # print the updated yaml file
  #cat beta.yaml

  # Run cobaya
  source /Users/dongha/Projects/cosmo/code/planck/clik/bin/clik_profile.zsh
  mpirun -np 1 cobaya-run beta.yaml
done
