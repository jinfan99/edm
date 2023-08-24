from dataset_tool import open_cifar100, open_cifar10

PATH_100 = "/home/ubuntu/edm/downloads/cifar-100-python.tar.gz"
PATH_10 = "/home/ubuntu/edm/downloads/cifar10/cifar-10-python.tar.gz"

def gen_dict(data_iter):
    data_dict = {}
    for data in data_iter:
        if data['label'] not in data_dict:
            data_dict[data['label']] = []
        
        data_dict[data['label']].append(data['img'])
        
    return data_dict
    
def main():
    c100 = open_cifar100(PATH_100, max_images=50000)[1]
    c10 = open_cifar10(PATH_10, max_images=50000)[1]
    c10_dict = gen_dict(c10)
    c100_dict = gen_dict(c100)
    
    for i in c1
    
    