from sqlalchemy import create_engine

def load_to_mysql(dataframe, table_name, db_uri):
    engine = create_engine(db_uri)
    dataframe.to_sql(table_name, con=engine, if_exists='append', index=False)
