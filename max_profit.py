# max_profit.py
from typing import Tuple, List

def max_profit_schedule_with_tiebreak(n: int) -> Tuple[int, int, int, int]:
    """
    Returns (best_profit, count_T, count_P, count_C)
    Prefers schedules with more T, then P, then C when profits tie.
    """
    # Step 1: building definitions
    types = [
        ("T", 5, 1500),
        ("P", 4, 1000),
        ("C", 10, 2000),
    ]
    
    # Step 2: DP initialization
    NEG = -10**30
    dp = [NEG] * (n + 1)
    dp_counts: List[Tuple[int,int,int] or None] = [None] * (n + 1)
    parent = [None] * (n + 1)  # optional

    dp[0] = 0
    dp_counts[0] = (0, 0, 0)

    # Step 3: DP transitions
    for t in range(0, n + 1):
        if dp[t] == NEG:
            continue
        for i, (_, build_time, revenue) in enumerate(types):
            new_t = t + build_time
            if new_t > n:
                continue

            gain = (n - new_t) * revenue
            cand_profit = dp[t] + gain

            prev_counts = dp_counts[t]
            cand_counts = list(prev_counts)
            cand_counts[i] += 1
            cand_counts_tup = tuple(cand_counts)

            # update decision with tie-breaking
            if dp[new_t] == NEG:
                should_update = True
            elif cand_profit > dp[new_t]:
                should_update = True
            elif cand_profit < dp[new_t]:
                should_update = False
            else:
                existing_counts = dp_counts[new_t]
                should_update = cand_counts_tup > existing_counts

            if should_update:
                dp[new_t] = cand_profit
                dp_counts[new_t] = cand_counts_tup
                parent[new_t] = (t, i)

    # Step 4: extract best profit and counts
    best_profit = max(dp)
    best_t = dp.index(best_profit)
    best_counts = dp_counts[best_t] if dp_counts[best_t] is not None else (0, 0, 0)
    count_T, count_P, count_C = best_counts
    return int(best_profit), count_T, count_P, count_C


# ------------------------------
# CLEAN MAIN EXECUTION (NO TEST CASES)
# ------------------------------
if __name__ == "__main__":
    n_input = int(input("Enter total time units (n): ").strip())
    profit, t_count, p_count, c_count = max_profit_schedule_with_tiebreak(n_input)

    print(f"\nBest for n = {n_input}:")
    print(f"Earnings: ${profit}")
    print(f"T: {t_count} P: {p_count} C: {c_count}")















