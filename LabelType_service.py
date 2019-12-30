from concurrent import futures
import time
import grpc
from label_classifier_pb2 import Label, Label_class
from label_classifier_pb2_grpc import LabelTypeServicer, add_LabelTypeServicer_to_server
from run_classifier import BertSim
import tensorflow as tf
#进入bert标签预测模式
sim = BertSim()
sim.set_mode(tf.estimator.ModeKeys.PREDICT)

class LabelType(LabelTypeServicer):
    def __init__(self):
        # 原始type总类别和同义词
        self.Synonyms_type = {
            '实践能力': '实践', '行为习惯': '行为习惯', '人格品质': '人格品质',
            '人际沟通': '沟通', '体育': '运动', '理想信念': '理想信念',
            '课业质量': '学业', '知识技能': '知识掌握', '创新意识': '创新思维',
            '好奇心求知欲': '好奇心', '爱好特长': '爱好特长', '审美修养': '艺术审美',
            '无效敏感': '无效'
        }

    def Run_classifier(self, request_iterator, context):
        for label in request_iterator:
            sim_type=self.similarity(label.label_message)
            yield  Label_class(label_message=label.label_message,type_class=sim_type[0],similarity=sim_type[1])


    # 计算问题和问题库问题相似度以及相似句子
    def similarity(self,sentence):
        sim_dict={}
        for s,v in self.Synonyms_type.items():
            sims1=sim.predict_one(sentence,s)
            sims2 = sim.predict_one(sentence, v)
            if sims1[0][1]>sims2[0][1]:
                sim_dict[s]=sims1[0][1]
            else:
                sim_dict[s] = sims2[0][1]
        sim_words = sorted(sim_dict.items(), key=lambda asd: asd[1], reverse=True)[0]
        return sim_words

    #自定义很多规则于清楚无效信息
    def clean_label(self,label):

        return '无效敏感'
    # grpc开启服务
    def serve(self, addr):
        print("Starting server at {}...".format(addr))
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
        add_LabelTypeServicer_to_server(self, server)
        server.add_insecure_port(addr)
        server.start()
        # 一直持续下去
        try:
            while True:
                time.sleep(60 * 60 * 24)  # one day in seconds
        except KeyboardInterrupt:
            server.stop(0)
        # 等待直到接收一个信号
        # try:
        #     signal.pause()
        # except KeyboardInterrupt:
        #     pass

def main():
    service=LabelType()
    #时刻监控更新
    service.serve("{}:{}".format('0.0.0.0', 5000))

if __name__ == "__main__":
    main()