# https://visualgo.net/bn/sorting

def insertionSort(data):

    for i in range(1, len(data)):
        key = data[1]
        j = i-1
        # print(">> i[{}] j[{}]".format(i, key, j))

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

            data[j+1] = key

        return

ages = [12, 34, 11, 67, 88, 77, 37, 43, 51, 13]

# original data = 12, 34, 11, 67, 88, 77, 37, 43, 51, 13
# i[
insertionSort(ages)

for age in ages:
    print(age, end=" ")
    