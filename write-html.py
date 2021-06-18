import streamlit as st

f = open('helloworld.html', 'w')
print("hello")
message = """<html>
<head></head>
<body><p>Hello world</p></body>
</html>"""

f.write(message)
f.close()
