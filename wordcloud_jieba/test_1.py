import jieba
from wordcloud import WordCloud
import os

cur_path = os.path.dirname(__file__)

def chinese_jieba(txt):
    wordlist_jieba = jieba.cut(txt) # 将文本分割，返回列表
    print(wordlist_jieba, list(wordlist_jieba))
    txt_jieba = " ".join(wordlist_jieba) # 将列表拼接为以空格为间断的字符串
    return txt_jieba

stopwords = {'这些':0, '那些':0, '因为':0, '所以':0} # 噪声词

# with open(os.path.join(cur_path, '择天记.txt')) as fp:
#     txt = fp.read()
#     txt = chinese_jieba(txt)
#     print(txt)
#     wordcloud = WordCloud(#font_path = 'FZLTXIHK.TTF', # 字体
#                           background_color = 'black', # 背景色
#                           max_words = 30, # 最大显示单词数
#                           max_font_size = 60, # 频率最大单词字体大小
#                           stopwords = stopwords # 过滤噪声词
#                         ).generate(txt)
#     image = wordcloud.to_image()
#     image.show()

chinese_jieba('你好，我是谁')