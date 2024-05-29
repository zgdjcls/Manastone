def main():
    length = 1000
    success_rate_list = [0.6,0.7,0.8,0.9]
    slots_list = range(2,7)
    test_cases = [(rate, slot) for rate in success_rate_list for slot in
                  slots_list]
    # history is used for dynamic programming, history[i][j] represents the probability of j manastones remain on gear after i+1 manastones have been used totally
    # Note: we only calculate the probability before first success for each history[i][j](except j == slot)
    for (rate, slot) in test_cases:
        history = [[0 for _ in range(slot+1)] for _ in range(length)]
        # Initialization for DP
        history[0][0] = 1-rate
        history[0][1] = rate
        # total is used for check the total success rate from 0 to $length, only used for debug
        total = 0
        for i in range(1, length):
            for j in range(slot+1):
                if j == 0:
                    history[i][j] = sum(history[i-1][:slot])*(1-rate)
                else:
                    history[i][j] = history[i-1][j-1] * rate
                if j == slot:
                    total += history[i][j]
        expectation = 0
        for i in range(length):
            expectation += (i+1)*history[i][slot]
        print("success rate:", rate,"slot: ", slot,"expectation: ", expectation)





if __name__ == '__main__':
    main()