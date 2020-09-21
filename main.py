import parser

from relation import Papers
from graph import DrawGraph




def main():
    papers = [
        {'title':'Generative Adversarial Nets','arxivId':'1406.2661','label':'GAN'},
        {'title':'Conditional Generative Adversarial Nets','arxivId':'1411.1784','label':'cGAN'},
        {'title':'Conditional Image Synthesis With Auxiliary Classifier GANs','arxivId':'1610.09585','label':'ACGAN'},
        {'title':'Towards Biologically Plausible Deep Learning','arxivId':'1502.04156','label':'TBP'}
    ]
    p = Papers(papers)
    rel =p.get_relations()
    d = DrawGraph(rel)
    d.draw()
    d.save()


if __name__ == '__main__':
    main()