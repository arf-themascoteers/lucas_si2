from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths(),
        ["savi"],
        spec_utils.get_wavelengths() + ["savi"]
    ]

    c = Evaluator(prefix="t1", folds=10, algorithms=["mlr","rf","svr"], column_groups=column_groups)
    c.process()