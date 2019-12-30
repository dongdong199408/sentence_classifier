import os
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

tem_path=os.getcwd()
file_path = os.path.join(os.getcwd(),'model')
model_dir = os.path.join(file_path, 'chinese_L-12_H-768_A-12/')
config_name = os.path.join(model_dir, 'bert_config.json')
ckpt_name = os.path.join(model_dir, 'bert_model.ckpt')
output_dir = os.path.join(tem_path, 'tmp/result/')
output_dir_sim=os.path.join(tem_path, 'sim_graph/')
vocab_file = os.path.join(model_dir, 'vocab.txt')
data_dir = os.path.join(tem_path, 'data/')

num_train_epochs = 10
batch_size = 64
learning_rate = 0.00005

# gpu使用率
gpu_memory_fraction = 1.0

# 默认取倒数第二层的输出值作为句向量
layer_indexes = [-2]

# 序列的最大长度，单文本建议把该值调小，双文本double
max_seq_len = 64
T_max_seq_len = 88
