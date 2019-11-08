

"""
NDArray utils
"""
import mxnet as mx
import numpy as np


def top_probability(data, labels, top=5):
    """
    Get top probability prediction from NDArray.

    :param data: NDArray
        Data to be predicted
    :param labels: List
        List of class labels
    :param top:
    :return: List
        List of probability: class pairs in sorted order
    """
    dim = len(data.shape)
    if dim > 2:
        data = mx.nd.array(
            np.squeeze(data.asnumpy(), axis=tuple(range(dim)[2:])))
    sorted_prob = mx.nd.argsort(data[0], is_ascend=False)
    # pylint: disable=deprecated-lambda
    top_prob = map(lambda x: int(x.asscalar()), sorted_prob[0:top])
    return [{'probability': float(data[0, i].asscalar()), 'class': labels[i]}
            for i in top_prob]
