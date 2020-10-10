import argparse
import os
from relation import Papers
from graph import DrawGraph
from loader import SimpleLoader




def main(path):
    papers = [
        {'title':'Generative Adversarial Nets','arxivId':'1406.2661','label':'GAN'},
        {'title':'Conditional Generative Adversarial Nets','arxivId':'1411.1784','label':'cGAN'},
        {'title':'Conditional Image Synthesis With Auxiliary Classifier GANs','arxivId':'1610.09585','label':'ACGAN'},
        {'title':'Towards Biologically Plausible Deep Learning','arxivId':'1502.04156','label':'TBP'}
    ]
    sl = SimpleLoader(path)
    papers = sl()
    p = Papers(papers)
    rel =p.get_relations()
    d = DrawGraph(rel)
    d.draw()
    d.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='引用関係をグラフにする')    
    parser.add_argument('--input_path', default='' ,help='入力ファイルのパス')

    args = parser.parse_args()
    path = args.input_path
    if not path:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'input.csv')

    main(path)