s = input()
t = input()
s_h, s_m = map(int, s.split(':'))
t_h, t_m = map(int, t.split(':'))
total_minutes = s_h * 60 + s_m - (t_h * 60 + t_m)
if total_minutes < 0:
    total_minutes += 24 * 60
p_h = total_minutes // 60
p_m = total_minutes % 60
print(f"{p_h:02d}:{p_m:02d}")