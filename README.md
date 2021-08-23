# Data team coding exercise - Domantas Vaicys

## Installation instructions

Note: the program is written in Python 3, so it will not work with Python 2

To clone the git repository, please run:

```
git clone https://github.com/domantasvaicys/data-team-exercise-domantas.git
```

There is only 1 dependency: Pandas (https://pandas.pydata.org/docs/). To install please run:

```
pip install pandas
```

The program can then be run by the instruction (from the directory of the cloned git repository):

```
python Order_Summariser_3_Jun.py
```


## Requirements

'to create a simple output detailing how many units of each coloured component that were ordered on 3rd June 2021', the below 3 points summarise how this is met:

- new dataset created detailing each colour and its corresponding sum of all orders
- results of this dataset printed into the terminal
- copy of this dataset also saved locally as a CSV on the machine to allow easy usage elsewhere

## Space-time complexity

below are all the functions written, and their space-time complexity in big O notation.

- allValuesSameTest(values): O(1)
- importComponents(): O(1)
- importOrders(): O(1)
- reduceOrdersTo3June(orders): O(1)
- sumUnitsOrdered(orders, components): O(n) where n is number of component types
- mergeColourAndSums(components, orderSums): O(1)
- printResults(colourSums): O(n) where n is number of component types
- downloadResultsAsCSV(colourSums): O(1)
- programFlow(): O(1) 

The program's total space-time complexity is thus O(n) where n is number of component types.



