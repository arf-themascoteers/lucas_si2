from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi0"],
        ["savi0.5"],
        ["savi1"],
        spec_utils.get_wavelengths(),
        spec_utils.get_wavelengths() + ["savi0"],
        spec_utils.get_wavelengths() + ["savi0.5"],
        spec_utils.get_wavelengths() + ["savi1"]
    ]
    algorithms = ["ann_simple"]
    c = Evaluator(prefix="test", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()