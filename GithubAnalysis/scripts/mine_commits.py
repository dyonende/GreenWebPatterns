import re
import sys
import csv

from pydriller import Repository

projects = list()
with open("../data/filtered.txt") as infile:
    projects = infile.read().split('\n')
    

# regex to match commit messages
PATTERN_ENERGY = "(.*(energy).*)|(.*(battery).*)|(.*(power).*)"
regexEnergy = re.compile(PATTERN_ENERGY, re.IGNORECASE)

headers = ['project', 'hash', 'msg']
collected_commits = list()

def write_to_csv():
    with open('../data/commits_results.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(collected_commits)

counter = 1
for project in projects:
    print(f" project {counter}/{len(projects)}: {project}\t\t\t\t", end='\r',file=sys.stderr)
    counter+=1
    try:
        for commit in Repository('https://github.com/'+project).traverse_commits():
            msg = commit.msg
            match = regexEnergy.search(msg)
            
            if match:
                out_dict = {
                            "project": project,
                            "hash":commit.hash,
                            "msg":commit.msg
                            }
                collected_commits.append(out_dict)

    except KeyboardInterrupt:
        save = input("\nwrite to csv? (y/n)\t")
        if save=='y':
            write_to_csv()
        sys.exit()
    
    except Exception as e:
        print(f"\n{project} failed, {e}", file=sys.stderr)
        
write_to_csv()