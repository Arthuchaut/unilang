import enum


class Statement(enum.Enum):
    INC_PTN: str = ">"  # Increment the pointer​
    DEC_PTN: str = "<"  # Decrement the pointer
    INC_BYTE: str = "+"  # Increment the byte in the current pointed memory case
    DEC_BYTE: str = "-"  # Decrement the byte in the current pointed memory case
    WRITE: str = "."  # Write the ASCII value of the current pointed memory case
    READ: str = ","  # Read the value and pass it to the current pointed memory case
    GO_FW: str = "["  # Jump after the matched GO_BK if the pointed byte equal 0
    GO_BK: str = (
        "]"  # Back after the matched GO_FW if the pointed byte is different than 0
    )
