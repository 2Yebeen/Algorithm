def solution(angle):
    if (1 <= angle <= 89):
        return 1;
    elif (angle == 90):
        return 2;
    elif (90 < angle < 180):
        return 3;
    elif (angle == 180):
        return 4;