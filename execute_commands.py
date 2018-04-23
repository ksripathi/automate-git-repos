import subprocess

__all__ = ['execute_command']

# Backporting check_output from 2.7 to 2.6
if "check_output" not in dir(subprocess):
    def f(*popenargs, **kwargs):
        if 'stdout' in kwargs:
            raise ValueError(
                'stdout argument not allowed, it will be overridden'
            )
        process = subprocess.Popen(stdout=subprocess.PIPE,
                                   *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise subprocess.CalledProcessError(retcode, cmd)
        return output
    subprocess.check_output = f


def execute_command(cmd):
    return_code = -1
    output = None
    try:
        output = subprocess.check_output(cmd, shell=True)
        return_code = 0
    except subprocess.CalledProcessError as cpe:
        raise cpe
    except OSError as ose:
        raise ose

    return (return_code, output)


if __name__ == '__main__':
    '''
    cmd = "git clone " +\
        "https://github.com/Virtual-Labs/computer-programming-iiith.git " \
        "/root/labs/cse02-programming"
   '''
    cmd = "ls -la"

    try:
        (ret_code, output) = execute_command(cmd)
    except Exception, e:
        print str(e)
