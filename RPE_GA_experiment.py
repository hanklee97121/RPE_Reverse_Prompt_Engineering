import pandas as pd
import json
from tqdm.notebook import trange, tqdm #if running in jupyter notebook
#from tqdm import trange, tqdm #if running python script
from RPE_ga import Reverse_Prompt_Engineering
#read answer file if initial answers are provided
# with open("results/ori_answers.json", "r") as f:
#     ori_answers = json.load(f)
#read dataset
data_prompt = pd.read_csv("RE_hard.csv", index_col=0)
list_prompt = list(data_prompt["prompt"])

#record initial answers
ori_answers = []
#record final answer
final_outputs = []
#initialize optimizer
RPE = Reverse_Prompt_Engineering(X=5, N=5, model="gpt-3.5-turbo", tag_model="en_core_web_trf")
n = len(list_prompt)
print("Algorithm starts")
for i in trange(n):
    p = list_prompt[i]
    RPE.reset(X=5, N=5)
    #o_answers = ori_answers[i]
    RPE.generate_answers(prompt=p, answers=[], n=5)
    #RPE.generate_answers(prompt=p, answers=o_answers, n=5)
    output = RPE(ini_prompts=None, ini_scores=None, ini_total_scores=None, ini_answers=None)
    final_outputs.append(output)
    ori_answers.append(RPE.answers)
    
#save final prompt and initial answers
with open('results/final_outputs.json', 'w') as outfile:
    json.dump(final_outputs, outfile)
with open('results/ori_answers.json', 'w') as outfile:
    json.dump(ori_answers, outfile)
