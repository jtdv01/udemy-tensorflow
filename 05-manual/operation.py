class Operation():
    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []
        
        # For every node in the inputnodes
        # Append this operation to the output nodes
        for node in input_nodes:
            node.output_nodes.append(self)

        _default_graph.operations.append(self)

        def compute(self):
            pass

class add(Operation):
        
        def __init__(self, x, y):
            super().__init__([x,y])
        
        def compute(self, x_var, y_var):
            self.inputs = [x_var, y_var]
            return x_var + y_var

        
class multiply(Operation):
        
        def __init__(self, x, y):
            super().__init__([x,y])
        
        def compute(self, x_var, y_var):
            self.inputs = [x_var, y_var]
            return x_var * y_var

class matmul(Operation):
        
        def __init__(self, x, y):
            super().__init__([x,y])
        
        def compute(self, x_var, y_var):
            self.inputs = [x_var, y_var]
            # Assuming x_var is a np array
            return x_var.dot(y_var)

class Placeholder():
    """
    An empty node that needs a value to be
    probided to compute an output
    """
    def __init__(self):
        self.output_nodes = []
        _default_graph.placeholders.append(self)

class Variable():
    """
    Changeable parameters
        eg: weights of neural network
    """
    def __init__(self, inivial_value=None):
        self.value = initial_value
        self.output_nodes = []
        _default_graph.variables.append(self)

class Graph():
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
       
    def set_as_default(self):
        # Default graph is a global variable for other graph objects
        global _default_graph
        _default_graph = self

if __name__ == "__main__":

    """
    z = Ax + b
    A = 10
    b = 1
    
    z = 10x + 1
    """
    
    g = Graph()
    g.set_as_default()
    

    A = Variable(10)
    b = Variable(1)

    # To be provided later
    x = Placeholder()

    y = multiply(A, x)
    z = add(y, b)


