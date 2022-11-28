def solution(genres, plays):
    album = {}
    p_album = {}
    answer = []

    # 장르별로 play 횟수
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        album[genre] = album.get(genre, 0) + int(play)

    # play 횟수 내림차순으로 정렬
    play_list = sorted(album.items(), key=lambda x:-x[1])

    # 많이 재생된 장르 순으로 for문 돌리기
    for genre, play in play_list:
        arr=[]
        for idx, (g, p) in enumerate(zip(genres, plays)):
            if g == genre:
                arr.append([p, idx])
        # 조건 2,3 을 고려한 정렬
        arr = sorted(arr,key = lambda x : (x[0],-x[1]), reverse=True)
        for i in range(min(len(arr),2)):
            answer.append(arr[i][1])

    return answer
