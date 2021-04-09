import numpy as np

def bn(x):
    eps = 1e-5
    weight = 1
    bias = 0

    batch_size, channels, height, width = x.shape()
    numel = batch_size* height*width
    x = x.reshape(channels, numel)

    sum = x.sum(1)
    mean = sum / numel

    var = (x-mean).pow(2).sum(1) / numel

    y = (x-mean) / (var+eps).pow(0.5)

    y = weight*y+bias
    y = y.reshape(batch_size, channels, height, width)
    return y
