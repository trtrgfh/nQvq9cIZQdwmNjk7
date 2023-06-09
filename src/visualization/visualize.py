import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from predict_model import *
from make_dataset import *

# Plot confusion matrix for training
cm = confusion_matrix(y_train, pred_y)
disp_cm = ConfusionMatrixDisplay(confusion_matrix=cm)
disp_cm.plot()
plt.title("Confusion Matrix for Training set")
plt.savefig('figure1.png', bbox_inches='tight')
plt.show()

# Plot confusion matrix for testing
cm_test = confusion_matrix(y_test, pred_y_test)
disp_cm_test = ConfusionMatrixDisplay(confusion_matrix=cm_test)
disp_cm_test.plot()
plt.title("Confusion Matrix for Testing set")
plt.savefig('figure2.png', bbox_inches='tight')
plt.show()

im_features = model.feature_importances_
plt.bar(range(len(im_features)), im_features)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importances")
plt.xticks(range(len(im_features)), ["X1", "X2", "X3", "X4", "X5", "X6"])
plt.savefig('figure3.png', bbox_inches='tight')
plt.show()
