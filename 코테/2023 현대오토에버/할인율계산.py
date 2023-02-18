import sys
input = sys.stdin.readline

def discount(price, grade, coupon, pay):
    discount_per = 0.3
    if grade > 1:
        discount_per -= 0.05 * grade
    price *= 1 - discount_per
    
    if coupon == 'O':    # 쿠폰 유무
        price *= 0.95
    
    if pay == 'C':  # 현금 결제면
        return int(price * 10) / 10
    else:           # 카드 결제면
        return round(price, 2)
    
n = int(input())
for _ in range(n):
    price, grade, coupon, pay = input().split()
    price = float(price)
    grade = int(grade)
    print("%.2f"%discount(price, grade, coupon, pay))