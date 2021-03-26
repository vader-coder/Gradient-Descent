#this function is a polynomial
class function:
    #should be lists of equal length
    def __init__(self, coefficients, exponets):
        if (len(coefficients) != len(exponets) or len(coefficients) == 0):
            print("ERROR: make sure your parameters aren't empty")
            return
        self.coefficients = coefficients
        self.exponets = exponets

    def copy(self):
        return function(self.coefficients.copy(), self.exponets.copy())

    def evaluate(self, indexable):
        counter = 0
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                counter += (self.coefficients[i]*(indexable[i]**self.exponets[i]))
        return counter
    
    #gradient outputs a vector, so we cannot just evaluate it as a real-valued function
    def gradient(self, returnCopyOfGradient=False):
        if not(returnCopyOfGradient):# modify existing funciton
            for i in range(len(self.exponets)):#iterative polynomial rule.
                if self.coefficients[i] != 0:
                    self.coefficients[i] *= self.exponets[i]
                    self.exponets[i] -= 1
        else:#copy function and create the gradient.
            gradient = self.copy()
            gradient.gradient(False)
            gradient = Gradient(gradient.coefficients, gradient.exponets)
            return gradient

#gradient is different from function because it returns
#a vector when you evaluate it.
class Gradient(function):
    def evaluate(self, indexable):
        ans = []
        for i in range(len(self.exponets)):
            if self.coefficients[i] != 0:
                ans.append(self.coefficients[i]
                            * (indexable[i]**self.exponets[i]))
            else:
                ans.append(0)
        return ans