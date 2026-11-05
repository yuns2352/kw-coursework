# keylogger_solver.py
from __future__ import annotations
import sys

def solve_keylogger(cases: list[str]) -> list[str]:
    out = []
    for s in cases:
        left, right = [], []  # 두 스택
        for ch in s.strip():
            if ch == '<':
                if left:
                    right.append(left.pop())
            elif ch == '>':
                if right:
                    left.append(right.pop())
            elif ch == '-':
                if left:
                    left.pop()
            else:
                left.append(ch)
        # 결과 병합: 왼쪽 그대로 + 오른쪽을 뒤집어서 이어붙임
        left.extend(reversed(right))
        out.append(''.join(left))
    return out

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    if not data:
        sys.exit(0)
    t = int(data[0].strip())
    cases = data[1:1+t]
    for ans in solve_keylogger(cases):
        print(ans)
