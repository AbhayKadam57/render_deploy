# Get the database using the method we defined in pymongo_test_insert file
from functions.pymongo_getdatabase import get_database


def get_name_symbols(query):

    dbname = get_database()
    collection_name = dbname["stocksdetails"]

    search_results = collection_name.find({"$text": {"$search": f"\"{query}\""}})

    print(search_results)

    # for item in search_results:
    #     symbol=item.get("symbol")
    #     name=item.get("name").lower()
    #     joined_name="-".join(name.split())
    # return {"name":joined_name,"symbol":symbol}

    first_item = search_results[0]
    symbol = first_item.get("symbol")
    name = first_item.get("name").lower()
    joined_name = "-".join(name.split())
    result = {"name": joined_name, "symbol": symbol}

    return result
        


