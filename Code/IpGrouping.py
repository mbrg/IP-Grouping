"""
IP Grouping Algorithm
"""

import numpy as np
from IpManipulation import *

# number of bits in IP binary representation
BINARY_SIZE = 32


def FindMinBinaryInterval(p1, p2):
    """
    Find minimal binary interval which covers p1, p2
    :param p1: IPv4 in decimal format
    :param p2: IPv4 in decimal format
    :return: IP range in astrix format
    """
    bit_diff = RangeBitDiff(p1, p2)
    msb_substring = IpDecimalToBinary(p1, BINARY_SIZE)
    if bit_diff!=0: msb_substring = msb_substring[:-bit_diff]
    return (msb_substring + '*'*BINARY_SIZE)[:BINARY_SIZE]


def GetCover(A,B,C, format='slash'):
    """
    Iterate backwards over FindMinCover matrices to print results
    A similar procedure as PrintCover, but with the small change of returning the results instead of printing them to screen
    :param format: wanted format for result. options=['astrix','slash']
    :return: the minimal cover found, as a list
    """
    if A[-1,-1]==np.inf:
        return  # failed
    else:
        cover = []
        i = A.shape[0]-1
        j = A.shape[1]-1
        while i>0:
            cover.append(C[i,j])
            if format=='slash': cover[-1] = GetSlashNotation(cover[-1], BINARY_SIZE)
            i = int(B[i,j])-1
            j = j-1
    return cover


def FindMinCover(points, L, S, format='slash'):
    """
    Find minimal binary interval cover which covers all points, under the constraints given by L and S
    :param points: collection of IPv4 IPs in string notation e.g. 10.0.0.1
    :param L: maximum number of binary intervals
    :param S: maximum length of a binary interval
    :param format: wanted format for result. options=['astrix','slash']
    :return: the minimal cover found, as a list
    """
    # preprocess to decimal IP format
    dec_points = sorted([IpStringToDecimal(p) for p in points])

    # define constants
    n = len(dec_points)

    # define matrices
    matrix_shape = (n+1, L+1)
    A = np.zeros(matrix_shape)
    B = np.zeros(matrix_shape)
    C = np.empty(matrix_shape, dtype=object)

    # Initiate A
    A[0,:] = np.zeros((1, L+1))
    A[1:,0] = np.inf

    for i in range(1, n+1):
        for j in range(1, L+1):

            # s <- argmin_{k<=i} s.t |FindMinBinaryInterval(p_k, p_i)| <= S
            s = i
            for k in range(1,i+1):
                I = FindMinBinaryInterval(dec_points[k-1], dec_points[i-1])
                if BinaryIntervalLen(I) <= S:
                    s = k
                    break

            A[i,j] = np.inf
            for k in range(s, i+1):
                I = FindMinBinaryInterval(dec_points[k-1], dec_points[i-1])
                x = BinaryIntervalLen(I) - (i - k + 1)
                if A[i,j] > x + A[k-1,j-1]:
                    # update for i points, j intervals
                    A[i,j] = x + A[k-1,j-1]  # min noise
                    B[i,j] = k  # first wanted IP in I
                    C[i,j] = I

    cover = GetCover(A, B, C, format)  # iterate backwards to print results
    return cover


def example(L=4, S=8, format='slash'):
    """
    A short example for points ('0.0.0.3','0.0.0.5','0.0.0.6','0.0.0.7')
    Prints out found cover
    :param L: maximum number of binary intervals
    :param S: maximum length of a binary interval
    :param format: wanted format for result. options=['astrix','slash']
    """
    global BINARY_SIZE
    BINARY_SIZE = 3
    points = ('10.0.0.3','10.0.0.5','10.0.0.6','10.0.0.7')
    cover = FindMinCover(points, L, S, format)
    for i in cover:
        print(i)

