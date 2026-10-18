from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Aaliyah:
    def __init__(self, objectif):
        
        self.model=DecisionTreeClassifier()
        self.objectif=objectif
        
    def goal(self):
        return self.objectif
        
    def train(self, X, y):
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            self.model.fit(X_train,y_train)
            return f"{(100-accuracy_score(y_test, y_pred=self.model.predict(X_test))*100):.1f}%"
        except Exception as e0:
            return f"Erreur : {e0}"
  
    def answer_to(self,truc):
        try:
            return self.model.predict(truc)[0]
        except Exception as something:
            try:
                answer_to_première_erreur=something
                return self.model.predict([truc])[0]
            except Exception as something1:
                return f"Erreur : {answer_to_première_erreur}"
