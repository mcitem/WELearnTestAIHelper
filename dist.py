def api(string):
    try:
        with open(f'./dist/{string}.txt','rt') as fff:
            return fff.read()
    except:
        return '未找到对应的题目内容--------------'
from utils.data import data;
count = 1 # 题目序号
data = data['data']
dist = ''
itemDivs_count = 0
for itemDiv in data:
    itemDivs_count +=1
    dist += f'第 {itemDivs_count} 段文章' + api(itemDiv['test_center_link']) + '\n'

    hovs_count = 0

    for hov in itemDiv['test_hovs']:
        hovs_count +=1
        hov['test_hov_link']
        dist += ' 第' + str(count) + '题' + api(hov['test_hov_link']) + '\n'
        #print(count,hov['test_hov_link'])
        for choi in hov['choices']:
            dist += '   ' + choi + '\n'
        count+=1
    #print(itemDIV_count)

with open('./output.txt','wt+',encoding='utf-8') as f:
    f.write(dist)

