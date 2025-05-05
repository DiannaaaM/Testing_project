from sqlalchemy import create_engine, text
import pytest

@pytest.fixture()
def connecting_db():
    engine = create_engine("postgresql://postgres:493138@localhost:5432/Testing")
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS fruits (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
        """))
    return engine

def test_add_items(connecting_db):
    with connecting_db.connect() as connection:
        result_columns = connection.execute(
            text("SELECT column_name FROM information_schema.columns WHERE table_name='fruits';")
        )
        columns = result_columns.fetchall()
        assert any(col[0] == 'name' for col in columns)
        connection.execute(text("INSERT INTO fruits (name) VALUES (:name)"), {"name": "Cherry"})
        connection.execute(text("INSERT INTO fruits (name) VALUES (:name)"), {"name": "Banana"})
        connection.execute(text("INSERT INTO fruits (name) VALUES (:name)"), {"name": "Strawberry"})
        connection.execute(text("INSERT INTO fruits (name) VALUES (:name)"), {"name": "Melon"})

        result = connection.execute(text('SELECT * FROM fruits'))
        rows = result.fetchall()

        assert any(row['name'] == 'Cherry' for row in rows)
        assert any(row['name'] == 'Banana' for row in rows)
        assert any(row['name'] == 'Strawberry' for row in rows)
        assert any(row['name'] == 'Melon' for row in rows)


def test_put_items(connecting_db):
    with connecting_db.connect() as connection:
        connection.execute("UPDATE fruits SET name='some_fruit' WHERE name='Banana'")
        result = connection.execute(text('SELECT * FROM fruits'))
        rows = result.fetchall()
        assert any(row['name'] == 'some_fruit' for row in rows)


def test_delete_items(connecting_db):
    with connecting_db.connect() as connection:
        connection.execute('delete from fruits')
        result = connection.execute(text('SELECT * FROM fruits'))
        rows = result.fetchall()
        assert rows == []