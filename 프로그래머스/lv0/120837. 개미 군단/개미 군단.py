def solution(hp):
    ant1 = hp // 5
    ant2 = (hp % 5) // 3
    ant3 = (hp % 5) % 3
    return ant1 + ant2 + ant3