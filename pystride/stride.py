import subprocess


def stride(pdbpath):
    """Perform STRIDE analysis

    Parameters
    ----------
    pdbpath : str
      path to the pdb file to analyse

    Returns
    -------
    """
    p = subprocess.Popen(['stride', pdbpath],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    return stdout
