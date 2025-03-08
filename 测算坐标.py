from turtle import *

# 初始化绘制和文本
goto(0, 0)
write("yours name", True, align="center", font=('宋体', 240, 'normal'))
width(1)

def switchupdown():
    if penup():
        end_fill()
        pendown()
    else:
        up()
        begin_fill()
    # 输出当前画笔坐标
    print(f"({xcor()}, {ycor()})")


# 定义改变颜色的函数
def changecolor():
    global colors
    colors = colors[1:] + colors[:1]
    color(colors[0])
    # 输出当前画笔坐标
    print(f"({xcor()}, {ycor()})")


# 定义主函数
def main():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors = ["red", "green", "blue", "yellow"]
    color(colors[0])
    pendown()

    def onclick_left(x, y):
        goto(x, y)  # 移动画笔到点击位置
        switchupdown()  # 切换画笔状态

    def onclick_middle(x, y):
        goto(x, y)  # 移动画笔到点击位置（虽然中键通常不用于移动）
        changecolor()  # 改变颜色

    def onclick_right(x, y):
        goto(x, y)
        switchupdown()  # 切换画笔状态（或根据需要执行其他操作）

    onscreenclick(onclick_left, 1)  # 左键
    onscreenclick(onclick_middle, 2)  # 中键
    onscreenclick(onclick_right, 3)  # 右键

    # 由于我们已经在函数内部输出了坐标，所以不需要在这里再打印消息
    return "EVENTLOOP"


# 程序入口
if __name__ == "__main__":
    msg = main()
    mainloop()

