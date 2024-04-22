from data.db_connection import db_connection_pool

#loading data for user overview analysis section

def load_top_ten_handsets_data():
    """
        this function will select the top handsets used by users
    """
    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "Handset Type",count("Handset Type") count 
            from public.xdr_data
            group by "Handset Type"
            order by count desc
            limit 10
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data