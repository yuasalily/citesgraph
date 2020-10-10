import arxiv
import requests
import time




class Papers:
    def __init__(self,papers=None,comp=None,preprocess=None):
        self.relations = {}
        self.papers = papers
        if preprocess:
            self.papers = preprocess(self.papers)
        self.comp = comp

    def get_references(self, title, arxivId, label):
        paper_info = requests.get('https://api.semanticscholar.org/v1/paper/arXiv:'+ arxivId).json()
        time.sleep(1)
        if self.comp:
            return self.comp(self.papers, paper_info)
        
        ref_list = []
        for ref in paper_info['references']:
            for paper in self.papers:
                if (ref['title'] == paper['title'] or ref['arxivId'] == paper['arxivId']):
                    ref_list.append(paper['label'])
        return ref_list


    def get_relations(self):
        if not self.papers:
            raise Exception('There is no paper')
        for paper in self.papers:
            self.relations[paper['label']] = self.get_references(**paper)
        return self.relations

    def main(self):
        return self.get_relations()

    def __call__(self,papers):
        self.papers = papers


    
if __name__ == '__main__':
    papers = [
        {'title':'Generative Adversarial Nets','arxivId':'1406.2661','label':'GAN'},
        {'title':'Conditional Generative Adversarial Nets','arxivId':'1411.1784','label':'cGAN'},
        {'title':'Conditional Image Synthesis With Auxiliary Classifier GANs','arxivId':'1610.09585','label':'ACGAN'},
        {'title':'Towards Biologically Plausible Deep Learning','arxivId':'1502.04156','label':'TBP'}
        ]
    p = Papers(papers)
    p.get_relations()