
import grpc, sys

import grpc_py_database_accessing.api.grpc as api


TB = 'qrcodes_tb'
DB_HOST = 'postgres://postgres:postgres@postgres:5433/postgres'

class Database:

    def __init__(self, host: str, dbHost: str) -> None:
        self.host = host
        self.conn = grpc.insecure_channel(host) 
        self.stub = api.DatabaseStub(self.conn)
        self.dbHost = dbHost
    
    def get(self, columns: str, table: str, condition: str) -> api.GetDbResponse:
        return self.stub.GetDb(api.GetDbRequest(
            columns=columns, table=table, condition=condition, db_host=self.dbHost))

    def insert(self, table: str, columns: str, values: str) -> api.InsertDbResponse:
        return self.stub.InsertDb(api.InsertDbRequest(
            table=table, columns=columns, values=values, db_host=self.dbHost))

    def delete(self, table : str, condition : str) -> api.DeleteDbResponse:
        return self.stub.DeleteDb(api.DeleteDbRequest(
            table=table, condition=condition, db_host=self.dbHost))
    

def run(host):

    db = Database(host)
    
    print(db.get(columns="*", table=TB, condition="WHERE url='Hello'", db_host=DB_HOST))


if __name__ == "__main__":
    host = sys.argv[1].split('=')[1] # localhost:808...
    print(host)
    run(host)