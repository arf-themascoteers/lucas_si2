from ann_simple import ANNSimple
from ann_savi import ANNSAVI
from ann_savi_only import ANNSAVIOnly
from ann_savi_rev import ANNSAVIRev


def get_ann_by_name(algorithm):
    if algorithm == "ann_simple":
        return ANNSimple
    elif algorithm == "ann_savi":
        return ANNSAVI
    elif algorithm == "ann_savi_only":
        return ANNSAVIOnly
    elif algorithm == "ann_savi_rev":
        return ANNSAVIRev

