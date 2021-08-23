import datetime as dt
import pandas as pd 

#test to check if all values passed in argument are the same (i.e. no more than 1 unique value)
def allValuesSameTest(values):
    valuesInNumpy = values.to_numpy()
    if (valuesInNumpy[0] == valuesInNumpy).all():
        return True
    else:
        return False

#imports and returns the components csv as a pandas dataframe
def importComponents():
    components = pd.read_csv('data/components.csv')
    print('Components CSV loaded')
    return components

#imports and returns the orders JSON as a pandas dataframe
def importOrders():
    orders = pd.read_json('data/orders.json.txt', lines=True)
    orders['timestamp'] = pd.to_datetime(orders['timestamp']).dt.date
    print('Orders JSON loaded')
    return orders

#takes the orders dataframe as an argument and reduces the size of the dataset to 3rd of June, returning the result
def reduceOrdersTo3June(orders):
    june3 = (orders['timestamp'] > dt.date(2021, 6, 2)) & (orders['timestamp'] < dt.date(2021, 6, 4))
    orders3June = orders.loc[june3]
    if allValuesSameTest(orders3June['timestamp']) == True: #checks there is only 1 time stamp ('2021-06-03')
            print('Orders succesfully reduced to 3rd of June 2021')
    else:
            print('ERROR: Orders not correctly reduced to 3rd of June 2021')     
    return orders3June

#tallies and records the units ordered per component colour, returning a dataframe consisting of the component ID and its corresponding order sum
def sumUnitsOrdered(orders, components):
    for component in components['componentId']: #creates a separate column for each component ID to record units ordered
        orders[component] = orders['units'].apply(lambda x: x.get(component))
    orderSumDataList = []
    for component in components['componentId']: #sums each of the columns to create a sum of orders for each component ID
        orderSumDataList.append([component, orders[component].sum()])
    orderSumDataFrame = pd.DataFrame(orderSumDataList, columns = ['componentId', 'orders'])
    print('Orders for each component have been summed up')
    return orderSumDataFrame

#merges the components data file together with the new order sums, and returns a cleaned file consisting of only the colour and its corresponding orders
def mergeColourAndSums(components, orderSums):
    colourSums = pd.merge(components, orderSums, on='componentId')
    colourSums = colourSums.drop(['componentId', 'costPrice'], axis=1)
    colourSums['orders'] = colourSums['orders'].astype(int)
    print('Orders have been paired with their corresponding colour')
    return colourSums

#prints the row by row result of component colour and its corresponding sum of orders
def printResults(colourSums):
    print('Below is a summary of how many units of each coloured components were ordered on 3rd June 2021')
    for index, row in colourSums.iterrows():
        print(row['colour'], ':', row['orders'], 'units')

#saves the colour and its corresponding order sums data frame as a CSV
def downloadResultsAsCSV(colourSums):
    fileName = 'Summary_of_3rd_June_orders.csv'
    colourSums.to_csv(fileName, index=False)
    print('Results saved as', fileName)

#runs the program's functions in the correct order
def programFlow():
    components = importComponents()
    orders = importOrders()
    orders = reduceOrdersTo3June(orders)
    orderSums = sumUnitsOrdered(orders, components)
    colourSums = mergeColourAndSums(components, orderSums)
    printResults(colourSums)
    downloadResultsAsCSV(colourSums)

programFlow()