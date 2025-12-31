# programed by DeepSeek

def is_valid_word(word):
    """检查单词是否恰好只有一对重复字母，其他字母都唯一"""
    from collections import Counter
    char_count = Counter(word)
    
    # 统计出现次数
    count_freq = Counter(char_count.values())
    
    # 必须满足：
    # 1. 恰好有一个字母出现2次
    # 2. 所有其他字母都出现1次
    # 3. 没有出现3次或以上的字母
    return count_freq[2] == 1 and count_freq[1] == len(word) - 2

def calculate_gap(word):
    """计算重复字母之间的间隔数"""
    char_count = {}
    positions = {}
    
    # 记录每个字母的位置
    for idx, char in enumerate(word):
        if char not in positions:
            positions[char] = []
        positions[char].append(idx)
    
    # 找到重复的字母
    for char, pos_list in positions.items():
        if len(pos_list) == 2:
            return pos_list[1] - pos_list[0] - 1
    
    # 如果没有找到重复对（理论上不会发生，因为已经通过is_valid_word检查）
    return 0

def process_words(input_file, output_file):
    """处理单词文件并输出结果"""
    results = []
    
    with open(input_file, 'r') as f:
        words = [line.strip().lower() for line in f if line.strip()]
    
    for word in words:
        if is_valid_word(word):
            gap = calculate_gap(word)
            results.append((gap, word))
    
    # 按间隔数从大到小排序，间隔数相同时按单词字典序排序
    results.sort(key=lambda x: (-x[0], x[1]))
    
    with open(output_file, 'w') as f:
        for gap, word in results:
            f.write(f"{gap}\t{word}\n")

if __name__ == "__main__":
    process_words('words.txt', 'di_output.txt')
