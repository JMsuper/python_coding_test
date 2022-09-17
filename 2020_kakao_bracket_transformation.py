
def is_perfect(w):
    stack = []
    for item in list(w):
        if item == "(":
            stack.append(item)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
                continue
            else:
                return False
    if stack:
        return False
    else:
        return True

def separate(w):
    left_bracket_cnt = 0
    right_bracket_cnt = 0 
    idx = 0
    for i in range(len(w)):
        if w[i] == "(":
            left_bracket_cnt += 1
        else:
            right_bracket_cnt += 1
        if left_bracket_cnt == right_bracket_cnt:
            idx = i + 1
            break
    u, v = "", ""
    if idx == len(w):
        u, v = w, ""
    else:
        u, v = w[:idx], w[idx:]
    return u, v

def reverse(w):
    ret = ""
    for item in list(w):
        if item == "(":
            ret += ")"
        else:
            ret += "("
    return ret

def solution(p):
    if p == "":
        return ""
    u, v = separate(p)
    if is_perfect(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])


def main():
    p = "()))((()"
    print(solution(p))

if __name__ == "__main__":
    main()