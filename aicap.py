def caps():
    print("Choose between :")
    print("1. Keyboard")
    print("2. Voice")
    q = int(input("Enter on of the number : "))
    if q == 1:
        query = str(input("Enter your query : "))
    elif q == 2:
        query = takeCommand()
    if "plot a" in query:
        query = query[6:]
        if "horizontal bar graph" in query:
            query = query[25:]
            query = query.split()
            query.remove("and")
            if len(query) == 2:
                plotb(data(sales, col[query[0]]), data(sales, col[query[1]]), t = "bh")
        elif "vertical bar graph" in query:
            query = query[24:]
            query = query.split()
            query.remove("and")
            if len(query) == 2:
                plotb(data(sales, col[query[0]]), data(sales, col[query[1]]), t = "bv")
        elif "pie chart" in query:
            query = query[15:]
            query = query.split()
            query.remove("and")
            pie(data(sales, col[query[1]]), data(sales, col[query[0]]))
            
    elif "plot" in query:
        query = query[4:]
        if "horizontal bar graph" in query:
            query = query[25:]
            query = query.split()
            query.remove("and")
            if len(query) == 2:
                plotb(data(sales, col[query[0]]), data(sales, col[query[1]]), t = "bh")
        elif "vertical bar graph" in query:
            query = query[24:]
            query = query.split()
            query.remove("and")
            if len(query) == 2:
                plotb(data(sales, col[query[0]]), data(sales, col[query[1]]), t = "bv")
        elif "pie chart" in query:
            query = query[15:]
            query = query.split()
            query.remove("and")
            pie(data(sales, col[query[1]]), data(sales, col[query[0]]))

