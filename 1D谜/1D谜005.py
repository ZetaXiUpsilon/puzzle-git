# by DeepSeek

def load_word_sets():
    """加载words.txt和di_output.txt到内存"""
    # 加载words.txt中的所有单词
    with open('words.txt', 'r') as f:
        word_set = set(line.strip().lower() for line in f if line.strip())
    
    # 加载di_output.txt中的单词及其间隔数
    di_dict = {}
    try:
        with open('di_output.txt', 'r') as f:
            for line in f:
                if line.strip():
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        gap = int(parts[0].strip())
                        word = parts[1].strip().lower()
                        di_dict[word] = gap
    except FileNotFoundError:
        print("警告: di_output.txt文件不存在")
    
    return word_set, di_dict

def main():
    # 预加载单词集
    word_set, di_dict = load_word_sets()
    
    print("单词查询系统已启动。输入'-'退出程序")
    print("=" * 40)
    
    while True:
        # 获取用户输入
        user_input = input("请输入一个单词: ").strip().lower()
        
        # 检查退出条件
        if user_input == "-":
            print("程序已退出")
            break
        
        # 检查是否在words.txt中
        if user_input not in word_set:
            print("单词不在词表中")
            print("-" * 40)
            continue
        
        # 检查是否在di_output中
        if user_input in di_dict:
            print(f"返回值：{di_dict[user_input]}")
        else:
            print("返回值：-1")
        
        print("-" * 40)

if __name__ == "__main__":
    main()
