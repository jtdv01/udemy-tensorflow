import tensorflow as tf

print(tf.__version__)


# Constants
hello = tf.constant("hello")
world = tf.constant("world")

a = tf.constant(10)
b = tf.constant(20)

# Sessions
with tf.Session() as sess:
    res1 = sess.run(hello + world)
    res2 = sess.run(a+b)
    print(res1)
    print(res2)

# Simples
fill_mat = tf.fill((4,4), 10)
myzeros = tf.zeros((4,4))
myones = tf.ones((4,4))

myrandn = tf.random_normal((4,4), mean= 0, stddev=1.0)
myrandu = tf.random_uniform((4,4), minval=0, maxval=1)

# interactive session
sess = tf.InteractiveSession()
my_ops = [fill_mat, myzeros, myones, myrandn, myrandu]
for op in my_ops:
    res = sess.run(op)
    # or op.eval()
    print(res)

# Tensors are a fancy word for n dimension arrays
# a: 2x2
a = tf.constant([
    [1,2],
    [3,4]
])
print(a.get_shape())

# b: 2x1
b = tf.constant([[10], [100]])
print(b.get_shape())

res = tf.matmul(a,b)
print(sess.run(res))
