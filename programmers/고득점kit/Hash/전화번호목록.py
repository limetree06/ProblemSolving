def solution(phone_book):
    MIN = len(min(phone_book, key=len))
    MAX = len(max(phone_book, key=len))
    
    for length in range(MIN, MAX):
        books = dict()
        for phone in phone_book:
            if len(phone) <= length:
                if phone in books.keys():
                    return False
                else:
                    books[phone] = []

            elif len(phone) > length:
                head = phone[0:length]
                tail = phone[length:]
                if head in books.keys():
                    if tail in books[head] or books[head] == []:
                        return False
                else:
                    books[head] = [tail]
    return True

# 정렬, startwith 코드
# 문제를 풀때 정렬도 한번해보고, 1차적으로 생각해봐야하는게 정렬도 풀수 있는지
# 어떤 방식으로 풀껀지 무작정 코드 풀기 시작하지 말것!
def solution_1(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) -1):
        p1 = phone_book[i]
        p2 = phone_book[i+1]
        if p2.startswith(p1):
            return False
    return True