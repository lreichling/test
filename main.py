from moshu_square import MoshuSquare

def main():
    square_1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    square_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    msq_1 = MoshuSquare(square_1)
    msq_2 = MoshuSquare(square_2)
    print(f"square 1 is moshu: {msq_1.is_moshu()}")
    print(f"square 2 is moshu: {msq_2.is_moshu()}")

if __name__ == "__main__":
    main()
