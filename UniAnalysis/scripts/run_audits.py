import sys
import pandas as pd
import glob
import subprocess


# export CHROME_PATH=/usr/bin/google-chrome
# NODE_PATH=.. yarn lighthouse https://blog.hubspot.com/website/html-video --plugins=lighthouse-plugin-sus --output=json --output-path=./report.json

df_top_100 = pd.read_csv("/mnt/d/dev/GreenWebPatterns/UniAnalysis/data/top100.csv", sep=';')
df_bottom_100 = pd.read_csv("/mnt/d/dev/GreenWebPatterns/UniAnalysis/data/bottom100.csv", sep=';')

def process_top_100(df):
    for row in df.itertuples():
        url = row[-1]
        rank = row[1]
        uni_name = row[2].replace('(', '').replace(')','').replace('|','')
        of_name = str(rank) + '_' + uni_name.replace(' ', '_')
        output_path = f"/mnt/d/dev/GreenWebPatterns/UniAnalysis/data/top100results/{of_name}.json"
        command = f"NODE_PATH=.. yarn lighthouse {url} --plugins=lighthouse-plugin-sus --output=json --output-path={output_path}"
        
        print(row[0], uni_name)

        return_value = subprocess.call(command,shell=True, cwd=r'/mnt/d/dev/lighthouse-plugin-sus/', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        if return_value != 0:
            print("failed, trying again")
            return_value = subprocess.call(command,shell=True, cwd=r'/mnt/d/dev/lighthouse-plugin-sus/', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            if return_value != 0:
                print("failed again")
            
def process_bottom_100(df):
    for row in df.itertuples():
        url = row[-1]
        uni_name = row[1].replace('(', '').replace(')','').replace('|','')
        of_name = uni_name.replace(' ', '_')
        output_path = f"/mnt/d/dev/GreenWebPatterns/UniAnalysis/data/bottom100results/{of_name}.json"
        command = f"NODE_PATH=.. yarn lighthouse {url} --plugins=lighthouse-plugin-sus --output=json --output-path={output_path}"
        
        print(row[0], uni_name)

        return_value = subprocess.call(command,shell=True, cwd=r'/mnt/d/dev/lighthouse-plugin-sus/', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        if return_value != 0:
            print("failed, trying again")
            return_value = subprocess.call(command,shell=True, cwd=r'/mnt/d/dev/lighthouse-plugin-sus/', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            if return_value != 0:
                print("failed again")

        

process_top_100(df_top_100)

process_bottom_100(df_bottom_100)


