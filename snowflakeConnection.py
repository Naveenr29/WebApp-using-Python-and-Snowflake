from snowflake import connector


# Snowflake connection
def sfconnect():
    cnx = connector.connect(
    account='<Snowflake Account>',  # Enter your snowflake account info
    user='<Snowflake User>',    # Enter your snowflake user info
    password='<Snowflake Password>',    # Enter your snowflake acc password
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
    )
    return cnx
