# grpc_py_database_accessing

## Build
- Proto
    ```bash
    make proto
    ```

## Run
```bash
make run
```

## Issues
- At `database_pb2_grpc.py` change import
    ```python
    import api.grpc.database_pb2 as database__pb2
    ```