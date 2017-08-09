from collections import namedtuple
import subprocess


def stride(pdbpath):
    """Perform STRIDE analysis

    Parameters
    ----------
    pdbpath : str
      path to the pdb file to analyse

    Returns
    -------
    output : str
      The raw stdout from stride as a string
    """
    p = subprocess.Popen(['stride', pdbpath],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    return stdout


Assignment = namedtuple(
    'Assignment',
    ['resname', 'chainid', 'resid', 'resnum', 'structure_code',
     'structure_name', 'phi', 'psi', 'area']
)


def parse_assignment(line):
    """Parse an ASG line from STRIDE

    Returns
    -------
    Assignment namedtuple
    """
    return Assignment(
        line[5:8],
        line[9],
        int(line[11:15]),
        int(line[16:20]),
        line[24],
        line[26:39].strip(),
        float(line[42:49]),
        float(line[52:59]),
        float(line[64:69]),
    )


def parse_assignments(output):
    """Parse the assignments from the raw output of STRIDE

    Each item in the returned list is a namedtuple with the following fields:
      resname
      chainid
      resid
      resnum
      structure_code
      structure_name
      phi
      psi
      area

    Parameters
    ----------
    output : str
      the raw output from pystride.stride

    Returns
    -------
    assignments : list of Assignment
      each item in the list represents a single entry, as described above
    """
    return [parse_assignment(line)
            for line in output.split('\n')
            if line.startswith('ASG')]
