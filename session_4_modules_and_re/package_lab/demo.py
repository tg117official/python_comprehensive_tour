from mathpkg import add         # thanks to __init__.py re-export
from mathpkg.stats import mean        # submodule absolute import

print("add(2, 3) =", add(2, 3))
print("mean([2, 4, 6]) =", mean([2, 4, 6]))
