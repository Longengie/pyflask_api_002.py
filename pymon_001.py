import pymongo 
from pymongo import MongoClient 

MONGO_URI = 'mongodb+srv://db01:csdl001@cluster0-q8a6f.mongodb.net/test?retryWrites=true&w=majority'
cluster = MongoClient(MONGO_URI)

db = cluster["ShopOnline"]
collection = db["NhanVien"]

nv_post = {'_id': 1002, 'HoTen': r'Phùng Văn Há', 'GioiTinh': 'Nam', 'Tuoi': 57, 'ThamNien': 20}
collection.insert_one(nv_post)

results = collection.find({})

for item in results:
    print(item)