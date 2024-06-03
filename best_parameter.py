import os
import pandas as pd
import pickle 

from collections import defaultdict

results=defaultdict(list)

def load_pickle(file_path):
   
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

root_folder='pretrained agents'
for folder in os.listdir(root_folder):
    folder_path=os.path.join(root_folder,folder,'data')

    best_mean=0

    for file in os.listdir(folder_path):
        file_path=os.path.join(folder_path,file)

        if not file_path.endswith('results'):
            df=load_pickle(file_path)

            if best_mean<df['EO'].mean():
                results['cut']=df['EO']
                results['tau']=df['tau']
                best_mean=df['EO'].mean()

    # print(folder)
    # print(results['tau'].iloc[0])
    if results['tau'].iloc[0]>1.41:
        print(folder)
    # print(results[''])
    df=pd.DataFrame(results)
    df.to_pickle(os.path.join(folder_path,'results'))
    # break

    # print()
    


