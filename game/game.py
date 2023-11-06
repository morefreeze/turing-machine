a = [ [201, 798, 204, 796],
    [206, 793, 212, 790],
    [215, 786, 217, 783],
    [220, 781, 223, 779],
    [227, 776, 231, 773],
    [233, 770, 237, 767],
    [244, 765, 251, 759],
    [253, 757, 256, 754],
    [261, 750, 264, 747],
    [267, 744, 270, 742],
    [274, 740, 278, 738],
    [280, 736, 282, 733],
    [286, 729, 288, 725],
    [293, 720, 296, 718],
    [302, 715, 304, 710],
    [309, 708, 312, 704],
    [315, 699, 317, 696],
    [322, 694, 325, 690],
    [329, 687, 331, 684],
    [334, 680, 337, 673],
    [339, 669, 341, 667],
    [346, 664, 348, 662],
    [350, 658, 353, 656],
    [356, 653, 358, 651],
    [360, 649, 365, 647],
    [370, 645, 373, 641],
    [376, 639, 378, 637],
    [381, 635, 385, 633],
    [387, 631, 390, 629],
    [392, 627, 394, 621],
    [396, 617, 401, 615],
    [403, 613, 405, 610],
    [407, 608, 410, 605],
    [413, 599, 416, 597],
    [419, 595, 423, 593],
    [429, 591, 432, 589],
    [434, 587, 437, 585],
    [440, 581, 442, 579],
    [447, 577, 453, 573],
    [455, 571, 459, 567],
    [462, 564, 464, 562],
    [470, 558, 472, 553],
    [475, 550, 479, 547],
    [481, 543, 483, 540],
    [485, 536, 487, 533],
    [491, 530, 495, 527],
    [497, 523, 499, 518],
    [503, 515, 505, 509],
    [507, 506, 514, 504],
    [516, 502, 520, 498],
    [525, 496, 528, 492],
    [532, 490, 534, 486],
    [537, 484, 541, 482],
    [546, 480, 549, 476],
    [551, 474, 557, 471],
    [560, 469, 563, 463],
    [566, 461, 568, 458],
    [572, 454, 576, 449],
    [578, 445, 580, 441],
    [582, 439, 586, 435],
    [588, 433, 590, 430],
    [592, 424, 594, 421],
    [596, 418, 598, 414],
    [604, 412, 606, 409],
    [609, 406, 611, 404],
    [614, 402, 616, 399],
    [618, 395, 625, 393],
    [628, 391, 630, 391],
    [632, 386, 634, 382],
    [636, 379, 638, 377],
    [640, 374, 643, 372],
    [646, 369, 648, 362],
    [650, 359, 652, 357],
    [654, 355, 657, 352],
    [661, 349, 663, 347],
    [665, 344, 668, 340],
    [670, 338, 677, 335],
    [681, 332, 686, 330],
    [688, 327, 691, 324],
    [695, 319, 697, 316],
    [701, 314, 706, 311],
    [709, 308, 714, 303],
    [717, 299, 719, 294],
    [723, 289, 726, 287],
    [737, 279, 739, 277],
    [741, 273, 743, 268],
    [746, 266, 749, 263],
    [751, 257, 755, 255],
    [758, 252, 763, 247],
    [766, 243, 769, 236],
    [771, 232, 775, 228],
    [778, 224, 780, 221],
    [782, 219, 785, 216],
    [787, 213, 792, 207],
    [795, 205, 797, 202],]
chk_idx = [46, 73, 92, 34, 37, 29, 41, 22, 77, 39, 79, 89, 59, 44, 52, 32, 74, 2, 24, 40, 0, 72, 93, 3, 0, 27, 28, 56, 0, 57, 85, 84, 66, 8, 80, 95, 91, 69, 63, 14, 18, 75, 19, 65, 71, 48, 51, 53, 67, 25, 4, 62, 6, 88, 17, 9, 86, 50, 47, 21, 33, 12, 45, 26, 15, 78, 20, 11, 23, 16, 87, 49, 92, 29, 31, 38, 77, 94, 46, 61, 7, 34, 41, 54, 68, 39, 1, 73, 35, 36, 37, 22, 42, 89, 59, 44, 52, 32, 74, 70, 58, 43, 76, 90, 0, 60, 13, 55, 81, 30, 5, 88, 10, 64, 46, 73, 61, 35, 7, 36, 92, 34, 37, 29, 41, 22, 31, 54, 42, 38, 68, 82, 77, 39, 79, 94, 1, 83, 63, 14, 18, 75, 19, 65, 57, 85, 84, 66, 8, 80, 84, 85, 57, 95, 91, 69, 2, 24, 40, 72, 93, 3, 72, 93, 3, 27, 28, 56, 2, 24, 40, 27, 28, 56, 57, 85, 84, 66, 8, 80, 95, 91, 69]

from collections import defaultdict, Counter
from itertools import permutations
import math

def only_one_one(x):
    return x != 0 and x & (x-1) == 0

def gen_code(b,y,p):
    return (b-1)*25+(y-1)*5+(p-1)

def dec_code(x):
    blue = x // 25 + 1
    yellow = (x // 5) % 5 + 1
    purple = x % 5 + 1
    return blue, yellow, purple

# for x in loop_code(res[19][0] & res[17][0] & res[18][0]):
#     print(x, dec_code(int(math.log2(x))))
def loop_code(x):
    while x > 0:
        res = x - (x & (x-1))
        yield res
        x -= res

def count_same(b,y,p):
    if b==y==p:
        return 3
    return 2 if b==y or y==p or p==b else 0
def count_order(b,y,p):
    if b<y<p:
        return -1
    return 1 if b>y>p else 0
def count_asc(b,y,p):
    if y-b==1 and p-y==1:
        return 3
    if y-b==1 or p-y==1:
        return 2
    return 0
def count_desc(b,y,p):
    if b-y==1 and y-p==1:
        return 3
    if b-y==1 or y-p==1:
        return 2
    return 0
def count_num(b,y,p, num):
    return sum([x==num for x in [b,y,p]])

criteria = [
    [lambda b,y,p: b==1, lambda b,y,p: b>1],
    [lambda b,y,p: b < 3, lambda b,y,p: b == 3, lambda b,y,p: b > 3],
    [lambda b,y,p: y < 3, lambda b,y,p: y == 3, lambda b,y,p: y > 3],
    [lambda b,y,p: y < 4, lambda b,y,p: y == 4, lambda b,y,p: y > 4],
    [lambda b,y,p: b % 2 == 0, lambda b,y,p: b % 2 == 1],
    # 5
    [lambda b,y,p: y % 2 == 0, lambda b,y,p: y % 2 == 1],
    [lambda b,y,p: p % 2 == 0, lambda b,y,p: p % 2 == 1],
    [lambda b,y,p: count_num(b,y,p, 1) == 0, lambda b,y,p: count_num(b,y,p, 1) == 1, lambda b,y,p: count_num(b,y,p, 1) == 2, lambda b,y,p: count_num(b,y,p, 1) == 3, ],
    [lambda b,y,p: count_num(b,y,p, 3) == 0, lambda b,y,p: count_num(b,y,p, 3) == 1, lambda b,y,p: count_num(b,y,p, 3) == 2, lambda b,y,p: count_num(b,y,p, 3) == 3, ],
    [lambda b,y,p: count_num(b,y,p, 4) == 0, lambda b,y,p: count_num(b,y,p, 4) == 1, lambda b,y,p: count_num(b,y,p, 4) == 2, lambda b,y,p: count_num(b,y,p, 4) == 3, ],
    # 10 above
    [lambda b,y,p: b<y, lambda b,y,p: b==y, lambda b,y,p: b>y],
    [lambda b,y,p: b<p, lambda b,y,p: b==p, lambda b,y,p: b>p],
    [lambda b,y,p: y<p, lambda b,y,p: y==p, lambda b,y,p: y>p],
    [lambda b,y,p: b<y and b<p, lambda b,y,p: y<b and y<p, lambda b,y,p: p<b and p<y],
    [lambda b,y,p: b>y and b>p, lambda b,y,p: y>b and y>p, lambda b,y,p: p>b and p>y],
    # 15 above
    [lambda b,y,p: sum([x%2 for x in[b,y,p]]) < 2, lambda b,y,p: sum([x%2 for x in[b,y,p]]) >= 2],
    [lambda b,y,p: sum([x%2 for x in[b,y,p]]) == 3, lambda b,y,p: sum([x%2 for x in[b,y,p]]) == 2, lambda b,y,p: sum([x%2 for x in[b,y,p]]) == 1, lambda b,y,p: sum([x%2 for x in[b,y,p]]) == 0],
    [lambda b,y,p: sum([b,y,p]) % 2 == 0, lambda b,y,p: sum([b,y,p]) % 2 == 1],
    [lambda b,y,p: b+y<6, lambda b,y,p: b+y==6, lambda b,y,p: b+y>6],
    [lambda b,y,p: count_same(b,y,p)==3, lambda b,y,p: count_same(b,y,p)==2, lambda b,y,p: count_same(b,y,p)==0],
    # 20 above
    [lambda b,y,p: count_same(b,y,p)!=2, lambda b,y,p: count_same(b,y,p)==2],
    [lambda b,y,p: count_order(b,y,p)==-1, lambda b,y,p: count_order(b,y,p)==1, lambda b,y,p: count_order(b,y,p)==0],
    [lambda b,y,p: sum([b,y,p])<6, lambda b,y,p: sum([b,y,p])==6, lambda b,y,p: sum([b,y,p])>6],
    [lambda b,y,p: count_asc(b,y,p)==3, lambda b,y,p: count_asc(b,y,p)==2, lambda b,y,p: count_asc(b,y,p)==0],
    [lambda b,y,p: count_asc(b,y,p)==0 and count_desc(b,y,p)==0, lambda b,y,p: count_asc(b,y,p)==2 or count_desc(b,y,p)==2, lambda b,y,p: count_asc(b,y,p)==3 or count_desc(b,y,p)==3],
    # 25
    [lambda b,y,p: b<3, lambda b,y,p: y<3, lambda b,y,p: p<3],
    [lambda b,y,p: b<4, lambda b,y,p: y<4, lambda b,y,p: p<4],
    [lambda b,y,p: b==1, lambda b,y,p: y==1, lambda b,y,p: p==1],
    [lambda b,y,p: b==3, lambda b,y,p: y==3, lambda b,y,p: p==3],
    [lambda b,y,p: b==4, lambda b,y,p: y==4, lambda b,y,p: p==4],
    # 30
    [lambda b,y,p: b>1, lambda b,y,p: y>1, lambda b,y,p: p>1],
    [lambda b,y,p: b>3, lambda b,y,p: y>3, lambda b,y,p: p>3],
    [lambda b,y,p: b%2==0, lambda b,y,p: b%2==1, lambda b,y,p: y%2==0, lambda b,y,p: y%2==1, lambda b,y,p: p%2==0, lambda b,y,p: p%2==1],
    [lambda b,y,p: b<=y and b<=p, lambda b,y,p: y<=b and y<=p, lambda b,y,p: p<=b and p<=y],
    [lambda b,y,p: b>=y and b>=p, lambda b,y,p: y>=b and y>=p, lambda b,y,p: p>=b and p>=y],
    # 35
    [lambda b,y,p: sum([b,y,p])%3==0, lambda b,y,p: sum([b,y,p])%4==0, lambda b,y,p: sum([b,y,p])%5==0],
    [lambda b,y,p: b+y==4, lambda b,y,p: b+p==4, lambda b,y,p: y+p==4],
    [lambda b,y,p: b+y==6, lambda b,y,p: b+p==6, lambda b,y,p: y+p==6],
    [lambda b,y,p: b==1, lambda b,y,p: b>1, lambda b,y,p: y==1, lambda b,y,p: y>1, lambda b,y,p: p==1, lambda b,y,p: p>1],
    [lambda b,y,p: b<3, lambda b,y,p: b==3, lambda b,y,p: b>3, lambda b,y,p: y<3, lambda b,y,p: y==3, lambda b,y,p: y>3, lambda b,y,p: p<3, lambda b,y,p: p==3, lambda b,y,p: p>3],
    # 40
    [lambda b,y,p: b<4, lambda b,y,p: b==4, lambda b,y,p: b>4, lambda b,y,p: y<4, lambda b,y,p: y==4, lambda b,y,p: y>4, lambda b,y,p: p<4, lambda b,y,p: p==4, lambda b,y,p: p>4],
    [lambda b,y,p: b<y and b<p, lambda b,y,p: b>y and b>p, lambda b,y,p: y<b and y<p, lambda b,y,p: y>b and y>p, lambda b,y,p: p<b and p<y, lambda b,y,p: p>b and p>y],
    [lambda b,y,p: b<y, lambda b,y,p: b<p, lambda b,y,p: b==y, lambda b,y,p: b==p, lambda b,y,p: b>y, lambda b,y,p: b>p],
    [lambda b,y,p: y<b, lambda b,y,p: y<p, lambda b,y,p: y==b, lambda b,y,p: y==p, lambda b,y,p: y>b, lambda b,y,p: y>p],
    [lambda b,y,p: count_num(b,y,p, 1)==0, lambda b,y,p: count_num(b,y,p, 1)==1, lambda b,y,p: count_num(b,y,p, 1)==2, lambda b,y,p: count_num(b,y,p, 3)==0, lambda b,y,p: count_num(b,y,p, 3)==1, lambda b,y,p: count_num(b,y,p, 3)==2, ],
    # 45
    [lambda b,y,p: count_num(b,y,p, 3)==0, lambda b,y,p: count_num(b,y,p, 3)==1, lambda b,y,p: count_num(b,y,p, 3)==2, lambda b,y,p: count_num(b,y,p, 4)==0, lambda b,y,p: count_num(b,y,p, 4)==1, lambda b,y,p: count_num(b,y,p, 4)==2, ],
    [lambda b,y,p: count_num(b,y,p, 1)==0, lambda b,y,p: count_num(b,y,p, 1)==1, lambda b,y,p: count_num(b,y,p, 1)==2, lambda b,y,p: count_num(b,y,p, 4)==0, lambda b,y,p: count_num(b,y,p, 4)==1, lambda b,y,p: count_num(b,y,p, 4)==2, ],
    [lambda b,y,p: b<y, lambda b,y,p: b==y, lambda b,y,p: b>y, lambda b,y,p: b<p, lambda b,y,p: b==p, lambda b,y,p: b>p, lambda b,y,p: y<p, lambda b,y,p: y==p, lambda b,y,p: y>p],
    # 48
]

def every_criteria_useful(sol):
    for cris in permutations(sol, len(sol)):
        bitset = (1<<125)-1
        for cri_no, cond_no in cris[:-1]:
            bitset &= res[cri_no-1][cond_no]
            if only_one_one(res[cri_no-1][cond_no]) or only_one_one(bitset):
                print(f'bad at {cri_no} {cond_no}, {cris}')
                return False
    return True

res = defaultdict(lambda: defaultdict(int))
for i, cri in enumerate(criteria):
    for j, cond in enumerate(cri):
        bitset = 0
        for code in range(125):
            blue = code // 25 + 1
            yellow = (code // 5) % 5 + 1
            purple = code % 5 + 1
            bitset |= int(cond(blue, yellow, purple)) << code
        res[i][j] = bitset

def dfs(cris, all_sol, sol=None, idx=0, bitset=(1<<125)-1):
    if bitset == 0:
        return False
    if idx == len(cris):
        if bitset & (bitset-1) == 0 and every_criteria_useful(sol):
            answer = dec_code(int(math.log2(bitset)))
            all_sol.append((sol[:], answer))
            print('solve!', sol, answer)
        return
    for j, b in res[cris[idx]-1].items():
        new_sol = sol[:] if sol is not None else []
        new_sol.append((cris[idx], j))
        new_bitset = bitset & b
        dfs(cris, all_sol, new_sol, idx+1, bitset & b)

res_arr = []
res_st = {0:0}
for i, v in res.items():
    res_st[i+1] = res_st[i] + len(v)
    res_arr.extend(v.values())

def find_real_cond(cri_no:int, sec_code:int)->(int, int, int):
    for i in range(res_st[cri_no-1], res_st[cri_no]):
        if sec_code in a[chk_idx[i]-1]:
            return i, cri_no, i-res_st[cri_no-1]    # abs_cri_no, cri_no, cond_no
    return res_st[cri_no-1], cri_no, -1 # -1 mean not found
            
import inspect
def my_getsource(cri_no, cond_no):
    code = inspect.getsource(criteria[cri_no-1][0])
    if cond_no == -1:
        return code
    return code.split('lambda b,y,p: ')[cond_no+1].strip(', \n]')

def gen_valid_puzzle():
    from itertools import combinations
    cri_cnt = 4
    max_cri = 22 # [1, max_cri] inclusive
    sol_stat = []
    for cris in combinations(range(1, max_cri + 1), cri_cnt):
        all_sol = []
        dfs(cris, all_sol)
        if len(all_sol) == 0:
            continue
        sol_stat.append({'cris': cris, 'sols': all_sol, 'len': len(all_sol)})
    return sol_stat

def gen_zero_moves():
    sol_stat = gen_valid_puzzle()
    return [x['cris'] for x in sol_stat if x['len']==1]

if __name__ == '__main__':
    my_cris = [4, 5, 8, 22]
    my_sec_code = [0]*len(my_cris)
    all_sol = []
    dfs(my_cris, all_sol)
    print('='*10, 'criteria', '='*10)
    cri_cond = []
    for cri_no, sec_code in zip(my_cris, my_sec_code):
        _, cri_no, cond_no = find_real_cond(cri_no, sec_code)
        cri_cond.append((cri_no, cond_no))
        print(cri_no, my_getsource(cri_no, cond_no))
    print('='*10, 'answer', '='*10)
    for (sol, answer) in all_sol:
        if cri_cond == sol:
            print(answer)
            break