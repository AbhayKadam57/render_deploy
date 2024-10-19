# Get the database using the method we defined in pymongo_test_insert file
from functions.pymongo_getdatabase import get_database


def get_name_symbols(query):
    dbname = get_database()
    collection_name = dbname["stocksdetails"]
    print(collection_name)

    search_results = collection_name.aggregate(
        [
            {
                "$search": {
                    "index": "default",
                    "text": {"query": f"{query}", "path": {"wildcard": "*"}},
                }
            }
        ]
    )
    print("search", search_results)

    first_item = list(search_results)

    print("list", first_item)

    symbol = first_item[0]["symbol"]
    print(symbol)

    name = first_item[0]["name"]
    joined_name = "-".join(name.split())

    print(joined_name)
    return {"name": joined_name, "symbol": symbol.split(".", 1)[0]}
