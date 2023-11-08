from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["red","vnir4"]
    ]
    algorithms = ["ann_savi_learnable_only_bound"]
    c = Evaluator(prefix="ann_savi_learnable_only_bound", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()