import re


def find_ans(line):
    tmp = re.findall(r'（.*）', line)
    if tmp:
        ans = tmp[0][1: -1].strip()
        return ans
    else:
        return ''


def test1():
    file = open('1.txt', 'r', encoding='utf-8')
    ans = ''
    flag = True
    question = ''
    while True:
        line = file.readline()
        if line == '\n' and not flag:
            break
        if line == '\n':
            print(question, ans)
            question = ''
            ans = ''
            flag = False
        else:
            if not ans:
                ans = find_ans(line)
            question = question + line
            flag = True
    file.close()


def test2():
    file = open('6.txt', 'r', encoding='utf-8')
    file2 = open('123.txt', 'w', encoding='utf-8')
    ans = ''
    flag = True
    question = ''
    while True:
        line = file.readline()
        if line == '\n' and not flag:
            break
        if line == '\n':
            file2.writelines(line)
            file2.writelines(ans + '\n')
            question = ''
            ans = ''
            flag = False

        else:
            if not ans:
                tmp = re.findall(r'（.*）', line)
                if tmp:
                    ans = tmp[0][1: -1].strip()
                    line = re.sub(tmp[0], '( )', line)
            question = question + line
            flag = True
            file2.writelines(line)
    file.close()
    file2.close()


def test3():
    file = open(r'{}s.txt'.format(input()), 'r', encoding='utf-8')
    ans_dic = {}
    que_list = []
    n = 0
    question = ''
    while True:
        line = file.readline()
        if line == 'e':
            break
        if line == '\n':
            ans = file.readline()
            ans_dic[n] = ans[0]
            que_list.append(question)
            question = ''
            n += 1
        else:
            question += line
    print(ans_dic)
    print(que_list)
    file.close()

