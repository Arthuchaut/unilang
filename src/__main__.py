import sys
import pathlib
from src.engine import Engine

if __name__ == "__main__":
    try:
        arg: str = sys.argv[1]
        instructions: str = arg

        if (may_path := pathlib.Path(arg)).exists():
            instructions = may_path.read_text("utf-8")
    except IndexError:
        pass
    else:
        engine: Engine = Engine()
        engine.run(instructions)