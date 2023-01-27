
import grpc, sys, json

import grpc_py_database_accessing.api.grpc as api


TB = 'qrcodes_tb'
DB_HOST = 'postgres://postgres:postgres@postgres:5433/postgres'

class Database:

    def __init__(self, host: str, dbHost: str) -> None:
        self.host = host
        self.conn = grpc.insecure_channel(host) 
        self.stub = api.DatabaseStub(self.conn)
        self.dbHost = dbHost
    
    def get(self, columns: str, table: str, condition: str) -> list | str:
        req = self.stub.GetDb(api.GetDbRequest(
            columns=columns, table=table, condition=condition, db_host=self.dbHost))
        if req.status != "ok":
            return [], req.status
        data = json.loads(req.data.decode("utf-8"))
        return data if data else [], req.status

    def insert(self, table: str, columns: str, values: str) -> api.InsertDbResponse:
        return self.stub.InsertDb(api.InsertDbRequest(
            table=table, columns=columns, values=values, db_host=self.dbHost))

    def delete(self, table: str, condition: str) -> api.DeleteDbResponse:
        return self.stub.DeleteDb(api.DeleteDbRequest(
            table=table, condition=condition, db_host=self.dbHost))

    def update(self, table: str, to_set: str, condition: str) -> api.UpdateDbResponse:
        return self.stub.UpdateDb(api.UpdateDbRequest(
            table=table, to_set=to_set, condition=condition, db_host=self.dbHost))
    

def run(host):

    db = Database(host)
    
    print(db.get(columns="*", table=TB, condition="WHERE url='Hello'", db_host=DB_HOST))


if __name__ == "__main__":
    host = sys.argv[1].split('=')[1] # localhost:808...
    print(host)
    run(host)