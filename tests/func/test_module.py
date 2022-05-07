import subprocess
import pytest
from _pytest.capture import CaptureFixture
from src.engine import Statement


@pytest.mark.func
class TestModule:
    @pytest.mark.parametrize(
        "argument, expected_output",
        [
            (
                Statement.INC_BYTE.value * 52
                + Statement.WRITE.value
                + Statement.INC_PTN.value
                + Statement.INC_BYTE.value * 50
                + Statement.WRITE.value,
                "42",
            ),
        ],
    )
    def test_call(
        self,
        argument: str,
        expected_output: str,
    ) -> None:
        output: bytes = subprocess.check_output(["python", "-m", "src", argument])
        assert output.decode("utf8") == expected_output
