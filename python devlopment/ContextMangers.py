from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


# with open('some_file', 'w+') as f:
#     f.write('hola!')
#     a=f.read()
#     print(a)