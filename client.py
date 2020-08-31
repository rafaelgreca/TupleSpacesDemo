from xmlrpc.client import ServerProxy

server = ServerProxy("http://189.84.197.211:8000", allow_none=True)

response = server.tuple_space_out(("teste", 1))
print(response)
response = server.tuple_space_out(("teste2", 2))
print(response)
response = server.tuple_space_out(("teste3", 3))
print(response)
response = server.tuple_space_rt(("teste2", 2))
print(response)
response = server.tuple_space_all()
print(response)

# response = server.tuple_space_rd()
# print(response)