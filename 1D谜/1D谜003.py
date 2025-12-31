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
        raise ValueError("The word is not in the list")
    
    # 计算 t1 = 单词长度
    t1 = len(s)
    
    # 计算 t2 = 最长上升子序列的长度
    # 将单词转换为数字序列（a→0, b→1, ..., z→25）
    nums = [ord(char) - ord('a') for char in s]
    
    # 计算最长递增子序列
    if t1 == 0:
        t2 = 0
    else:
        dp = [1] * t1
        for i in range(t1):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        t2 = max(dp)
    
    # 计算 t3 = 首字母对应的数字（a→0, b→1, ..., z→25）
    t3 = nums[0]
    
    # 计算最终结果
    return t3/27 + (t1/29 + (t2/t1)/29) / 27

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
    return word if len(word) <= 23 else word[:10] + '...' + word[-10:]

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
        top15 = sorted_history[:15]
        for w, _ in top15:
            display_words.append(get_display_word(w))
        
        # 计算所有显示单词的最大长度
        max_display_len = max(len(dw) for dw in display_words)
        
        # 输出固定行
        fixed_tabs = get_tab_count(4, max_display_len)  # "????"长度为4
        print("\n[1D Puzzle #3]")
        print("????" + '\t' * fixed_tabs + f"{calc_answer_val:.10f}")
        
        # 输出当前行
        current_display = get_display_word(word)
        current_len = len(current_display)
        current_tabs = get_tab_count(current_len, max_display_len)
        print(current_display + '\t' * current_tabs + f"{current_val:.10f}")
        
        # 计算分隔线长度（数值部分固定12字符）
        separator_length = max_display_len + 12
        if max_display_len <= 7:
            separator_length = 20  # 8+11
        elif max_display_len <= 15:
            separator_length = 28  # 16+11
        else:
            separator_length = 36  # 24+11
        print('-' * separator_length)
        
        # 输出top10
        for w, val in top15:
            dw = get_display_word(w)
            dw_len = len(dw)
            tabs = get_tab_count(dw_len, max_display_len)
            print(dw + '\t' * tabs + f"{val:.10f}")

    print(f"\nYou win!\n\n???? = {answer}")
    input()
