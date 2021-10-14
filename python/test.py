import ejdb2

ejdb2.EJDB.init()

db = ejdb2.EJDB()

db.open("test.db")
myset = {"apple":23, "banana":23, "cherry":234}

db.debug(None)

id = db.put_new("test", {"aaa":32})

print(db.get("test", id))

query = ejdb2.EJDBQuery("test", "/[aaa > :aaa]")

query.init();

query.set_placeholder("aaa", 0, 3 );

results = []
db.exec(query, results)

print(results)

print(db.info())

#db.close()