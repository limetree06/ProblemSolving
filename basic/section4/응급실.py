import sys

""" 
메디컬 병원 응급실에는 의사가 한 명밖에 없습니다.
응급실은 환자가 도착한 순서대로 진료를 합니다. 하지만 위험도가 높은 환자는 빨리 응급조 치를 의사가 해야 합니다. 이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정합니다.
• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로
다시 넣습니다. 그렇지 않으면 진료를 받습니다.
현재 N명의 환자가 대기목록에 있습니다.
N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료 를 받는지 출력하는 프로그램을 작성하세요.
대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.
"""


def emergency(degree, M):
    count = 0

    while degree:
        max_value = max(degree)
        patient = degree.pop(0)
        if patient == max_value:
            count += 1
            if M == 0:
                break
        else:
            degree.append(patient)

        if M == 0:
            M = len(degree) - 1
        else:
            M -= 1
    return count


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    risk_degree = list(map(int, input().split()))
    result = emergency(risk_degree, M)

    print(result)
