import numpy as np

class perceptron:
    def __init__(self, pos, neg):
        self.pos = pos
        self.neg = neg
        self.num_pos = pos.shape[0]
        self.num_neg = neg.shape[0]
        self.m = pos.shape[1] # pos is a n x m matrix. Each row is a different sample.
        self.w = np.random.rand(1, self.m) # make w a row vector for easy adding

    def adjust_pos(self):
        post_dot = np.dot(self.w, self.pos)
        for i in range(self.num_pos):
            if pos_dot[i] < 0:
                self.w = np.add(self.w, self.pos[i])
                return False
        return True

    def adjust_neg(self):
        neg_dot = np.dot(self.w, self.neg)
        for i in range(self.num_neg)
            if neg_dot[i] >= 0:
                self.w = np.subtract(self.w, self.pos[i])
                return False
        return True

    def train(self):
        while(not adjust_pos() or not adjust_neg()):
            pass

    def classify(self, datum):
        return np.dot(self.w, datum) >= 0

            