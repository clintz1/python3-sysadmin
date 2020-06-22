# Setting system path before test
import sys
path = "\\".join(sys.path[0].split('\\\\')[:-1])
sys.path.append(path)

import pytest
import subprocess

from pgbackup import pgdump
url = "postgres://postgres:postgres@127.0.0.1:5432/sample"


def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)
