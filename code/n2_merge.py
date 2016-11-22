
route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

merged = {}

# least pythonic
for k in query:
    merged[k] = query[k]
for k in post:
    merged[k] = post[k]
for k in route:
    merged[k] = route[k]

print(merged)

# pythonic
merged = {}
merged.update(query)
merged.update(post)
merged.update(route)
print(merged)

# 3.5:
merged = {**query, **post, **route}
print(merged)

process = {
    k
    for k in {**query, **post, **route}
}

