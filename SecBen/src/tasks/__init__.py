import json
from pprint import pprint
from typing import List, Union

import lm_eval.base 

from . import Sec

TASK_REGISTRY = {
    "Sec_Cls_4": Sec.Sec_Cls_4,
    "Sec_Cls_6": Sec.Sec_Cls_6,
    "Sec_Cls_8": Sec.Sec_Cls_8,
    "Sec_Cls_9": Sec.Sec_Cls_9,
    "Sec_Cls_15": Sec.Sec_Cls_15,
    "Sec_Cls_16": Sec.Sec_Cls_16,
    "Sec_Cls_18": Sec.Sec_Cls_18,
    "Sec_Cls_25": Sec.Sec_Cls_25,
    
    "Sec_AS_3_1": Sec.Sec_AS_3_1,
    "Sec_AS_3_2": Sec.Sec_AS_3_2,
    "Sec_AS_3_3": Sec.Sec_AS_3_3,
    "Sec_AS_3_4": Sec.Sec_AS_3_4,
    "Sec_AS_10": Sec.Sec_AS_10,
    "Sec_AS_12": Sec.Sec_AS_12,
    "Sec_AS_14": Sec.Sec_AS_14,

    "Sec_CQA_28": Sec.Sec_CQA_28,

    "Sec_NER_29_cyner": Sec.Sec_NER_29_cyner,
    "Sec_NER_30_aptner": Sec.Sec_NER_30_aptner,
    "Sec_AS_31_TheHackerNews": Sec.Sec_AS_31_TheHackerNews,
    "Sec_Cls_32_cve": Sec.Sec_Cls_32_cve,
    "Sec_Cls_33_email": Sec.Sec_Cls_33_email,
    "Sec_Cls_34_mitre": Sec.Sec_Cls_34_mitre,
    "Sec_Cls_35_web": Sec.Sec_Cls_35_web,

    "Sec_NER_29_cyner_TEST": Sec.Sec_NER_29_cyner_TEST,
    

    "Sec_AS_1": Sec.Sec_AS_1,
    "Sec_Cls_27": Sec.Sec_Cls_27,

    "Sec_CQA_28_TEST": Sec.Sec_CQA_28_TEST,
    "Sec_AS_3_4_TEST": Sec.Sec_AS_3_4_TEST,
    "Sec_Cls_4_TEST": Sec.Sec_Cls_4_TEST,

}


ALL_TASKS = sorted(list(TASK_REGISTRY))

_EXAMPLE_JSON_PATH = "split:key:/absolute/path/to/data.json"

def add_json_task(task_name):
    """Add a JSON perplexity task if the given task name matches the
    JSON task specification.

    See `json.JsonPerplexity`.
    """
    if not task_name.startswith("json"):
        return

    def create_json_task():
        splits = task_name.split("=", 1)
        if len(splits) != 2 or not splits[1]:
            raise ValueError(
                "json tasks need a path argument pointing to the local "
                "dataset, specified like this: json="
                + _EXAMPLE_JSON_PATH
                + ' (if there are no splits, use "train")'
            )

        json_path = splits[1]
        if json_path == _EXAMPLE_JSON_PATH:
            raise ValueError(
                "please do not copy the example path directly, but substitute "
                "it with a path to your local dataset"
            )
        return lambda: json.JsonPerplexity(json_path)

    TASK_REGISTRY[task_name] = create_json_task()


def get_task(task_name):
    try:
        add_json_task(task_name)
        return TASK_REGISTRY[task_name]
    except KeyError:
        print("Available tasks:")
        pprint(TASK_REGISTRY)
        raise KeyError(f"Missing task {task_name}")


def get_task_name_from_object(task_object):
    for name, class_ in TASK_REGISTRY.items():
        if class_ is task_object:
            return name

    # this gives a mechanism for non-registered tasks to have a custom name anyways when reporting
    return (
        task_object.EVAL_HARNESS_NAME
        if hasattr(task_object, "EVAL_HARNESS_NAME")
        else type(task_object).__name__
    )


def get_task_dict(task_name_list: List[Union[str, lm_eval.base.Task]]):
    task_name_dict = {
        task_name: get_task(task_name)()
        for task_name in task_name_list
        if isinstance(task_name, str)
    }
    task_name_from_object_dict = {
        get_task_name_from_object(task_object): task_object
        for task_object in task_name_list
        if not isinstance(task_object, str)
    }

    assert set(task_name_dict.keys()).isdisjoint(set(task_name_from_object_dict.keys()))
    return {**task_name_dict, **task_name_from_object_dict}
