from typing import Tuple


def parse_entities(data: str) -> set:
    """
    Функция извлекает сущности из строки данных.
    в формате {(entity_name, entity)}.

    :param data: строка с сущностями через запятую.
    :return: множество уникальных сущностей
    """
    if not data.strip():
        return set()

    entities = data.split(',')

    return set(tuple(entity.strip().split('_', 1)) for entity in entities)


def score_fn(gold: str, pred: str) -> Tuple[int, int, int]:
    """
    Считает метрики:
    F1-score
    Precision
    Recall

    :param gold: строка с эталонной разметкой
    :param pred: строка с разметкой LLM

    :return: значения метрик
    """
    gold_entities = parse_entities(gold)
    pred_entities = parse_entities(pred)

    tp = len(gold_entities & pred_entities)
    if tp == 0:
        return 0.0, 0.0, 0.0

    fp = len(pred_entities - gold_entities)
    fn = len(gold_entities - pred_entities)

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    return f1_score, precision, recall
