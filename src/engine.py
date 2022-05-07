import enum
from typing import ClassVar, Deque, Mapping, Sequence
from collections import deque

class _Statement(enum.Enum):
    INC_PTN: str = "🐇"     # Increment the pointer​
    DEC_PTN: str = "🐬"     # Decrement the pointer
    INC_BYTE: str = "🐌"    # Increment the byte in the current pointed memory case 
    DEC_BYTE: str = "🦧"    # Decrement the byte in the current pointed memory case
    WRITE: str = "🙈"       # Write the ASCII value of the current pointed memory case
    READ: str = "🐢"        # Read the value and pass it to the current pointed memory case
    GO_FW: str = "🦆"       # Jump after the matched GO_BK if the pointed byte equal 0
    GO_BK: str = "🦛"       # Back after the matched GO_FW if the pointed byte is different than 0


class Engine:
    _STATEMENT_MAPPING: ClassVar[Mapping[str, str]] = {
        _Statement.INC_PTN: "_inc_pointer",
        _Statement.DEC_PTN: "_dec_pointer",
        _Statement.INC_BYTE: "_inc_byte",
        _Statement.DEC_BYTE: "_dec_byte",
        _Statement.WRITE: "_write",
        _Statement.READ: "_read",
        _Statement.GO_FW: "_go_forward",
        _Statement.GO_BK: "_go_backward",
    }

    def __init__(self) -> None:
        self._stack: Deque[_Statement]
        self._memory: Deque[int] = deque([0])
        self._pointer: int = 0
        self._stack_index: int = 0

    def run(self, instructions: str) -> None:
        self._stack = self._build_stack(instructions)

        while self._stack_index < len(self._stack):
            stmt: _Statement = self._stack[self._stack_index]
            getattr(self, self._STATEMENT_MAPPING[stmt])()

            if stmt not in (_Statement.GO_FW, _Statement.GO_BK):
                self._stack_index += 1


    def _build_stack(self, instructions: str) -> Deque[_Statement]:
        stack: Deque[_Statement] = deque([])
        idx: int = 0

        while idx < len(instructions):
            for stmt in _Statement:
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
                if stmt is _Statement.GO_FW:
                    opened_brackets += 1
                elif stmt is _Statement.GO_BK:
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
            stack: Deque[_Statement] = list(self._stack)[:self._stack_index+1]

            for i, stmt in enumerate(stack[::-1]):
                if stmt is _Statement.GO_FW:
                    opened_brackets += 1
                elif stmt is _Statement.GO_BK:
                    closed_brackets += 1

                if opened_brackets == closed_brackets:
                    self._stack_index = len(stack) - i - 1
                    break
            else:
                raise SyntaxError("Missing begin loop.")

        self._stack_index += 1


