def execute_query_noncompliant(request):
        
    import sqlite3
        
    name = request.GET.get("name")
        
    query = "SELECT * FROM Users WHERE name = " + name + ";"
        
    with sqlite3.connect("example.db") as connection:
        
        cursor = connection.cursor()
        
        # Noncompliant: user input is used without sanitization.
        
        cursor.execute(query)
        
        connection.commit()
        
        connection.close()
