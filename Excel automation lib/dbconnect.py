from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select

# 1. Engine create karo (SQLite database file ya memory me)
engine = create_engine("sqlite:///students_sqlalchemy.db", echo=True)

# 2. Metadata object
meta = MetaData()

# 3. Table define karo
students = Table(
    "students_sqlalchemy", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

# Step 4: Table create karo database me
meta.create_all(engine)

print("✅ Connected to Database & Table Created!")

# Step 5: Insert some records
with engine.connect() as conn:
    # ek student insert
    stmt = insert(students).values(name="Vishal", age=21)
    conn.execute(stmt)

    # multiple students insert
    conn.execute(
        students.insert(),
        [
            {"name": "Honey", "age": 22},
            {"name": "Raj", "age": 23}
        ]
    )

    conn.commit()  # ✅ commit karna zaroori hai SQLite me
    print("✅ Data inserted successfully!")

# Step 6: Select (Read) records
with engine.connect() as conn:
    result = conn.execute(select(students))  # ✅ correct way in SQLAlchemy 2.x
    print("\n📂 Students in Database:")
    for row in result:
        print(row._mapping)  # ✅ better output as dict-like
