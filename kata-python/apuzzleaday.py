#!/usr/bin/env python3
"""
A Puzzle A Day - 求解器

本程序求解 "A Puzzle A Day" 日历拼图：
- 9×6 网格棋盘，包含月份、日期（1-31）和星期
- 9 个不同形状的五格/六格拼板
- 目标：用拼板覆盖整个棋盘，只留出当天的月份、日期和星期位置

算法特点：
- 使用位掩码表示棋盘，实现 O(1) 碰撞检测
- 递归回溯 + 剪枝优化
- 预计算所有旋转形态，避免运行时重复计算
- 检测孤立空格，提前剪枝无效状态

使用方法：
    python apuzzleaday.py                  # 求解今天的日期
    python apuzzleaday.py -d 2026-12-25    # 求解指定日期
"""

from datetime import date, datetime
from functools import lru_cache

if __name__ == "__main__":
    import sys

    # 检查 Python 版本（需要 3.2+ 支持 lru_cache）
    if sys.version_info < (3, 2):
        print("错误：需要 Python 3.2 或更高版本")
        sys.exit(1)

# =============================================================================
# 常量定义
# =============================================================================

BOARD_H = 9  # 棋盘行数
BOARD_W = 6  # 棋盘列数

FILE_NAME = "logfile.txt"  # 日志文件，用于保存解

# 星期在棋盘上的位置（行，列）
# 布局：第7行放 MON TUE WED，第8行放 THU FRI SAT SUN
# 索引：0=周一，1=周二，...，6=周日
WD_POS = [(7, 3), (7, 4), (7, 5), (8, 2), (8, 3), (8, 4), (8, 5)]

# =============================================================================
# 拼块定义
# =============================================================================
# 每个拼块用相对于原点的 (行, 列) 坐标列表表示
# 第二个元素是拼块索引（0-8）
#
# 形状图示：
# 拼块1: X..   拼块2: X.   拼块3: XX   拼块4: XX   拼块5: XXX
#       XXX        XX        X.        X.        X..
#       X..        X.        X.        X.        X..
#       X..        X.        X.        X.
#
# 拼块6: X.   拼块7: X.X   拼块8: X..   拼块9: X.
#       XX        XXX       XXX       XX
#       .X        X..       .X.       XX
#       .X                  .X.
#                           .X.

BLOCKS_RAW = [
    ([(0, 0), (1, 0), (1, 1), (1, 2), (2, 0), (3, 0)], 0),  # 拼块1 - 6格
    ([(0, 0), (1, 0), (1, 1), (2, 0), (3, 0), (4, 0)], 1),  # 拼块2 - 6格
    ([(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)], 2),  # 拼块3 - 5格
    ([(0, 0), (0, 1), (1, 0), (2, 0), (3, 0), (4, 0)], 3),  # 拼块4 - 6格
    ([(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0)], 4),  # 拼块5 - 6格
    ([(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)], 5),  # 拼块6 - 5格
    ([(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)], 6),  # 拼块7 - 6格
    ([(0, 0), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)], 7),  # 拼块8 - 6格
    ([(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)], 8),  # 拼块9 - 5格
]


# =============================================================================
# 位掩码工具函数
# =============================================================================

def bit(r, c):
    """
    将二维棋盘坐标转换为位掩码位置。
    
    每个格子 (r, c) 对应 54 位整数中的第 (r * BOARD_W + c) 位。
    使用位运算可以在 O(1) 时间内检测碰撞。
    
    参数:
        r: 行索引 (0-8)
        c: 列索引 (0-5)
    
    返回:
        只有第 (r * BOARD_W + c) 位为 1 的整数
    """
    return 1 << (r * BOARD_W + c)


# =============================================================================
# 拼块变换
# =============================================================================

@lru_cache(maxsize=None)
def rotate(cells_tuple, k):
    """
    将拼块顺时针旋转 90 度 k 次。
    
    旋转公式：(r, c) -> (c, -r - 1)
    旋转后归一化，使左上角格子位于 (0, 0)。
    
    参数:
        cells_tuple: (行, 列) 坐标元组
        k: 旋转次数 (0-3)
    
    返回:
        旋转并归一化后的坐标列表
    """
    cells = list(cells_tuple)
    if k == 0:
        return cells
    res = cells
    for _ in range(k % 4):
        # 应用旋转：(r, c) 变为 (c, -r - 1)
        res = [(c, -r - 1) for r, c in res]
        # 归一化：平移使所有坐标非负
        min_r = min(r for r, _ in res)
        min_c = min(c for _, c in res)
        res = [(r - min_r, c - min_c) for r, c in res]
    return res


@lru_cache(maxsize=None)
def mirror(cells_tuple):
    """
    水平镜像拼块（左右翻转）。
    
    参数:
        cells_tuple: (行, 列) 坐标元组
    
    返回:
        镜像后的坐标列表
    """
    cells = list(cells_tuple)
    max_c = max(c for _, c in cells)
    return [(r, max_c - c) for r, c in cells]


@lru_cache(maxsize=None)
def get_variants(cells_tuple):
    """
    生成拼块的所有唯一旋转形态。
    
    生成 8 种形态：原形的 4 种旋转 + 镜像的 4 种旋转。
    对于对称拼块，会自动去重。
    
    参数:
        cells_tuple: (行, 列) 坐标元组
    
    返回:
        唯一坐标元组的列表（每个已归一化并排序）
    """
    variants = []
    for i in range(4):
        # 原形旋转
        variants.append(tuple(sorted(rotate(cells_tuple, i))))
        # 镜像旋转
        variants.append(tuple(sorted(rotate(tuple(mirror(cells_tuple)), i))))
    return list(set(variants))


# 模块加载时预计算所有拼块的所有形态
# 每个元素是 (形态列表, 原始拼块索引)
PRECOMPUTED_VARIANTS = [(get_variants(tuple(cells)), idx) for cells, idx in BLOCKS_RAW]

# 按拼块大小排序（大的优先），优化回溯性能
# 这个启发式通过先放置限制性强的拼块来减少搜索空间
PRECOMPUTED_VARIANTS.sort(key=lambda x: -len(x[0][0]))


# =============================================================================
# 棋盘初始化
# =============================================================================

def board_mask(month, day, wd):
    """
    为指定日期创建初始棋盘掩码。
    
    标记三个位置为已占用（设置对应位）：
    1. 月份格子（前两行，月份 1-12）
    2. 日期格子（第 2-7 行，日期 1-31）
    3. 星期格子（最后两行）
    
    棋盘布局：
    第 0-1 行: JAN FEB MAR APR MAY JUN
              JUL AUG SEP OCT NOV DEC
    第 2-7 行: 1   2   3   4   5   6
              7   8   9   10  11  12
              ...（直到 31）
    第 7-8 行: 31          MON TUE WED
                  THU FRI SAT SUN
    
    参数:
        month: 月份 (1-12)
        day: 日期 (1-31)
        wd: 星期索引 (0=周一, ..., 6=周日)
    
    返回:
        设置了三个日期对应位的位掩码
    """
    m = 0
    # 月份位置：前 2 行（索引 0-1），每行 6 列 = 12 个月份
    m |= bit((month - 1) // BOARD_W, (month - 1) % BOARD_W)
    # 日期位置：第 2-7 行，每行 6 列 = 36 个位置
    m |= bit((day - 1) // BOARD_W + 2, (day - 1) % BOARD_W)
    # 星期位置
    r, c = WD_POS[wd]
    m |= bit(r, c)
    return m


# =============================================================================
# 放置操作
# =============================================================================

def can_place(mask, cells, dr, dc):
    """
    检查拼块能否在指定偏移位置放置而不重叠。
    
    参数:
        mask: 当前棋盘位掩码
        cells: 拼块的 (行, 列) 坐标列表
        dr: 行偏移量
        dc: 列偏移量
    
    返回:
        如果放置有效（不越界、不重叠）返回 True，否则 False
    """
    for r, c in cells:
        nr, nc = r + dr, c + dc  # 偏移后的新位置
        # 检查边界
        if nr < 0 or nc < 0 or nr >= BOARD_H or nc >= BOARD_W:
            return False
        # 检查碰撞
        if mask & bit(nr, nc):
            return False
    return True


def place(mask, cells, dr, dc):
    """
    在棋盘上放置拼块，设置掩码中的对应位。
    
    参数:
        mask: 当前棋盘位掩码
        cells: 拼块的 (行, 列) 坐标列表
        dr: 行偏移量
        dc: 列偏移量
    
    返回:
        拼块位置被标记为已占用的新位掩码
    """
    for r, c in cells:
        mask |= bit(r + dr, c + dc)
    return mask


# =============================================================================
# 剪枝启发式
# =============================================================================

def count_empty_neighbors(mask, r, c):
    """
    统计相邻的空格数量。
    
    用于检测孤立的单格，这些格子无法被任何拼块填充。
    
    参数:
        mask: 当前棋盘位掩码
        r: 要检查的行
        c: 要检查的列
    
    返回:
        相邻空格数量（考虑边界后为 0-4）
    """
    count = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < BOARD_H and 0 <= nc < BOARD_W:
            if not (mask & bit(nr, nc)):
                count += 1
    return count


def has_small_enclosure(mask):
    """
    检测棋盘上是否有孤立的单个空格。
    
    剪枝启发式：如果单个空格被已占用格子完全包围（包括棋盘边缘），
    它永远无法被任何拼块填充（最小拼块有 5 格）。
    
    参数:
        mask: 当前棋盘位掩码
    
    返回:
        如果有孤立空格（死胡同）返回 True，否则 False
    """
    for r in range(BOARD_H):
        for c in range(BOARD_W):
            if not (mask & bit(r, c)):  # 格子为空
                empty_neighbors = count_empty_neighbors(mask, r, c)
                if empty_neighbors == 0:
                    return True  # 发现孤立空格
    return False


# =============================================================================
# 求解器
# =============================================================================

def solve(mask, block_idx, placed, remaining_indices):
    """
    递归回溯求解器。
    
    尝试在棋盘上放置所有剩余拼块。使用深度优先搜索和剪枝找到可行解。
    
    算法步骤：
    1. 如果所有拼块都已放置，返回成功
    2. 获取下一个拼块（按大小排序，大的优先）
    3. 尝试所有旋转形态和位置
    4. 对每个有效放置，检查是否产生封闭空间（剪枝）
    5. 递归求解剩余拼块
    
    参数:
        mask: 当前棋盘位掩码
        block_idx: 当前拼块在 remaining_indices 中的索引
        placed: 已成功放置的拼块列表
        remaining_indices: (形态列表, 原始索引) 元组列表
    
    返回:
        (True, 解列表) 如果找到解
        (False, []) 如果此分支无解
    """
    # 基本情况：所有拼块成功放置
    if block_idx == len(remaining_indices):
        return True, placed

    # 获取当前拼块的形态列表和原始索引
    variants_list, orig_idx = remaining_indices[block_idx]

    # 尝试每种旋转形态
    for cells in variants_list:
        # 尝试棋盘上的每个位置
        for dr in range(BOARD_H):
            for dc in range(BOARD_W):
                if can_place(mask, cells, dr, dc):
                    new_mask = place(mask, cells, dr, dc)
                    
                    # 剪枝：如果产生孤立空格则跳过
                    if not has_small_enclosure(new_mask):
                        # 递归求解剩余拼块
                        success, result = solve(
                            new_mask,
                            block_idx + 1,
                            placed + [(cells, dr, dc, orig_idx)],
                            remaining_indices,
                        )
                        if success:
                            return True, result
    
    # 当前拼块无有效放置方式
    return False, []


# =============================================================================
# 输出格式化
# =============================================================================

def to_board(solution, month, day, wd):
    """
    将解转换为可视化棋盘表示。
    
    创建 9×6 网格：
    - 0 = 空格（有效解中不应出现）
    - 1-9 = 拼块编号
    - -1 = 日期标记（月份、日期或星期）
    
    参数:
        solution: (cells, dr, dc, block_idx) 元组列表
        month: 月份 (1-12)
        day: 日期 (1-31)
        wd: 星期索引 (0-6)
    
    返回:
        表示解的 9×6 嵌套列表
    """
    # 初始化空棋盘
    res = [[0] * BOARD_W for _ in range(BOARD_H)]
    
    # 放置每个拼块
    for cells, dr, dc, idx in solution:
        for r, c in cells:
            res[r + dr][c + dc] = idx + 1  # 拼块索引 0-8 变为 1-9
    
    # 用 -1 标记日期位置
    # 月份格子
    m = (month - 1) // BOARD_W
    mc = (month - 1) % BOARD_W
    res[m][mc] = -1
    
    # 日期格子
    d = (day - 1) // BOARD_W + 2
    dc = (day - 1) % BOARD_W
    res[d][dc] = -1
    
    # 星期格子
    wdr, wdc = WD_POS[wd]
    res[wdr][wdc] = -1
    
    return res


def log(arr):
    """
    保存解到日志文件。
    
    参数:
        arr: 棋盘表示（嵌套列表）
    """
    with open(FILE_NAME, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        for row in arr:
            f.write(str(row) + "\n")
        f.write("\n")


# =============================================================================
# 主入口
# =============================================================================

def main(daystr=""):
    """
    主求解函数。
    
    解析日期（或使用今天），生成初始棋盘掩码，求解拼图，输出结果。
    
    参数:
        daystr: YYYY-MM-DD 格式的日期字符串，空则使用今天
    """
    # 获取目标日期
    today = date.today()
    if daystr:
        today = datetime.strptime(daystr, "%Y-%m-%d").date()

    # 创建初始棋盘掩码，标记日期格子
    mask = board_mask(today.month, today.day, today.weekday())
    
    # 求解拼图
    success, solution = solve(mask, 0, [], PRECOMPUTED_VARIANTS)

    if success:
        # 转换为可视化棋盘并输出
        result = to_board(solution, today.month, today.day, today.weekday())
        log(result)
        for row in result:
            print(row)
    else:
        print("无解")


# =============================================================================
# 命令行接口
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A Puzzle A Day 求解器 - 为任意日期找到有效的拼块放置方案"
    )
    parser.add_argument(
        "--date",
        "-d",
        type=str,
        default="",
        help="要求解的日期（格式：YYYY-MM-DD，默认：今天）",
    )
    args = parser.parse_args()
    main(args.date)
