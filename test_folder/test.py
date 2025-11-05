def fibonacci_generator(n):
    """
    フィボナッチ数列をn個まで1つずつ生成（yield）する
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 実行例：ジェネレータを使って10個の数を表示
print("ジェネレータの実行結果:")
for num in fibonacci_generator(10):
    print(num, end=" ")