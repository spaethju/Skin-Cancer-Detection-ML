from sklearn.metrics import roc_curve, auc, roc_auc_score
import matplotlib.pyplot as plt

def plotROC(pred_labels, test_labels, save_path = None):
    """
    Plots roc curve
    :param pred_labels: List of predicted labels
    :param test_labels: List of true labels
    :return: ROC graph
    """
    roc_auc = roc_auc_score(test_labels, pred_labels)
    plt.title('Receiver Operating Characteristic')
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.2])
    plt.ylim([-0.1, 1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')

    if not save_path:
        plt.show()
    else:
        plt.savefig(save_path)


def getANNResults(pred_labels, test_labels):
    """
    Get number of maligne and benigne predicted labels
    :param labels: Labels
    :return: maligne, benigne : Number of maligne and benigne prediction
    """
    maligne_pred = 0
    benigne_pred = 0
    maligne_test = 0
    benigne_test = 0
    for pred in pred_labels:
        if pred == 1:
            maligne_pred+=1
        else:
            benigne_pred+=1
    for label in test_labels:
        if label == 1:
            maligne_test+=1
        else:
            benigne_test+=1
    return maligne_pred, benigne_pred, maligne_test, benigne_test

def getPositiveNegatves(pred_labels, test_labels):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(0, len(pred_labels)):
        if pred_labels[i] == 1 and test_labels[i] == 1:
            TP = TP+1
        elif pred_labels[i] == 1 and test_labels[i] == 0:
            FP = FP+1
        elif pred_labels[i] == 0 and test_labels[i] == 0:
            TN = TN+1
        elif pred_labels[i] == 0 and test_labels[i] == 1:
            FN = FN+1
        else:
            print("ERROR")
    print("TP: ", TP," FP: ",FP," TN: ",TN," FN: ",FN)




def getAUC(pred_labels, test_labels):
    """
    Compute AUC of prediction
    :param pred_labels:
    :param test_labels:
    :return: roc_auc - AUC of prediction
    """
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = roc_auc_score(test_labels, pred_labels)
    return roc_auc


if __name__ == '__main__':
    pred = []
    label = []

    print("ANN predicted %s of %s maligne and %s of %s benigne. AUC = %s" % (
    getANNResults(pred, label)[0], getANNResults(pred, label)[2], getANNResults(pred,label)[1], getANNResults(pred,label)[3], getAUC(pred, label)))
    plotROC(pred, label)
    getPositiveNegatves(pred, label)


