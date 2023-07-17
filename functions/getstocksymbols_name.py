# Get the database using the method we defined in pymongo_test_insert file
from functions.pymongo_getdatabase import get_database


def get_name_symbols(query):
    dbname = get_database()
    collection_name = dbname["stocksdetails"]

    search_results = collection_name.aggregate(
        [
            {
                "$search": {
                    "index": "default1",
                    "text": {"query": f"{query}", "path": {"wildcard": "*"}},
                }
            }
        ]
    )

    first_item = list(search_results)

    symbol = first_item[0]["symbol"]

    name = first_item[0]["name"]
    joined_name = "-".join(name.split())
    return {"name": joined_name, "symbol": symbol.split(".", 1)[0]}
