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

def avg(datalist):
    return sum(datalist)/len(datalist)

def total(datalist):
    return sum(datalist)

def dt(keys, values):
    dt = {}
    for key in keys:
        dt[key] = 0
        for value in values:
            dt[key] += value
            values.remove(value)
            break
    return dt

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

            if t == "bv":
                plt.bar(xval, yval, color = "blue")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Industry Sales Analysis")
                plt.show()
            elif t == "bh":
                plt.barh(xval, yval, color = "blue")
                plt.xlabel(y)
                plt.ylabel(x)
                plt.title("Industry Sales Analysis")
                plt.show()
    elif len(ls) == 3:
            prim = ls[0]
            p = ls[0][-1]
            p = y.title()
            ls[0].remove(ls[0][-1])
            
            n1 = ls[1]
            y1 = ls[1][-1]
            y1 = y1.title()
            
            
            n2 = ls[2]
            y2 = ls[2][-1]
            y2 = y2.title()

            xax = np.arange(len(prim))
                
            plt.bar(xax - 0.2 ,n1,width = 0.4,label = y1)
            plt.bar(xax + 0.2, n2,width = 0.4, label = y2)
            
            plt.xticks(xax, xval)
            plt.legend()
            plt.title("Industry Sales Analysis")
            plt.show()
            
def pie(dt):
    
    ls.remove(ls[-1])
    if labels != None:
        labels.remove(labels[-1])
        
    y = np.array(ls)
    mylabels = labels
    plt.pie(y, labels = mylabels)
    plt.show()
    
