from pymongo import MongoClient

uri = "mongodb+srv://testuser:<Test123>@cluster0.dbhpqrl.mongodb.net/?appName=Cluster0"

print("URI:", uri)   # ✅ THIS LINE

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ CONNECTED")
except Exception as e:
    print("❌ ERROR:", e)