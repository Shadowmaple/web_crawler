import jieba
import numpy as np
import requests
from PIL import Image
from wordcloud import WordCloud


def generate_wordcloud():
    f = open("data.txt", "r", encoding='utf-8').read()

    # WordCloud（按英文习惯）以空格分词，中文不用空格所以不能正确对中文进行分词，因此要手动空格分隔
    jieba_txt = ' '.join(jieba.cut(f))
    background_image = np.array(Image.open("bgImage.jpg"))

    # 默认字体不支中文，需要指定要使用的中文字体路径
    wordcloud = WordCloud(
        font_path = "SourceHanSansSC-Normal.otf",
        background_color = 'white',
        mask = background_image,
    )
    wordcloud.generate(jieba_txt)
    wordcloud.to_file('cloud.png')

    # 打开云词图
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()


if __name__ == '__main__':
    generate_wordcloud()
    print("OK")
