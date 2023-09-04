from dataloader import data_loader
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import sklearn
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
import seaborn as sns

path = 'data/'
train_fitnessman_list = ['shuffled_combined_data_split1', 'shuffled_combined_data_split2']
train_fitnessman_height = [170, 169]
# train_x, test_x, train_y, test_y = LoadData(path, test_person_list, test_person_height)
train_x, train_y = data_loader(path, train_fitnessman_list, train_fitnessman_height)

scaler = PCA(n_components=0.95)#MinMaxScaler(feature_range=(0, 1))
scaler.fit(train_x)
train_x = scaler.transform(train_x)
print(scaler.explained_variance_ratio_)

rbf_svm = SVC(kernel='rbf')
rbf_svm.fit(train_x, train_y)

test_fitnessman_list = ['shuffled_combined_data_split3']
test_fitnessman_height = [171]
test_x, test_y = data_loader(path, test_fitnessman_list, test_fitnessman_height)

test_x = scaler.transform(test_x)
y = rbf_svm.predict(test_x)
print(rbf_svm.score(test_x, test_y))
print(sklearn.metrics.f1_score(test_y, y))

joblib.dump(rbf_svm, 'test23n_svm.joblib')
joblib.dump(scaler, 'test23n_scaler.joblib')

# Draw ROC_AUC curve
fpr, tpr, thresholds = roc_curve(test_y, rbf_svm.decision_function(test_x))
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('figure/23n/ROC.jpg',dpi=400)
plt.clf() # 清除图形

#Draw P-R curve
precision, recall, thresholds = precision_recall_curve(test_y, rbf_svm.decision_function(test_x))

plt.figure()
plt.plot(recall, precision, color='darkorange', lw=2) 
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.savefig('figure/23n/P-R.jpg',dpi=400)
plt.clf() # 清除图形

#Draw confusion matrix
cm = confusion_matrix(test_y, y)
ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax, cmap='Blues')

ax.set_xlabel('Predicted')
ax.set_ylabel('True')
ax.set_title('Confusion Matrix')
plt.savefig('figure/23n/confusion_matrix.jpg',dpi=400)
plt.clf() # 清除图形