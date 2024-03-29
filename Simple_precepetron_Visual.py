from sklearn import datasets
import numpy as np 

iris = datasets.load_iris()

x = iris.data[:,[2,3]]
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.30, random_state=42,stratify = y)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

xstd1 = sc.fit_transform(x_train)

from sklearn.linear_model import Perceptron

ppn = Perceptron(n_iter_no_change=40,eta0=0.1)

ppn.fit(xstd1,y_train)

xstd2 = sc.fit_transform(x_test)
ypred = ppn.predict(xstd2)

from sklearn.metrics import classification_report
print(classification_report(ypred,y_test))

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


def plot_decision(x,y,classifier,test_idx = None,resolution = 0.02):
    
    markers = ('s','x','o','^','v')
    colors = ('red','blue','lightgreen','gray','cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    
    x1min,x1max = x[:,0].min() -1,x[:,0].max() + 1
    x2min,x2max = x[:,1].min() -1,x[:,1].max() + 1
    
    xx1,xx2 = np.meshgrid(np.arange(x1min,x1max,resolution),
                          np.arange(x2min,x2max,resolution))
    
    z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    
    plt.contourf(xx1,xx2,z,alpha=0.3,cmap =cmap)
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=x[y ==cl,0],y= x[y==cl,1],alpha =0.8 ,c= colors[idx]
                   ,marker=markers[idx],label=cl,edgecolor='black')


xc = np.vstack((xstd1,xstd2))
yc= np.hstack((y_train,y_test))
plot_decision(x= xc,y=yc,classifier=ppn,test_idx=range(105,150))
plt.legend()


