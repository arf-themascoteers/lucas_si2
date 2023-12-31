from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["red","vnir4"]
    ]
    algorithms = ["ann_savi_learned_only"]
    c = Evaluator(prefix="ann_savi_learned_only2", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()