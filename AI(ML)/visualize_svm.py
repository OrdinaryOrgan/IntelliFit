from re import X
from dataloader import data_loader
from sklearn.manifold import TSNE
import joblib
import numpy as np
import matplotlib.pyplot as plt


def visualize_svm_2d(path, fitnessman_list, fitnessman_height):

    x, y = data_loader(path, fitnessman_list, fitnessman_height)
    data_size =len(x)

    svm = joblib.load('test23n_svm.joblib')
    scaler = joblib.load('test23n_scaler.joblib')
    x = scaler.transform(x)
    sv = np.array(svm.support_vectors_)
    x = np.append(x, sv, axis=0)

    t_sne = TSNE(n_components=2, \
                 perplexity=200.0, \
                 early_exaggeration=12.0,\
                 learning_rate=200.0, \
                 n_iter=50000, \
                 n_iter_without_progress=300, \
                 min_grad_norm=1e-07, \
                 metric='euclidean', \
                 init='random', \
                 verbose=0, \
                 random_state=None, \
                 method='barnes_hut', \
                 angle=0.5)
    
    x = t_sne.fit_transform(x)

    xx = x[:data_size, 0]
    xy = x[:data_size, 1]

    plt.figure(1) 
    plt.plot(xx[y==1], xy[y==1], 'c.',  label='right')
    plt.plot(xx[y==0], xy[y==0], '.',  label='wrong') 

    xx = x[..., 0]
    xy = x[..., 1]

    plt.plot(xx[data_size:], xy[data_size:], 'r.', label='support vector')
    plt.legend()
    plt.savefig('figure/23n/visualized_svm_2d.jpg', dpi=400)
    plt.clf() # 清除图形


def visualize_svm_3d(path, fitnessman_list, fitnessman_height):

    x, y = data_loader(path, fitnessman_list, fitnessman_height)
    data_size =len(x)

    svm = joblib.load('test23n_svm.joblib')
    scaler = joblib.load('test23n_scaler.joblib')
    x = scaler.transform(x)
    sv = np.array(svm.support_vectors_)
    x = np.append(x, sv, axis=0)

    t_sne = TSNE(n_components=3, \
                 perplexity=200.0, \
                 early_exaggeration=12.0, \
                 learning_rate=200.0, \
                 n_iter=50000, \
                 n_iter_without_progress=300, \
                 min_grad_norm=1e-07, \
                 metric='euclidean', \
                 init='random', \
                 verbose=0, \
                 random_state=None, \
                 method='barnes_hut', \
                 angle=0.5)
    
    x = t_sne.fit_transform(x)

    xx = x[:data_size, 0]
    xy = x[:data_size, 1]
    xz = x[:data_size, 2]

    plt.figure(2)
    ax = plt.axes(projection='3d')  
    # 画3D散点图
    ax.plot3D(xx[y==1], xy[y==1], xz[y==1], 'c.',  label='right') 
    ax.plot3D(xx[y==0], xy[y==0], xz[y==0], '.',  label='wrong')

    xx = x[..., 0]
    xy = x[..., 1]
    xz = x[..., 2]

    ax.plot3D(xx[data_size:], xy[data_size:], xz[data_size:], 'r.', label='support vector')
    ax.set_title('cluster')
    ax.legend()
    plt.savefig('figure/23n/visualized_svm_3d.jpg',dpi=300)


path = './data/'
fitnessman_list = ['shuffled_combined_data_split1', 'shuffled_combined_data_split2', 'shuffled_combined_data_split3']
fitnessman_height = [170, 169, 171]

visualize_svm_2d(path, fitnessman_list, fitnessman_height)
visualize_svm_3d(path, fitnessman_list, fitnessman_height) 