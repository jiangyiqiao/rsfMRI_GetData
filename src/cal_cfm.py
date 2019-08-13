tn,fp,fn,tp = 73,11,24,47

test_acc = 100 * (tn + tp) / (tn + fp + fn + tp)
sensitivity = 100 * tp / (tp + fn)  # 敏感度
specificity = 100 * tn / (tn + fp)  # 特异性
f_score = 100 * 2 * tp / (2 * tp + fp + fn)


print("Test ACC,SEN,SPE,Fscore,AUC:\n{:.2f}% {:.2f}% {:.2f}% {:.2f}% ".format(test_acc,sensitivity,specificity, f_score))
