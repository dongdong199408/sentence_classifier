# -*- coding: utf-8 -*-
# @Author: Miaoxudong
import pandas as pd
import numpy as np
import json
import os

class Json_data(object):
    def __init__(self,file='AI_comments.csv'):
        self.file=file
        self.data_file='json_data.json'
        self.json_data_file=os.path.join('./data',self.data_file)
        self.data,self.type_dict=self.load_data(os.path.join('./data',self.file))
        self.to_json(self.data)
        self.comment_data=self.read_JSON(os.path.join('./data',self.data_file))

    def load_data(self,file):
        f=open(file,encoding='utf8')
        data=pd.read_csv(f,index_col=None,low_memory=False)
        one_class=np.unique(data['大类'])
        type_dict = {}
        for one in one_class:
            one_data=data[data['大类']==one]
            for o in one_data['属性']:
                type_dict[o]=one
        return data,type_dict

    def to_json(self,data):
        #转化为一级分类 等级，话术的字典
        #初始化json
        conjunction=pd.read_csv('./data/AI_connection.csv',index_col=None,low_memory=False)
        position=np.unique(conjunction['位置'])
        data_json={'title':'晓黑板-晓评价'}
        for p in position:
            nature = list(conjunction[conjunction['位置']==p]['性质'])
            corpus = list(conjunction[conjunction['位置']==p]['语料'])
            data_json[p]={nature[i]:corpus[i].strip().split('/') for i in  range(len(nature))}
        #对一级分类去重
        stytle=data['属性']
        unique_stytle=np.unique(stytle)
        for s in unique_stytle:
            s_data=data[data['属性']==s]
            data_json[s]={s_data['等级'][i]:s_data['评语'][i].split('/') for i in s_data.index}
        with open(self.json_data_file,'w',encoding='utf8') as jf:
            json.dump(data_json, jf, ensure_ascii=False, indent=4)
            print("write json file success!")

    def read_JSON(self,fileName):
        if fileName != '':
            strList = fileName.split(".")
            if strList[len(strList) - 1].lower() == "json":
                with open(fileName, mode='r', encoding="utf-8") as file:
                    return json.loads(file.read())

if __name__=='__main__':
    data=Json_data()
    import random
    ans='平稳'
    while '平稳' in ans:
        ans=random.choice(data.comment_data['stationarity']['高'])
    print(ans)
