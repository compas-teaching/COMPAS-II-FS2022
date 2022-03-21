from compas_fab.backends import RosClient

# With context manager
with RosClient("localhost") as client:
    print("Connected:", client.is_connected)

# Without context manager
# client = RosClient("localhost")
# try:
#     client.run()
#     print("Connected:", client.is_connected)
# except:
#     pass
# finally:
#     if client:
#         client.close()