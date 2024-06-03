import subprocess
import numpy as np

for distribution in [ 'Physics',
                     'rnd_graph_800vertices_unweighted',
                     'rnd_graph_800vertices_weighted',
                     'toroidal_grid_2D_800vertices_weighted',
                     'planar_800vertices_unweighted',
                     'planar_800vertices_weighted',
                     'ER_200',
                     'BA_200',
                     'HomleKim_800vertices_unweighted',
                     'HomleKim_800vertices_weighted',
                     'BA_800vertices_unweighted',
                     'BA_800vertices_weighted',
                     'WattsStrogatz_800vertices_unweighted',
                     'WattsStrogatz_800vertices_weighted',
                     'SK_spin_70_100vertices_weighted',
                     'dense_MC_100_200vertices_unweighted',
                     ]:
    for tau in np.arange(1.1,1.6,0.1):
        print(f'Distribution:{distribution} Tau:{tau}')
        command= f'python EO.py --distribution {distribution} --tau {tau}'

        subprocess.run(command,shell=True,check=True)
    break
