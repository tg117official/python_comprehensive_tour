
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]

sys.path.append(str(root)+"\\basic_project_modules_1")

from math_operations.arithmetic import add  # would work with that sys.path


print(add(2, 3))  # 5