from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths() + ["savi"]
    ]
    algorithms = [f"ann_savi_rev_{i}" for i in range(11)]
    c = Evaluator(prefix="t", folds=10, algorithms=[algorithms], column_groups=column_groups)
    c.process()