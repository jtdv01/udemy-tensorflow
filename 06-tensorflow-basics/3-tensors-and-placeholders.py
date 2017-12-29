import tensorflow as tf

# Variables hold weights
# Placeholders are officially empty
#   data inputs
#   they need a declared expected data type

sess = tf.InteractiveSession()

my_tf = tf.random_uniform((4,4), 0, 1)

my_var = tf.Variable(my_tf)

init = tf.global_variables_initializer()

sess.run(init)


