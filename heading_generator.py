def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('greeting', '1'))
print(heading_generator('hi there', '3'))