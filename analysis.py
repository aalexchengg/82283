from collections import defaultdict
import re

swear_words = ['arse', 'ass',  'bastard', 'bitch', 'bloody',
                'fuck', 'shit', 'damn', 'dick', 'frig', 'hell',
                'jesus', 'piss', 'pussy', 'whore', 'turd', 'twat',
                'wanker']
# common_ass_words = ['glass', 'bass','embarrass', 'bass', 'sass',
#                      'lass', 'pass', 'mass', 'tass', 'grass', 
#                      'brass', 'crass', 'harass', 'carcass', 'surpass', 
#                      'compass']
# community = "OVER30REDDIT"
community = "teenagers"
filename = "{}.txt".format(community)

res = defaultdict(lambda: 0)
before = defaultdict(lambda: defaultdict(lambda: 0))
after = defaultdict(lambda: defaultdict(lambda: 0))
with open(filename, 'r', encoding = "utf-8") as file:
    for line in file:
        sline = line
        line = line.split(" ")
        for i in range(len(line)):
            for sw in swear_words:
                if '/' in line[i]:
                    continue
                s = re.sub(r'[^a-zA-Z0-9]', '', line[i]).lower()
                if sw in s:
                    res[s] += 1
                    if(i != 0):
                        sbefore = re.sub(r'[^a-zA-Z0-9]', '', line[i-1]).lower()
                        before[s][sbefore] += 1
                    if (i != len(line) - 1):
                        safter = re.sub(r'[^a-zA-Z0-9]', '', line[i+1]).lower()
                        after[s][safter] += 1

sorted_response = sorted(res.items(), key = lambda x: x[1], reverse = True)
with open("{}_sorted_output.txt".format(community), 'w', encoding = 'utf-8') as file:
    for word in sorted_response:
        file.write("SWEAR WORD: {}; COUNT {}\n".format(word[0], word[1]))
        bdict = sorted(before[word[0]].items(), key = lambda x: x[1], reverse = True)
        file.write("{} UNIQUE WORDS BEFORE: {}\n".format(len(before[word[0]]), bdict))
        adict = sorted(after[word[0]].items(), key = lambda x: x[1], reverse = True)
        file.write("{} UNIQUE WORDS AFTER: {}\n".format(len(after[word[0]]), adict))



                    