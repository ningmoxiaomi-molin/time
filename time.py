# 导入库
import time
import tkinter

# 创建窗口
window = tkinter.Tk()
window.title("专注时钟")
window.geometry("300x200")

# 创建标签
label = tkinter.Label(window, text="开始专注吧！", font=("Arial", 20))
label.pack()

# 创建按钮
def start():
    # 设置工作时间和休息时间（单位为秒）
    work_time = 25 * 60
    rest_time = 5 * 60
    # 开始工作循环
    while True:
        # 显示工作倒计时
        label.config(text="工作中...", fg="green")
        while work_time > 0:
            # 格式化时间字符串
            mins, secs = divmod(work_time, 60)
            time_str = "{:02d}:{:02d}".format(mins, secs)
            # 更新标签内容
            label.config(text=time_str)
            # 刷新窗口
            window.update()
            # 暂停一秒
            time.sleep(1)
            # 减少工作时间
            work_time -= 1
        # 显示休息倒计时
        label.config(text="休息中...", fg="red")
        while rest_time > 0:
            # 格式化时间字符串
            mins, secs = divmod(rest_time, 60)
            time_str = "{:02d}:{:02d}".format(mins, secs)
            # 更新标签内容
            label.config(text=time_str)
            # 刷新窗口
            window.update()
            # 暂停一秒
            time.sleep(1)
            # 减少休息时间
            rest_time -= 1
        # 重置工作时间和休息时间
        work_time = 25 * 60
        rest_time = 5 * 60

# 创建开始按钮，并绑定start函数
button = tkinter.Button(window, text="开始", command=start)
button.pack()

# 运行主循环
window.mainloop()
