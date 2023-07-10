#import tkinter
import customtkinter
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # screen setting
        self.title("Calculator")
        self.geometry("240x360")

        # result and display
        self.display_board = customtkinter.CTkLabel(self, text=".", width=40, height=40,
                                                    font=customtkinter.CTkFont(size=20))
        self.display_board.pack()
        self.number = ""

        self.result_board = customtkinter.CTkLabel(self, text=".", width=40, height=40,
                                                   font=customtkinter.CTkFont(size=20))
        self.result_board.pack()

        # control board
        self.control_board = customtkinter.CTkFrame(self)
        self.control_board.pack()

        # the number button
        self.button0 = customtkinter.CTkButton(self.control_board, text="0",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('0'))
        self.button0.grid(row=3, column=1)
        self.button1 = customtkinter.CTkButton(self.control_board, text="1",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('1'))
        self.button1.grid(row=2, column=0)
        self.button2 = customtkinter.CTkButton(self.control_board, text="2",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('2'))
        self.button2.grid(row=2, column=1)
        self.button3 = customtkinter.CTkButton(self.control_board, text="3",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('3'))
        self.button3.grid(row=2, column=2)
        self.button4 = customtkinter.CTkButton(self.control_board, text="4",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('4'))
        self.button4.grid(row=1, column=0)
        self.button5 = customtkinter.CTkButton(self.control_board, text="5",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('5'))
        self.button5.grid(row=1, column=1)
        self.button6 = customtkinter.CTkButton(self.control_board, text="6",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('6'))
        self.button6.grid(row=1, column=2)
        self.button7 = customtkinter.CTkButton(self.control_board, text="7",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('7'))
        self.button7.grid(row=0, column=0)
        self.button8 = customtkinter.CTkButton(self.control_board, text="8",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('8'))
        self.button8.grid(row=0, column=1)
        self.button9 = customtkinter.CTkButton(self.control_board, text="9",
                                               width=40, height=40,
                                               font=customtkinter.CTkFont(size=20),
                                               command=lambda: self.enter_Num('9'))
        self.button9.grid(row=0, column=2)

        # operators button
        self.button_minus = customtkinter.CTkButton(self.control_board, text="-",
                                                    width=40, height=40,
                                                    font=customtkinter.CTkFont(size=20),
                                                    command=lambda: self.enter_Num('-'))
        self.button_minus.grid(row=0, column=3)
        self.button_plus = customtkinter.CTkButton(self.control_board, text="+",
                                                   width=40, height=40,
                                                   font=customtkinter.CTkFont(size=20),
                                                   command=lambda: self.enter_Num('+'))
        self.button_plus.grid(row=1, column=3)
        self.button_multiple = customtkinter.CTkButton(self.control_board, text="x",
                                                       width=40, height=40,
                                                       font=customtkinter.CTkFont(size=20),
                                                       command=lambda: self.enter_Num('x'))
        self.button_multiple.grid(row=2, column=3)
        self.button_division = customtkinter.CTkButton(self.control_board, text="÷",
                                                       width=40, height=40,
                                                       font=customtkinter.CTkFont(size=20),
                                                       command=lambda: self.enter_Num('÷'))
        self.button_division.grid(row=3, column=3)
        self.button_dot = customtkinter.CTkButton(self.control_board, text=".",
                                                       width=40, height=40,
                                                       font=customtkinter.CTkFont(size=20),
                                                       command=lambda: self.enter_Num('.'))
        self.button_dot.grid(row=3, column=2)
        self.button_remove = customtkinter.CTkButton(self.control_board, text="←",
                                                     width=40, height=40,
                                                     font=customtkinter.CTkFont(size=20),
                                                     command=lambda: self.num_remove())
        self.button_remove.grid(row=3, column=0)
        self.button_root = customtkinter.CTkButton(self.control_board, text="√",
                                                         width=40, height=40,
                                                         font=customtkinter.CTkFont(size=20),
                                                         command=lambda: self.enter_Num('√'))
        self.button_root.grid(row=4, column=0)
        self.button_power = customtkinter.CTkButton(self.control_board, text="^",
                                                         width=40, height=40,
                                                         font=customtkinter.CTkFont(size=20),
                                                         command=lambda: self.enter_Num('^'))
        self.button_power.grid(row=4, column=1)
        self.button_equal = customtkinter.CTkButton(self.control_board, text="=",
                                                       width=40, height=40,
                                                       font=customtkinter.CTkFont(size=20),
                                                       command=lambda: self.calculate())
        self.button_equal.grid(row=4, column=3)
        self.button_percentage = customtkinter.CTkButton(self.control_board, text="%",
                                                  width=40, height=40,
                                                  font=customtkinter.CTkFont(size=20),
                                                  command=lambda: self.enter_Num('%'))
        self.button_percentage.grid(row=4, column=2)

    def enter_Num(self, num):
        # enter the numbers and operators to display label
        self.number += num
        self.display_board.configure(text=self.number)
        return

    def calculate(self):
        lst_operators = ['x', '÷', '+', '^']  # can't appear at the beginning or the end
        lst_operators1 = ['-', "√"]  # can't appear at the end
        lst_operators2 = ['%']  # can't appear at the beginning

        # check the formula start or end by operators
        if self.number[-1] in lst_operators1 or self.number[-1] in lst_operators:
            self.result_board.configure(text=f"Error:\nThe formula should not\nend by {self.number[-1]}.")
            return

        if self.number[0] in lst_operators2 or self.number[0] in lst_operators:
            self.result_board.configure(text=f"Error:\nThe formula should not\nstart by {self.number[0]}.")
            return

        # check if operators next to another operators
        per_operator = -1
        for i in range(len(self.number)):
            if self.number[i] in lst_operators:
                if i - per_operator == 1:
                    self.result_board.configure(text="Error:\nan operator should not\nnext to another operator.")
                    return
                per_operator = i

        if "√-" in self.number:
            self.result_board.configure(text="Error: \"√-\".")
            return

        # find negative num
        for i in range(len(self.number)-1, -1, -1):
            if self.number[i] == '-':
                if i-1 >= 0 and self.number[i-1] not in lst_operators:
                    self.number = self.number[:i] + "+" + self.number[i:]  # insert "+" for single "-"

        # extract the numbers
        print(self.number)
        nums_save = self.number

        nums_save = nums_save.replace('x', '*').replace('÷', '*').\
            replace('+', '*').replace('%', '').replace('√', '').replace('^', '*').split('*')
        nums = [float(i) for i in nums_save]

        # extract the operators
        oper = []
        for i in range(len(self.number)):
            if (self.number[i] in lst_operators
                or self.number[i] in lst_operators1
                or self.number[i] in lst_operators2) \
                    and self.number[i] != '-':
                oper.append(self.number[i])

        # calculate '%'
        for i in range(len(oper) - 1, -1, -1):
            if oper[i] == '%':
                nums[i] /= 100
                oper.pop(i)

        # calculate '√'
        for i in range(len(oper) - 1, -1, -1):
            if oper[i] == '√':
                nums[i] = math.sqrt(nums[i])
                oper.pop(i)

        # calculate '^'
        for i in range(len(oper) - 1, -1, -1):
            if oper[i] == '^':
                nums[i] = nums[i] ** nums.pop(i + 1)
                oper.pop(i)

        # calculate 'x', '÷'
        for i in range(len(oper) - 1, -1, -1):
            if oper[i] == 'x':
                nums[i] *= nums.pop(i + 1)
                oper.pop(i)

            elif oper[i] == '÷':
                nums[i] /= nums.pop(i + 1)
                oper.pop(i)

        # calculate '+'
        for i in range(len(oper) - 1, -1, -1):
            """if oper[i] == '-':
                nums[i] -= nums.pop(i + 1)
                oper.pop(i)"""

            if oper[i] == '+':
                nums[i] += nums.pop(i + 1)
                oper.pop(i)

        # display the result and clear the formula
        self.result_board.configure(text=nums[0])
        self.number = ""
        self.display_board.configure(text=".")
        return

    def num_remove(self):
        # if no value in formula, return
        if self.number == "":
            return

        # delete the last value
        self.number = self.number[:-1]

        # display "." if nothing in formula
        if self.number == "":
            self.display_board.configure(text=".")
            return

        self.display_board.configure(text=self.number)
        return


calculator = Calculator()
calculator.mainloop()
