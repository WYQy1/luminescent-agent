from python_fundamentals.generators.batch_generator import batch_generator


def test_batch_generator_splits_into_batches():
    assert list(batch_generator(list(range(1, 11)), 3)) == [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [10]
    ]


def test_batch_generator_empty_input():
    assert list(batch_generator([], 3)) == []


def test_batch_generator_rejects_non_positive_batch_size():
    try:
        list(batch_generator([1, 2], 0))
    except ValueError as exc:
        assert "大于 0" in str(exc)
    else:
        raise AssertionError("batch_size 为 0 时应抛出 ValueError")
