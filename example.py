from pyDV.App import App
from sklearn.decomposition import PCA
import numpy as np

def r(data, canvas):
    d = np.array(data)
    pca = PCA(n_components=2)
    pca_d = pca.fit_transform(d)
    stdvar_d = np.apply_along_axis(np.std,0,pca_d)
    print('stdvar',stdvar_d)
    ax = np.array([[0,0],[stdvar_d[0],0],[0,stdvar_d[1]]])
    rax = pca.inverse_transform(ax)
    print('pca',rax[1] - rax[0],rax[2] - rax[0])
    canvas.create_line(rax[0,0],rax[0,1],rax[1][0],rax[1][1])
    canvas.create_line(rax[0,0],rax[0,1],rax[2][0],rax[2][1])

if __name__ == "__main__":
    App(r)