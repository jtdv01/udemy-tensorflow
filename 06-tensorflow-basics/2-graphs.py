import tensorflow as tf

n1 = tf.constant(1)
n2 = tf.constant(2)

n3 = n1 + n2

with tf.Session() as sess:
    res = sess.run(n3)

print(n3)

print("Default graph:")
print(tf.get_default_graph())

# Another graph
g1 = tf.get_default_graph()
print("Another graph")
g2 = tf.Graph()

# Set g2 as default
with g2.as_default():
    print(g2 is tf.get_default_graph())


