import numpy as np

from .functions import moving_average


def test_moving_average():
    np.testing.assert_allclose(
        moving_average(np.ones(10) * 1.000000001, 4)[2:-2],
        1)
