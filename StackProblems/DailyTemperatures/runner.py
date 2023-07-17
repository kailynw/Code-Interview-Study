def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, temp in enumerate(T):
      while stack and temp >  T[stack[-1]]:
        cur = stack.pop()
        ans[cur] = i - cur
      stack.append(i)

    return ans

if __name__ == "__main__":
    temp_list = [73,74,75,71,69,72,76,73]
    dailyTemperatures(temp_list)