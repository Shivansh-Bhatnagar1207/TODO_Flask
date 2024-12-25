def todoEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
    }


def todosEntity(items) -> list:
    return [todoEntity(item) for item in items]
