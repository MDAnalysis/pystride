"""Tests for python bindings to STRIDE"""

import os
import pytest
import pystride
from six.moves import zip

HERE = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def ADK():
    return os.path.join(HERE, 'adk_oplsaa.pdb')


@pytest.fixture
def REF_ADK():
    with open(os.path.join(HERE, 'adk.out'), 'r') as inf:
        data = inf.read()
    return data


def test_stride(ADK, REF_ADK):
    result = pystride.stride(ADK)
    for a, b in zip(result.split('\n'), REF_ADK.split('\n')):
        if a.startswith('CHN'):
            continue
        assert a == b

def test_parse_assignments(REF_ADK):
    assignments = pystride.parse_assignments(REF_ADK)

    asg = assignments[1]
    assert asg.resname == 'ARG'
    assert asg.resid == 2
    assert asg.resnum == 2
    assert asg.structure_code == 'E'
    assert asg.structure_name == 'Strand'
    assert asg.phi == -124.70
    assert asg.psi == 94.79
    assert asg.area == 60.7
