import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import  load_digits
from sklearn.model_selection import train_test_split as tts
import numpy as np

class model:
    def __init__(self, verbose):
        self.loaded = False
        self.verbose = False
        self.train_data = None 
        self.test_data = None 
        self.trained_model = None
        # call key methods
        self.digits = load_digits()
        self.data_split()
        self.train_model()

    def data_split(self):
        x_train,x_test, y_train, y_test = tts(self.digits.data,self.digits.target,test_size = 0.3)
        self.train_data = {'data':x_train,'targets':y_train}
        self.test_data = {'data':x_test,'targets':y_test}
        if self.verbose:
            print("Data loaded!")
    
    def train_model(self):
        rfc = RandomForestClassifier()
        rfc.fit(self.train_data['data'],self.train_data['targets'])
        self.trained_model = rfc
        self.loaded =True
        if self.verbose:
            print("Model trained!")
            del self.digits
            del self.train_data

    def inference(self):
        rand_sample = np.random.randint(len(self.test_data['data']))
        if self.loaded:
            class_name_val = self.trained_model.predict(self.test_data['data'][rand_sample].reshape(1, -1))[0]
            probability_val = self.trained_model.predict_proba(self.test_data['data'][rand_sample].reshape(1, -1))[0].max()
            real = self.test_data['targets'][rand_sample]
            return [class_name_val, probability_val, real]
        else:
            return ['model not trained', 'model not trained', 'model not trained']
        
