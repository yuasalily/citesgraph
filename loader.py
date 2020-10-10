
import os

def read_file(file_path):
    with open(file_path) as f:
        f.readline()
        for line in f:
            yield line.rstrip('\n')

class SimpleLoader:
    def __init__(self,file_path):
        self.file_path = file_path

    def __call__(self):
        papers = []
        for paper in read_file(self.file_path):
            title, arxivId, label = paper.split(',')
            if not label.strip():
                label = self.labeler(title)
            papers.append({
                'title': title,
                'arxivId': arxivId,
                'label': label
            })
        return papers

    @staticmethod
    def labeler(title):
        return "".join(map(lambda x:x.strip()[0], title.split()))


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'input.csv')
    sl = SimpleLoader(path)
    print(sl())
    