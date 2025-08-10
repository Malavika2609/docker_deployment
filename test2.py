import sklearn
import sklearn.tree

print(sklearn.__version__)
print(sklearn.__file__)
print(sklearn.tree.__file__)
import sklearn
import inspect
from sklearn.tree import DecisionTreeClassifier

print(sklearn.__version__)  # should be 1.5.2
print(hasattr(DecisionTreeClassifier(), "monotonic_cst"))  # should be True

