# code by DeepSeek
# adjusted by ZXY

import math

# 从words.txt读取词表
with open("words.txt", "r") as f:
    word_list = {line.strip().lower() for line in f}

def calc(s):
    s = s.lower()
    
    # 验证单词是否在词表中
    if s not in word_list:
        raise ValueError("Not in the word list")
    
    # 计算 t1: 单词的非空真子串在词表中的数量
    t1 = 0
    n = len(s)
    # 遍历所有可能的子串（非空且不等于原单词）
    for length in range(1, n):  # 子串长度从1到n-1
        for start in range(0, n - length + 1):
            substr = s[start:start+length]
            if substr in word_list:
                t1 += 1
    
    # 计算 t2: 首字母按A1Z26转换的结果
    t2 = ord(s[0]) - ord('a') + 1
    
    # 计算 t3: 末字母按A1Z26转换的结果
    t3 = ord(s[-1]) - ord('a') + 1
    
    # 计算最终结果
    return t1 + t2/40 + t3/2000

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
    
    
    # 输入答案
    answer = input("Enter answer: ").lower()
    while answer not in word_list:
        print(f"Error: Not in the word list")
        answer = input("Enter answer: ").lower()
    
    calc_answer_val = calc(answer)
    history = []

    while True:
        word = input("Enter a word: ").lower()
        try:
            current_val = calc(word)
        except ValueError as e:
            print(f"Error: {e}")
            continue
            
        # 检查是否胜利
        if word == answer:
            print(f"\n* You Win! *\n\nThe secret word\n ???? = {answer}")
            break
        elif abs(current_val - calc_answer_val) < 1e-8:  # 浮点数比较容差
            print(f"\n* You Win! *\n\nYour word: {word}\ngets the same number ({calc_answer_val:.4f})\nas the secret word\n    ???? = {answer}")
            break
            
        history.append((word, current_val))

        # 输出标题
        print("\n[1D Puzzle #4]")
        
        # 获取要显示的所有单词（包括固定行、当前行和top20）
        display_words = ["????"]  # 固定行
        display_words.append(get_display_word(word))  # 当前行
        
        # 获取最接近的20个值
        sorted_history = sorted(history, key=lambda x: abs(x[1] - calc_answer_val))
        top20 = sorted_history[:20]
        for w, _ in top20:
            display_words.append(get_display_word(w))
        
        # 计算所有显示单词的最大长度
        max_display_len = max(len(dw) for dw in display_words)
        
        # 输出固定行
        fixed_tabs = get_tab_count(4, max_display_len)  # "????"长度为4
        fixed_line = "????" + '\t' * fixed_tabs + f"{calc_answer_val:8.4f}"
        print(fixed_line)
        
        # 输出当前行
        current_display = get_display_word(word)
        current_len = len(current_display)
        current_tabs = get_tab_count(current_len, max_display_len)
        current_line = current_display + '\t' * current_tabs + f"{current_val:8.4f}"
        print(current_line)
        
        # 计算分隔线长度（数值部分固定8字符）
        if max_display_len <= 7:
            separator_length = 16  # 8+8
        elif max_display_len <= 15:
            separator_length = 24  # 16+8
        else:
            separator_length = 32  # 24+8
        print('-' * separator_length)
        
        # 输出top20
        for w, val in top20:
            dw = get_display_word(w)
            dw_len = len(dw)
            tabs = get_tab_count(dw_len, max_display_len)
            print(dw + '\t' * tabs + f"{val:8.4f}")

    input()
