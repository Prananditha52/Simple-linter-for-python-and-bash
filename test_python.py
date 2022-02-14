import subprocess
import pathlib


def test_show():
    # compute actual output
    cmd = ['python', 'space.py', '--show', "testcase/sample_input.py"]
    actual_output = subprocess.check_output(cmd, encoding="utf-8", close_fds=True)

    # get expected output
    expected_output = pathlib.Path("testcase/sample_output_show.txt").read_text()

    # compare
    assert actual_output.rstrip() == expected_output.rstrip()


def test_fix():
    # compute actual output
    cmd = ['python', 'space.py', '--fix', "testcase/sample_input.py"]
    actual_output = subprocess.check_output(cmd, encoding="utf-8", close_fds=True)

    # get expected output
    expected_output = pathlib.Path("testcase/sample_output_fix.txt").read_text()

    # compare
    assert actual_output.rstrip() == expected_output.rstrip()
