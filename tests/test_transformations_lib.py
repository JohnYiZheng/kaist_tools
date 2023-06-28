import random
import math

import numpy as np
import transformations as tf


alpha, beta, gamma = 0.123, -1.234, 2.345
origin, xaxis, yaxis, zaxis = (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)
I = tf.identity_matrix()
Rx = tf.rotation_matrix(alpha, xaxis)
Ry = tf.rotation_matrix(beta, yaxis)
Rz = tf.rotation_matrix(gamma, zaxis)
R = tf.concatenate_matrices(Rx, Ry, Rz)
euler = tf.euler_from_matrix(R, 'rxyz')
print(np.allclose([alpha, beta, gamma], euler))

Re = tf.euler_matrix(alpha, beta, gamma, 'rxyz')
print(tf.is_same_transform(R, Re))

al, be, ga = tf.euler_from_matrix(Re, 'rxyz')
print(tf.is_same_transform(Re, tf.euler_matrix(al, be, ga, 'rxyz')))

# Quaternions ix+jy+kz+w are represented as [x, y, z, w].
qx = tf.quaternion_about_axis(alpha, xaxis)
qy = tf.quaternion_about_axis(beta, yaxis)
qz = tf.quaternion_about_axis(gamma, zaxis)
q = tf.quaternion_multiply(qx, qy)
q = tf.quaternion_multiply(q, qz)
Rq = tf.quaternion_matrix(q)
print(tf.is_same_transform(R, Rq))

S = tf.scale_matrix(1.23, origin)
T = tf.translation_matrix((1, 2, 3))
Z = tf.shear_matrix(beta, xaxis, origin, zaxis)
R = tf.random_rotation_matrix(np.random.rand(3))
M = tf.concatenate_matrices(T, R, Z, S)
scale, shear, angles, trans, persp = tf.decompose_matrix(M)
print(np.allclose(scale, 1.23))

angle = (random.random() - 0.5) * (2*math.pi)
direc = np.random.random(3) - 0.5
point = np.random.random(3) - 0.5
R0 = tf.rotation_matrix(angle, direc, point)
angle, direc, point = tf.rotation_from_matrix(R0)
R1 = tf.rotation_matrix(angle, direc, point)
print(tf.is_same_transform(R0, R1))

# compose matrix
translation = np.array([1.0, 2.0, 3.0])
translation_matrix = tf.translation_matrix(translation)
rotation_matrix = Re
transformation_matrix = tf.concatenate_matrices(translation_matrix, rotation_matrix)
print("rotation matrix:\n", rotation_matrix)
print("translation matrix:\n", translation_matrix)
print("final transformation:\n", transformation_matrix)