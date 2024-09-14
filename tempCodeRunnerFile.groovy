root = tk.Tk()
root.title("War Card Game")

# 创建 Canvas 画布来显示游戏内容
canvas = tk.Canvas(root, width=400, height=deck_size * 150)
canvas.pack()

# 绘制初始战场
draw_war(canvas, deck_size, 150)

# 按钮来触发更新游戏（比如下一轮攻击）
button = tk.Button(root, text="Next Attack", command=update_game)
button.pack()

root.mainloop()