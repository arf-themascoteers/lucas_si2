from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi"],
        ["savi2"],
        spec_utils.get_wavelengths(),
        spec_utils.get_wavelengths() + ["savi"],
        spec_utils.get_wavelengths() + ["savi2"],
        spec_utils.get_wavelengths() + ["savi"] +["savi2"]
    ]
    algorithms = ["mlr", "svr", "rf"]
    c = Evaluator(prefix="test_trad", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()