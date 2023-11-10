from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths() + ["savi"]
    ]
    algorithms = ["ann_savi_rev_3"]
    c = Evaluator(prefix="ann_savi_rev_3", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()