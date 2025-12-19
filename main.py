import random

def JiaHao():
    responses = [
        "累了",
        "JueJue你",
        "想你了，厚良",
        "逆天",
        "确实",
        "笑死"
    ]
    return random.choice(responses)

def main():
    print("=" * 50)
    print("输入 'quit'  退出家豪")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("你: ")
        
        if user_input.lower() in ['quit']:
            print("睡了")
            break
        
        if not user_input.strip():
            continue
        
        response = JiaHao()
        print(f"家豪: {response}")
        print()

if __name__ == "__main__":
    main()

