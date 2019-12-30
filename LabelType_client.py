from label_classifier_pb2 import Label, Label_class
from label_classifier_pb2_grpc import LabelTypeStub
import random
import json
from data_process import Json_data
import re
import pandas as pd
import grpc
json_data=Json_data()
data=json_data.data
data.dropna(inplace=True)
#删除简介，清洗标签
res=re.compile('(.*\n)|([【】])')
Synonyms_type = {
            '实践能力': '实践', '行为习惯': '行为习惯', '人格品质': '人格品质',
            '人际沟通': '沟通', '体育': '运动', '理想信念': '理想信念',
            '课业质量': '学业', '知识技能': '知识掌握', '创新意识': '创新思维',
            '好奇心求知欲': '好奇心', '爱好特长': '爱好特长', '审美修养': '艺术审美',
            '无效敏感': '无效'
        }
type_b_dict={list(data['属性'])[i]: list(set(res.sub('',list(data['标签'])[i]).split('/'))) for i in range(len(list(data['属性'])))}

def generate_label(type='实践能力'):
    for b in type_b_dict.get(type):
        yield Label(label_message=b)
if __name__ == '__main__':

    with grpc.insecure_channel('101.89.179.113:5000') as channel:
        stub= LabelTypeStub(channel)
        response = stub.Run_classifier(generate_label('好奇心求知欲'))
        for msg in response:
            print("recived message {message} sim_type {type}".format(
                message=msg.label_message,type=msg.type_class))

