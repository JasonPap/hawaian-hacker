from sklearn import svm
from Password import Password


class PasswordClassifier:
    def __init__(self):
        self.clf = svm.OneClassSVM(kernel='rbf', gamma=0.1, nu=0.35)

    def train(self, TrainingFile):
        training_data = []
        with open(TrainingFile) as inputFile:
            for word in inputFile:
                p = Password(word)
                p.analyze_frequencies()
                training_data.append(p.letter_frequencies.values())

        # print training_data
        self.clf.fit(training_data)

    def predict(self, guess):
        p = Password(guess)
        p.analyze_frequencies()
        if self.clf.decision_function([p.letter_frequencies.values()]) + 400 > 0:
            return True
        else:
            return False
        # print p.letter_frequencies.values()
        # print guess
        # print self.clf.predict([p.letter_frequencies.values()])
        # print self.clf.decision_function([p.letter_frequencies.values()])
