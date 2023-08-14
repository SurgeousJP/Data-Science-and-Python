# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def adjusted_R2_val(independent_var, dependent_var)
    reg = LinearRegression()
    reg.fit(independent_var, dependent_var)
    r2 = reg.score(independent_var, dependent_var)
    n = independent_var.shape[0]
    p = independent_var.shape[1]
    adjusted_R2 = 1 - (1-r2)*(n-1)/(n-p-1)
    return adjusted_R2