from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths(),
        ["savi"],
        spec_utils.get_wavelengths() + ["savi"]
    ]

    c = Evaluator(prefix="t3", folds=10, algorithms=["ann_simple"], column_groups=column_groups)
    c.process()