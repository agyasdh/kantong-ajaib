import numpy
import csv

#Upload array ke file csv
arr1 = [i for i in range(500)]
arr2 = [i for i in range(1000)]
arr3 = [i for i in range(2000)]
    
with open('kantongajaib.csv', 'a') as kantongajaib_append:
    numpy.savetxt(record_append, numpy.asarray([arr1]), delimiter=',')
    numpy.savetxt(record_append, numpy.asarray([arr2]), delimiter=',')
    numpy.savetxt(record_append, numpy.asarray([arr3]), delimiter=',')

#Download array dari file csv
two_dim_arr = []
with open('kantongajaib.csv', 'r') as kantongajaib_read:
    reader = csv.reader(record_read)
    for i, each_arr in enumerate(reader):
        two_dim_arr.append([eval(each) for each in each_arr])
        
# Print array 
for each_line in two_dim_arr:
  print(each_line)