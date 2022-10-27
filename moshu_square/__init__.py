class MoshuSquare:
    def __init__(self, values_array):
        """
        Class represntation of a "moshu square"
        :param values_array: # EX values_array =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        self.values_array = values_array
        self.checked_sum = 0

    def check_diag(self) -> bool:
        """
        check diagonal sum

        :return: bool
        """
        ret = True
        diag_count_left = 0
        diag_count_right = 0
        for i in range(0, 3):
            diag_count_left = diag_count_left + self.values_array[i][i]

        for i in range(2, -1, -1):
            diag_count_right = diag_count_right + self.values_array[i][i]

        if (diag_count_left != self.checked_sum) or (diag_count_right != self.checked_sum):
            ret = False

        return ret

    def check_rows(self) -> bool:
        """
        check row sums

        :return: bool
        """
        ret = True
        for row in self.values_array:
            temp_row_sum = sum(row)

            if temp_row_sum != self.checked_sum:
                ret = False

        return ret

    def check_columns(self):
        """
        check column sums

        :return: bool
        """
        ret = True
        for i in range(0, 2):
            temp_col_sum = 0
            for row in self.values_array:
                temp_col_sum = temp_col_sum + row[i]

            if temp_col_sum != self.checked_sum:
                ret = False
        return ret

    def is_moshu(self) -> bool:
        # set the checked sum to the first column
        self.checked_sum = sum(self.values_array[0])
        if self.check_columns() and self.check_rows() and self.check_diag():
            return True
        else:
            return False
