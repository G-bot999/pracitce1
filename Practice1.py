"""
1、定义一个函数 generate_numbers(n)，该函数接受一个整数 n 作为参数，并返回一个包含 1 到 n 的所有整数的列表。
2、定义一个函数 filter_even_numbers(numbers)，该函数接受一个整数列表 numbers 作为参数，并返回一个新列表，其中只包含原列表中的偶数。
3、在主程序中，要求用户输入一个正整数 n，然后调用 generate_numbers(n) 函数生成列表，并将生成的列表传递给 filter_even_numbers(numbers) 函数，最后打印出过滤后的偶数列表。
4、使用循环结构（如 for 循环或 while 循环）来实现列表的生成和过滤。
要求：
程序应能够正确处理用户输入，并确保输入的 n 是正整数。
程序应输出过滤后的偶数列表。

提示：
可以使用 range() 函数来生成数字序列。
可以使用 % 运算符来判断一个数是否为偶数。
"""
def generate_number(n):
    number =[]
    for i in range(1,n+1):
        number.append(i)
    return number

def filer_even_number(number):
    even_number =[]
    for num in number:
        if num % 2 ==0:
            even_number.append(num)
    return even_number

if __name__== "__main__":
    n = int(input("请输入一个正整数："))
    if n <= 0:
        print("请输入大于0的整数")
    else:
        number = generate_number(n)
        ber = filer_even_number(number)
        print(f"输入列表为{number},\n偶数列表为{ber}")