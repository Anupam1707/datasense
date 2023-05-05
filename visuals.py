"""This program is the Graphing Program of the App."""

#Function to compile multiple data in to a single format for graphing and analysis
def data(sheetname, colno=None, rowno=None, alldata=None, nums=False):
    if rowno == None and alldata == None and colno != None:
        data = sheetname.col_values(colno)
        data = data[1:]
        try :
            if type(float(data[0])) == float:
                data = [ float(x) for x in data]
        except ValueError:
            pass
        data.append(sheetname.cell(1,colno).value)
        
    elif rowno != None and alldata == None and colno == None:
        data = sheetname.row_values(rowno)
        
    elif rowno != None and alldata == None and colno != None:
        data = sheetname.cell(rowno, colno).value
        
    elif rowno == None and alldata != None and colno == None:
        data = sheetname.get_all_records()

    
    return data

#Function to get the average of data
def avg(datalist):
    return sum(datalist)/len(datalist)

#Function to get the total of a data
def total(datalist):
    return sum(datalist)

#Function to compile two data lists into a dictionary
def dt(keys, values):
    dt = {}
    for key in keys:
        dt[key] = 0
    for key in range(len(keys)):
        for value in range(len(values)):
            if key[value] == keys[key]:
                dt[keys[key]] += values[value]
        break
    return dt

#Function to Plot Horizontal Bar Graph, Vertical Bar Graph and Histogram
def plotb(*ls, t = "bv"):
    xval = []
    yval = []
    fig = plt.figure(figsize = (10, 5))
                     
    if len(ls) == 2:
            xval = ls[0]
            yval = ls[1]
            
            x = ls[0][-1]
            x = x.title()
            y = ls[1][-1]
            y = y.title()
            
            ls[0].remove(ls[0][-1])
            ls[1].remove(ls[1][-1])
    
            #Vertical Bar Graph
            if t == "bv":
                plt.bar(xval, yval, color = "blue")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Industry Sales Analysis")
                plt.show()
                
            #Horizontal Bar Graph
            elif t == "bh":
                plt.barh(xval, yval, color = "blue")
                plt.xlabel(y)
                plt.ylabel(x)
                plt.title("Industry Sales Analysis")
                plt.show()

#Function to Plot a Pie Chart
def pie(dt):
    labels = dt.keys()
        
    y = np.array(list(dt.values))
    mylabels = labels
    plt.pie(y, labels = mylabels)
    plt.show()
    
