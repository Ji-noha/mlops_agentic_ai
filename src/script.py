from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

#print(len(cancer.feature_names))
#print(cancer.feature_names)

#print(cancer.target_names)

print(cancer.data[0])