import math

# corners = [
#     [0.5, 0.5, 0.5],
#     [0.5, -0.5, 0.5],
#     [-0.5, 0.5, 0.5],
#     [-0.5, -0.5, 0.5],
#     [-0.5, -0.5, -0.5],
#     [0.5, 0.5, -0.5],
#     [-0.5, 0.5, -0.5],
#     [0.5, -0.5, -0.5],
# ]
#
#
# def area(R1, R2=None, AREA=0):
#     from scipy.spatial import ConvexHull
#     import numpy as np
#     points = [c[:] for c in corners]
#     if R2 is not None:
#         points = [np.dot(R1, c) for c in points]
#         points = [np.dot(R2, c) for c in points]
#     else:
#         points = [np.dot(R1, c) for c in points]
#     points = [[p[0], p[2]] for p in points]
#     hull = ConvexHull(points)
#     print("RESULT", round(hull.volume - AREA, 10), AREA)


def dot(V, W):
    return sum([x * y for x, y in zip(V, W)])


def mdot(M, V):
    return [dot(m, V) for m in M]


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = [
        a / math.sqrt(dot(axis, axis)) for a in axis
    ]
    a = math.cos(theta / 2.0)
    b, c, d = [-a * math.sin(theta / 2.0) for a in axis]
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return [[aa + bb - cc - dd, 2 * (bc + ad),
             2 * (bd - ac)], [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
            [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]]


def middle(f, l, h):
    m = (l + h) / 2.0
    fm = f(m)
    if fm > 1.e-11:
        return middle(f, l, m)
    if fm < -1.e-11:
        return middle(f, m, h)
    return m


s2 = math.sqrt(2)
s3 = math.sqrt(3)
t = int(input())
for i in range(1, t + 1):
    AREA = float(input())
    print("Case #{}:".format(i))
    centers = [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]
    if AREA <= s2:
        theta = math.acos(AREA / s2) - math.acos(1 / s2)
        axis = (0.0, 0.0, 1.0)
        R = rotation_matrix(axis, theta)
        for c in centers:
            print(" ".join(map(str, mdot(R, c))))
        # area(R, None, AREA)
        continue

    theta1 = math.acos(1 / s2)
    axis1 = (0.0, 0.0, 1.0)
    R1 = rotation_matrix(axis1, theta1)

    def f(x):
        return AREA / s2 - math.cos(x) - math.cos(x + math.pi / 2) / s2

    theta2 = middle(f, 2 * math.atan(s2 - s3), math.atan(s2))
    axis2 = (1.0, 0.0, 0.0)
    R2 = rotation_matrix(axis2, -theta2)
    for c in centers:
        print(" ".join(map(str, mdot(R2, mdot(R1, c)))))
    # area(R1, R2, AREA)
