# main main.py
html_content = """
<html>
  <head>
    <title>Python Output</title>
  </head>
  <body>
    <h1>Hello from GitHub Actions!</h1>
    <p>Workflow test!</p>
  </body>
</html>
"""

with open("output.html", "w") as f:
    f.write(html_content)

print("HTML file generated: output.html")
