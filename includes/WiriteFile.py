def WriteFile(filename, content):
    with open(filename, 'w') as f:
        f.write(content)