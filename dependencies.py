from fastapi import Query, Depends


class SpecificQuery:
    def __init__(self, limit: int = 10):
        self.limit = limit

class CommonQuery:
    def __init__(
        self,
        specific_query: SpecificQuery = Depends(),
        page_size: int = Query(8, ge=8),
        page: int = 1
    ):
        self.specific_query = specific_query
        self.page_size = page_size
        self.page = page
