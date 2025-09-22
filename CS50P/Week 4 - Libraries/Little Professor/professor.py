import random

PROBLEM_NUM = 10
ATTEMPT = 3

def main():
    stage, score = 0, 0
    level = get_level()
    nums = generate_integer(level)

    while stage < PROBLEM_NUM:
        x , y = nums[stage * 2], nums[stage * 2 + 1]
        answer = x + y
        attempt = 1
        while attempt <= ATTEMPT:
            try:
                user_a = int(input(f"{x} + {y} = "))
                if user_a != answer:
                    raise ValueError
            except ValueError:
                print("EEE")
                attempt += 1
            else:
                score += 1
                stage += 1
                break
        
        if attempt > ATTEMPT:
            print(f"{x} + {y} = {answer}")
            stage += 1

    print("Score:", score)
def get_level():
    while True:
        try:    
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if  0 < level <= 3:
                return level

def generate_integer(level):
    nums = []

    ranges = {
        1: (0, 9),
        2: (10, 99),
        3: (100, 999)
    }

    min, max = ranges.get(level)

    for _ in range(PROBLEM_NUM * 2):
        nums.append(random.randint(min, max))
    
    return nums
if __name__ == "__main__":
    main()