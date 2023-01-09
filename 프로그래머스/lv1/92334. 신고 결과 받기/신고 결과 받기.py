from collections import defaultdict

def solution(id_list, report, k):
    # 동일한 유저에 대한 신고 횟수는 1회로 처리
    ban = defaultdict(set)
    # k번 이상 신고된 유저는 게시판 이용이 정지 메일 발송
    ban_list = dict.fromkeys(id_list, 0)
    for report_id in report:
        # 피신고자:신고자
        value, key = report_id.split()
        ban[key].add(value)
    for id in id_list:
        if len(list(ban[id])) >= k:
            for i in list(ban[id]):
                ban_list[i] += 1
    return list(ban_list.values())