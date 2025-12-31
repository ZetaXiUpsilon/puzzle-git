# code by DeepSeek
# adjusted by ZXY

def calc(s):
    s = s.lower()
    total = 0.0
    base = 27
    for i, char in enumerate(s):
        if not ('a' <= char <= 'z'):
            raise ValueError(f"Invalid character: {char}")
        num = ord(char) - ord('a') + 1
        total += num / (base ** (i + 1))
    return total

def get_tab_count(display_len, max_display_len):
    """根据显示长度和最大显示长度确定制表符数量"""
    if max_display_len <= 7:
        return 1  # 数值从第8列开始
    elif max_display_len <= 15:
        return 2 if display_len <= 7 else 1  # 数值从第16列开始
    else:
        if display_len <= 7:
            return 3  # 数值从第24列开始
        elif display_len <= 15:
            return 2  # 数值从第24列开始
        else:
            return 1  # 数值从第24列开始

def get_display_word(word):
    """获取显示格式的单词，超过23字符的截断"""
    return word if len(word) <= 23 else word[:20] + '...'

if __name__ == "__main__":
    answer = input("Enter answer: ")
    calc_answer_val = calc(answer)
    history = []

    while True:
        word = input("Enter a word: ")
        if word == answer:
            break

        try:
            current_val = calc(word)
        except ValueError as e:
            print(f"Error: {e}")
            continue
            
        history.append((word, current_val))
        
        # 获取要显示的所有单词（包括固定行、当前行和top10）
        display_words = ["????"]  # 固定行
        display_words.append(get_display_word(word))  # 当前行
        
        # 获取最接近的10个值
        sorted_history = sorted(history, key=lambda x: abs(x[1] - calc_answer_val))
        top10 = sorted_history[:10]
        for w, _ in top10:
            display_words.append(get_display_word(w))
        
        # 计算所有显示单词的最大长度
        max_display_len = max(len(dw) for dw in display_words)
        
        # 输出固定行
        fixed_tabs = get_tab_count(4, max_display_len)  # "????"长度为4
        print("\n[1D Puzzle]")
        print("????" + '\t' * fixed_tabs + f"{calc_answer_val:.10f}")
        
        # 输出当前行
        current_display = get_display_word(word)
        current_len = len(current_display)
        current_tabs = get_tab_count(current_len, max_display_len)
        print(current_display + '\t' * current_tabs + f"{current_val:.10f}")
        
        # 计算分隔线长度（数值部分固定11字符）
        separator_length = max_display_len + 12
        if max_display_len <= 7:
            separator_length = 20  # 8+11
        elif max_display_len <= 15:
            separator_length = 28  # 16+11
        else:
            separator_length = 36  # 24+11
        print('-' * separator_length)
        
        # 输出top10
        for w, val in top10:
            dw = get_display_word(w)
            dw_len = len(dw)
            tabs = get_tab_count(dw_len, max_display_len)
            print(dw + '\t' * tabs + f"{val:.10f}")

    print(f"You win\n???? = {answer}")
    input()
