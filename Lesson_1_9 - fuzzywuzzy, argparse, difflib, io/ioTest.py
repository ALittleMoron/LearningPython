import io

with io.BytesIO(b'Hello, world!') as f:
    print(f.read(5), f.getvalue(), f.getbuffer())


with io.StringIO('Hello, World!') as f:
    print(f.read(5), f.getvalue())
