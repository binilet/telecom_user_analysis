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


def load_top_three_handset_manufactureres():
    
    """
    this data loader query will fetch the top three handset manufactureres, the handsets are first 'distincted' and then counted.
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "Handset Manufacturer",count(distinct("Handset Type")) Count from public.xdr_data
            group by "Handset Manufacturer"
            order by Count desc
            limit 3
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data


def load_top_five_handset_per_top_three_manufactureres():
    
    """
    this data loader query will fetch the top three handset manufactureres only, then the actual processing of assigning top5 devices will be done with pandas
    could also be used with sql window functions.

    it selects handset manufactureres and handset types by integrating the first query to filter the top3 manufactureres
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            SELECT "Handset Manufacturer", "Handset Type"
            FROM public.xdr_data
            WHERE "Handset Manufacturer" IN (
                SELECT "Handset Manufacturer"
                FROM (
                    SELECT "Handset Manufacturer", COUNT(*) AS ct
                    FROM public.xdr_data
                    GROUP BY "Handset Manufacturer"
                    ORDER BY ct DESC
                    LIMIT 3
                ) AS subquery
            );
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data


def load_data_for_univariate_dispersion_analysis():
    """
        selects important data for univariance dispersion analysis
    """
    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "Handset Manufacturer","Handset Type","MSISDN/Number","Dur. (ms)","Social Media DL (Bytes)",
            "Social Media UL (Bytes)","Google DL (Bytes)","Google UL (Bytes)",
            "Email DL (Bytes)","Email UL (Bytes)","Youtube DL (Bytes)","Youtube UL (Bytes)",
            "Netflix DL (Bytes)","Netflix UL (Bytes)","Gaming DL (Bytes)",
            "Gaming UL (Bytes)","Total UL (Bytes)","Total DL (Bytes)"
            from public.xdr_data
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data

def load_variable_transformation_data():
    """
        selects data for variable stransformation;
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "MSISDN/Number","Dur. (ms)","Total UL (Bytes)","Total DL (Bytes)"
            from public.xdr_data 
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data

def load_correlation_data():
    """
    selects data for correlation analysis
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "Social Media DL (Bytes)",
            "Social Media UL (Bytes)","Google DL (Bytes)","Google UL (Bytes)",
            "Email DL (Bytes)","Email UL (Bytes)","Youtube DL (Bytes)","Youtube UL (Bytes)",
            "Netflix DL (Bytes)","Netflix UL (Bytes)","Gaming DL (Bytes)",
            "Gaming UL (Bytes)","Other DL (Bytes)","Other UL (Bytes)"
            from public.xdr_data 
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data



#the following set of queries are for user engagment metrics

def load_user_engagment_metrics_data():
    """
    selects data for user engagment metrics
    it returns the session frequency,the total duration and total data grouped by user
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "MSISDN/Number" as tuser,CAST(count(*) AS float) as sessionFrequencie,sum("Dur. (ms)") as duration,sum("Total UL (Bytes)" + "Total DL (Bytes)") as totalData
            from public.xdr_data where "MSISDN/Number" is not null
            group by "MSISDN/Number"
            order by sessionFrequencie desc
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data

#queries for experience
def load_user_experience_metrics_data():
    """
    selects data for user experience metrics
    """

    db_connection_pool.reset_connection_pool()
    conn = db_connection_pool.get_connection()
    try:
        with conn.cursor() as cur:
            query = """
            select "MSISDN/Number",
                    "Handset Type",
                    "Avg RTT DL (ms)",
                    "Avg RTT UL (ms)",
                    "TCP DL Retrans. Vol (Bytes)",
                    "TCP UL Retrans. Vol (Bytes)",
                    "Avg Bearer TP DL (kbps)",
                    "Avg Bearer TP UL (kbps)"
                     from public.xdr_data
            """
            cur.execute(query)
            data = cur.fetchall()
    finally:
        cur.close()
        db_connection_pool.release_connection(conn)
    return data