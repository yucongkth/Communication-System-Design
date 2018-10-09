from Client_get import Do_get

NFMdata=Do_get("http://127.0.0.1:2500/")
data=NFMdata.get_data()
print(data)