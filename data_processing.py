import os
import tarfile
import urllib.request

URL_IMGS = 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz'
URL_LBLS = 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat'

def download_flower_data(img_url, lbl_url):
    #
    if not os.path.exists('data/flower_data'):
        try:
            path = os.getcwd() + '/data/flower_data'
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

    if not os.path.isfile('data/flower_data/102flowers.tgz'):
        print("Downloading flowers_102 images and labels...")
        urllib.request.urlretrieve(img_url, 'data/flower_data/102flowers.tgz')
        urllib.request.urlretrieve(lbl_url, 'data/flower_data/imagelabels.mat')
        print('Finished Downloading')
        print('-'*50)
    if not os.path.exists('data/flower_data/images'):
        try:
            print('Extracting Images ...')
            path = os.getcwd() + '/data/flower_data/'
            tf = tarfile.open(path+'102flowers.tgz')
            tf.extractall(path)
            os.rename(path+'/jpg', path+'images')
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)



if __name__ == "__main__":
    download_flower_data(URL_IMGS, URL_LBLS)

