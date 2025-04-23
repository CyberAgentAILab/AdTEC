from typing import Any, Iterable


def obj_join(separator: Any, iterable: Iterable[Any]) -> list[Any]:
    """
    任意のオブジェクトのイテラブルを区切り文字で区切りながら結合する関数

    Args:
        separator: 区切りとなるオブジェクト
        iterable: 結合するオブジェクトのイテラブル

    Returns:
        区切り文字で区切られたオブジェクトのリスト
    """
    result = []
    iterator = iter(iterable)

    # 最初の要素を追加（区切り文字なし）
    try:
        result.append(next(iterator))
    except StopIteration:
        return result  # 空のイテラブルの場合は空リストを返す

    # 残りの要素を区切り文字と共に追加
    for item in iterator:
        result.append(separator)
        result.append(item)

    return result
