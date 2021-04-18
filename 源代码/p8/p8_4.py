# p8_4.py
import pickle

pickle_file = open("E:\\my_list.pkl", "rb")
my_list = pickle.load(pickle_file)
print(my_list)
