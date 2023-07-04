import pandas as pd
import numpy as np
import Landslide_prediction_model as lp
from sklearn.ensemble import GradientBoostingClassifier
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn import ensemble

# A csv file having realtime data for a particular 
# geographical location having specified parameters is required here
realtime_data = pd.read_csv('Realtime_data.csv')

y = lp.pred(realtime_data)

def alert():
    for label in y:
        if( label == 1 ):
            return "Alert! Possibility of a landslide"
