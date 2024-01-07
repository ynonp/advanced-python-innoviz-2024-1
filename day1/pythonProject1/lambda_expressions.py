# return [22, 80]
def open_ports(ip):
    ...


# return [ssh, http]
def service_at_ports(list_of_ports):
    ...

def has_ssh_open(list_of_services):
    return "ssh" in list_of_services

def twice(x):
    print(f"x = {x}, x * 2 = {x * 2}")
    return x * 2

# Map doesn't actually call the function
# but rather returns the potential to call the function
results1 = map(twice, range(10))
results2 = map(lambda x: x * 2, range(10))

# When we NEED the result, only then map will
# call the function
# print(list(results1))
for i in results1:
    print(i)


