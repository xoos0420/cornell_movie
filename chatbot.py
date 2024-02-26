# Building a Chatbot with Deep NLP
import numpy as np
import tensorflow as tf
import re
import time

# 데이터셋 불러오기
lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

# 각 대사와 id 맵핑시키기
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]
