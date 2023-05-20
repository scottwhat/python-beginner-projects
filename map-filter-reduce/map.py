#map() = applies a function to each item in an iterable



store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

#to_euros = lambda data: (data[0], data[1] * 0.82)

def to_euros(data):
    return data[0], data[1] * 0.82

def to_euros(data):
    return data[0], data[1] / 0.82

store_euros = map(to_euros, store)

store_euros = list(store_euros)

print(store_euros)