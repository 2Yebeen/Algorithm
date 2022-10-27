#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int angle) {
    int answer = 0;

    if (angle > 90)
        answer = (int)(angle / 90) + 2;
    else
        answer = (int)(angle / 90) + 1;
    return answer;
}