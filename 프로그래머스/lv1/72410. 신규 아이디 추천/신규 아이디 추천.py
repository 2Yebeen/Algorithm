def solution(id):
    str = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    id = id.lower()
    for i in id:
        if i not in str:
            id = id.replace(i, '')
    while '..' in id:
        id = id.replace('..', '.')
    id = id.strip('.')
    id = 'a' if len(id) == 0 else id[:15]
    id = id.strip('.')
    id = id if len(id) > 2 else id + (id[-1] * (3-len(id)))
    return id
