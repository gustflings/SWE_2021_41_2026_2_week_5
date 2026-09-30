def isHappy(n):
    a = str(n)
    sum = 0
    t = list()

    while True:
      for i in a:
        sum += int(i)**2

      if sum != 1:
       a = str(sum)
       sum = 0
       if int(a) in t:
        return False
       t.append(int(a))

      else:
       return True


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")
