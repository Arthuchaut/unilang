from typing import Deque, Type
from collections import deque
import pytest
from _pytest.capture import CaptureFixture
from pytest_mock import MockerFixture
from src.engine import Engine, Statement


@pytest.mark.unit
class TestEngine:
    @pytest.mark.parametrize(
        "instructions, expected_memory_state, expected_output",
        [
            (
                Statement.INC_BYTE.value * 52
                + Statement.WRITE.value
                + Statement.INC_PTN.value
                + Statement.INC_BYTE.value * 50
                + Statement.WRITE.value,
                deque([52, 50]),
                "42",
            ),
        ],
    )
    def test_run(
        self,
        instructions: str,
        expected_memory_state: Deque[int],
        expected_output: str,
        capsys: CaptureFixture,
    ) -> None:
        engine: Engine = Engine()
        engine.run(instructions)
        assert engine._memory == expected_memory_state
        assert capsys.readouterr().out == expected_output

    @pytest.mark.parametrize(
        "instructions, expected",
        [
            (
                f"{Statement.INC_BYTE.value}"
                f"{Statement.INC_BYTE.value}"
                f"{Statement.INC_BYTE.value}"
                f"{Statement.INC_BYTE.value}"
                f"{Statement.INC_PTN.value}"
                f"{Statement.INC_BYTE.value}"
                f"{Statement.INC_BYTE.value}"
                f"{Statement.WRITE.value}",
                deque(
                    [
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.INC_PTN,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.WRITE,
                    ]
                ),
            ),
            (
                f"""
                {Statement.INC_BYTE.value}{Statement.INC_BYTE.value}
                {Statement.WRITE.value}
                {Statement.INC_PTN.value}
                {Statement.INC_BYTE.value}{Statement.INC_BYTE.value}
                {Statement.WRITE.value}
                """,
                deque(
                    [
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.WRITE,
                        Statement.INC_PTN,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.WRITE,
                    ]
                ),
            ),
        ],
    )
    def test__build_stack(
        self,
        instructions: str,
        expected: Deque[Statement],
    ) -> None:
        engine: Engine = Engine()
        res: Deque[Statement] = engine._build_stack(instructions)
        assert res == expected

    def test__inc_pointer(self) -> None:
        engine: Engine = Engine()
        assert len(engine._memory) == 1
        assert engine._pointer == 0
        engine._inc_pointer()
        assert len(engine._memory) == 2
        assert engine._pointer == 1

    @pytest.mark.parametrize(
        "inc_number, dec_number, throwable",
        [
            (1, 1, None),
            (2, 1, None),
            (0, 1, RuntimeError),
            (1, 2, RuntimeError),
        ],
    )
    def test__dec_pointer(
        self,
        inc_number: int,
        dec_number: int,
        throwable: Type[RuntimeError] | None,
    ) -> None:
        engine: Engine = Engine()
        assert len(engine._memory) == 1

        for _ in range(inc_number):
            engine._inc_pointer()

        if throwable:
            with pytest.raises(throwable):
                for _ in range(dec_number):
                    engine._dec_pointer()
        else:
            for _ in range(dec_number):
                engine._dec_pointer()

            assert engine._pointer == inc_number - dec_number

    def test__inc_byte(self) -> None:
        engine: Engine = Engine()
        assert engine._memory[0] == 0
        engine._inc_byte()
        assert engine._memory[0] == 1

    def test__dec_byte(self) -> None:
        engine: Engine = Engine()
        assert engine._memory[0] == 0
        engine._dec_byte()
        assert engine._memory[0] == -1

    def test__write(self, capsys: CaptureFixture) -> None:
        engine: Engine = Engine()
        engine._memory[0] = 97
        engine._write()
        assert capsys.readouterr().out == "a"

    @pytest.mark.parametrize(
        "value, throwable",
        [
            ("42", None),
            ("hello", ValueError),
        ],
    )
    def test__read(
        self,
        value: str,
        throwable: Type[ValueError] | None,
        mocker: MockerFixture,
    ) -> None:
        mocker.patch("builtins.input", lambda: value)
        engine: Engine = Engine()

        if throwable:
            with pytest.raises(throwable):
                engine._read()
        else:
            engine._read()
            assert engine._memory[0] == int(value)

    @pytest.mark.parametrize(
        "stack, pointer, memory_value, stack_index, expected_stack_index, throwable",
        [
            (
                deque(
                    [
                        Statement.GO_FW,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.GO_BK,
                        Statement.DEC_BYTE,
                    ]
                ),
                0,
                0,
                0,
                4,
                None,
            ),
            (
                deque(
                    [
                        Statement.GO_FW,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.DEC_BYTE,
                    ]
                ),
                0,
                1,
                0,
                1,
                None,
            ),
            (
                deque(
                    [
                        Statement.GO_FW,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.DEC_BYTE,
                    ]
                ),
                0,
                0,
                0,
                0,
                SyntaxError,
            ),
        ],
    )
    def test__go_forward(
        self,
        stack: Deque[Statement],
        pointer: int,
        memory_value: int,
        stack_index: int,
        expected_stack_index: int,
        throwable: Type[SyntaxError] | None,
    ) -> None:
        engine: Engine = Engine()
        engine._stack = stack
        engine._stack_index = stack_index
        engine._pointer = pointer
        engine._memory = deque([0] + [0] * pointer)
        engine._memory[pointer] = memory_value

        if throwable:
            with pytest.raises(throwable):
                engine._go_forward()
        else:
            engine._go_forward()

        assert engine._stack_index == expected_stack_index

    @pytest.mark.parametrize(
        "stack, pointer, memory_value, stack_index, expected_stack_index, throwable",
        [
            (
                deque(
                    [
                        Statement.GO_FW,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.GO_BK,
                    ]
                ),
                0,
                1,
                3,
                1,
                None,
            ),
            (
                deque(
                    [
                        Statement.GO_FW,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.DEC_BYTE,
                        Statement.GO_BK,
                        Statement.INC_BYTE,
                    ]
                ),
                0,
                0,
                4,
                5,
                None,
            ),
            (
                deque(
                    [
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.INC_BYTE,
                        Statement.DEC_BYTE,
                        Statement.GO_BK,
                    ]
                ),
                0,
                1,
                4,
                4,
                SyntaxError,
            ),
        ],
    )
    def test__go_backward(
        self,
        stack: Deque[Statement],
        pointer: int,
        memory_value: int,
        stack_index: int,
        expected_stack_index: int,
        throwable: Type[SyntaxError] | None,
    ) -> None:
        engine: Engine = Engine()
        engine._stack = stack
        engine._stack_index = stack_index
        engine._pointer = pointer
        engine._memory = deque([0] + [0] * pointer)
        engine._memory[pointer] = memory_value

        if throwable:
            with pytest.raises(throwable):
                engine._go_backward()
        else:
            engine._go_backward()

        assert engine._stack_index == expected_stack_index
