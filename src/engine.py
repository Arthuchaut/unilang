from typing import ClassVar, Deque, Mapping, Sequence
from collections import deque
from src.config import Statement


class Engine:
    _STATEMENT_MAPPING: ClassVar[Mapping[str, str]] = {
        Statement.INC_PTN: "_inc_pointer",
        Statement.DEC_PTN: "_dec_pointer",
        Statement.INC_BYTE: "_inc_byte",
        Statement.DEC_BYTE: "_dec_byte",
        Statement.WRITE: "_write",
        Statement.READ: "_read",
        Statement.GO_FW: "_go_forward",
        Statement.GO_BK: "_go_backward",
    }

    def __init__(self) -> None:
        self._stack: Deque[Statement]
        self._memory: Deque[int] = deque([0])
        self._pointer: int = 0
        self._stack_index: int = 0

    def run(self, instructions: str) -> None:
        self._stack = self._build_stack(instructions)

        while self._stack_index < len(self._stack):
            stmt: Statement = self._stack[self._stack_index]
            getattr(self, self._STATEMENT_MAPPING[stmt])()

            if stmt not in (Statement.GO_FW, Statement.GO_BK):
                self._stack_index += 1


    def _build_stack(self, instructions: str) -> Deque[Statement]:
        stack: Deque[Statement] = deque([])
        idx: int = 0

        while idx < len(instructions):
            for stmt in Statement:
                if instructions[idx:].startswith(stmt.value):
                    stack.append(stmt)
                    idx += len(stmt.value)
                    break
            else:
                idx += 1
        
        return stack
    
    def _inc_pointer(self) -> None:
        self._pointer += 1

        if self._pointer > len(self._memory) - 1:
            self._memory.append(0)

    def _dec_pointer(self) -> None:
        self._pointer -= 1

        if self._pointer < 0:
            raise RuntimeError(
                "Cannot access a memory case with an index inferior than 0."
            )

    def _inc_byte(self) -> None:
        self._memory[self._pointer] += 1

    def _dec_byte(self) -> None:
        self._memory[self._pointer] -= 1

    def _write(self) -> None:
        print(chr(self._memory[self._pointer]), end="")

    def _read(self) -> None:
        i: int = int(input())
        self._memory[self._pointer] = i

    def _go_forward(self) -> None:
        if self._memory[self._pointer] == 0:
            opened_brackets: int = 0
            closed_brackets: int = 0

            for i, stmt in enumerate(self._stack[self._stack_index:]):
                if stmt is Statement.GO_FW:
                    opened_brackets += 1
                elif stmt is Statement.GO_BK:
                    closed_brackets += 1

                if opened_brackets == closed_brackets:
                    self._stack_index += i
                    break
            else:
                raise SyntaxError("Missing end loop.")

        self._stack_index += 1
        

    def _go_backward(self) -> None:
        if self._memory[self._pointer] != 0:
            opened_brackets: int = 0
            closed_brackets: int = 0
            stack: Deque[Statement] = list(self._stack)[:self._stack_index+1]

            for i, stmt in enumerate(stack[::-1]):
                if stmt is Statement.GO_FW:
                    opened_brackets += 1
                elif stmt is Statement.GO_BK:
                    closed_brackets += 1

                if opened_brackets == closed_brackets:
                    self._stack_index = len(stack) - i - 1
                    break
            else:
                raise SyntaxError("Missing begin loop.")

        self._stack_index += 1


