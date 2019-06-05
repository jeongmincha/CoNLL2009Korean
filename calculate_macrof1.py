from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
from sklearn.metrics import recall_score, precision_score, f1_score

true_path='srl.test.korean.conll'
pred_path='srl-korean.out'

true_data = open(true_path, 'rt', encoding='utf8').readlines()
pred_data = open(pred_path, 'rt', encoding='utf8').readlines()

y_pred = []
y_true = []

x = []

for idx in range(len(pred_data)):
    true_line = true_data[idx].split()
    pred_line = pred_data[idx].split()
    
    if len(true_line) > 0:
        cur_true = []
        cur_pred = []
        for e in true_line[-3:]:
            x.append(e)
            if e in ['ARG0', 'ARG1', 'ARG2', 'ARG3']:
                cur_true.append(e)
            else:
                cur_true.append('_')
        for e in pred_line[-3:]:
            x.append(e)
            if e in ['ARG0', 'ARG1', 'ARG2', 'ARG3']:
                cur_pred.append(e)
            else:
                cur_pred.append('_')
        y_true.append(cur_true)
        y_pred.append(cur_pred)

mlb = MultiLabelBinarizer()
mlb.fit(y_true)
mlb.fit(y_pred)

# (None, 'micro', 'macro', 'weighted', 'samples')
average='macro'
r = recall_score(mlb.transform(y_true), mlb.transform(y_pred), average=average)
p = precision_score(mlb.transform(y_true), mlb.transform(y_pred), average=average)
f1 = f1_score(mlb.transform(y_true), mlb.transform(y_pred), average=average)

print("Recall: {}".format(r))
print("Precision: {}".format(p))
print("Macro F1 Score: {}".format(f1))