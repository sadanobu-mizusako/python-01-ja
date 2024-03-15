import random
def simulate_janken():    
    # 0: グー、1: チョキ、2: パー
    janken2int = {"グー":0, "チョキ":1, "パー":2}
    int2janken = {0:"グー", 1:"チョキ", 2:"パー"}

    pc_int = random.randint(0, 2)
    pc_janken = int2janken[pc_int]

    human_janken = input("あなたの手は（グーorチョキorパー）？: ")
    human_int = janken2int[human_janken]

    result = "あなたの勝ち" if (human_int-pc_int)%3==2 else "あなたの負け" if (human_int-pc_int)%3==1 else "あいこ"

    print("あなたの手は%s、PCの手は%sで、結果は%sです" %(human_janken, pc_janken, result))
    return

simulate_janken()