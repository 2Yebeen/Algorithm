from collections import deque

def solution(priorities, location):
    cnt = 0
    ans = 0
    # 중요도
    que = deque(priorities)
    # 문서
    # document = deque('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(priorities)])
    document = deque([0 for _ in range(len(priorities))])
    # 찾는 문서
    # my_doc = document[location]
    document[location] = 1
    
    while document:
        # 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        doc = document.popleft()
        priority = que.popleft()
        # 중요도가 높은 문서가 한 개라도 존재하면 현재 문서를 대기목록의 가장 마지막에 넣습니다.
        # 그렇지 않으면 J를 인쇄합니다.
        if len(que) > 1 and max(que) > priority:
            document.append(doc)
            que.append(priority)
        else:
            # cnt 증가, 찾는 문서의 경우 인쇄 종료
            cnt += 1
            if doc == 1:
                ans = cnt
                break

    return ans

