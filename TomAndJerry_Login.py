import turtle
import time
import random


class MainClass:
    def __init__(self):
        super().__init__()
        print('Yoo')
        # 對遊戲場所取名子
        self.CreatePlayGround()
        # 透過海龜創建開場文字並編輯文字，Login 3s後 清空畫布
        self.CreateLogInWord()
        # 創立Tom 跟 Jerry 的生成位置，透過Random來讓他們隨機生成位置，並註冊及更改Tom&Jerry圖片
        self.Tom_Jerry_Generate()

        # 綁定4個方向的key，並設定Jerry的速度，與放下Tom的筆
        self.BundleDirKey()

        self.start = time.time()
        # 設定讓Tom 一直追著 Jerry跑，是不停的所以寫Loop
        self.KeepGoing()

    def CreatePlayGround(self):
        self.playground = turtle.Screen()

    def CreateLogInWord(self):
        # 透過海龜功能替開場加文字
        self.writer = turtle.Turtle()
        # 讓他改變畫筆的顏色
        self.writer.color('brown')
        # 先隱藏掉
        self.writer.hideturtle()
        # 抬起筆
        self.writer.penup()

        # 走道遊戲中間開始寫字
        self.writer.home()
        self.writer.write("TOM and JERRY", align='center',
                          font=("Comic Sans MS", 50, "bold"))
        # 下方寫一行小字，提醒說準備好就開始
        self.writer.goto(0, -50)
        self.writer.write("READY? 3,2,1,GO!", align='center',
                          font=("Comic Sans MS", 20, "bold"))

        # 讓螢幕等待3s後進入遊戲，需要導入時間工具包
        # 這裡先讓整個螢幕沉睡3s後把整個畫面清空，開始遊戲
        time.sleep(3)
        self.writer.clear()

    def Tom_Jerry_Generate(self):
        # 創建Tom 跟 Jerry兩角色，用兩個小海龜來代表他們兩
        self.Tom = turtle.Turtle()
        self.Jerry = turtle.Turtle()
        # 透過引入的工具包Random來讓他們出現在畫布中的隨機的位置

        # 先把Tom 抬起來，之後讓他出生在隨機位置
        self.Tom.penup()
        self.Tom.goto(random.randint(-200, 200), random.randint(-200, 200))
        # 之後Jerry也是讓他出生在隨機位置
        self.Jerry.penup()
        self.Jerry.goto(random.randint(-200, 200), random.randint(-200, 200))
        # 替換Tom 跟 Jerry 的圖片，不要原始的箭頭形狀，先到網路上抓兩張圖片代表Tom and Jerry
        # 先向遊戲場所註冊我們的這兩張圖片
        self.playground.register_shape('img/Tom.gif')
        self.playground.register_shape('img/Jerry.gif')
        self.Tom.shape('img/Tom.gif')
        self.Jerry.shape('img/Jerry.gif')
        self.TomSpeed = 5

    def BundleDirKey(self):
        self.playground.onkey(self.Jerry_Up, "Up")
        self.playground.onkey(self.Jerry_Down, "Down")
        self.playground.onkey(self.Jerry_Left, "Left")
        self.playground.onkey(self.Jerry_Right, "Right")
        # 讓遊樂場間聽這幾個案件的動向
        self.playground.listen()
        # 讓Jerry等等移動用最快的速度，因此設定為0
        self.Jerry.speed(0)
        # 放下Tom的筆來記錄軌跡，並設定軌跡粗細與顏色
        self.Tom.pendown()
        self.Tom.pensize(3)
        self.Tom.color('blue')

    def GameOver_ShowSecond(self):
        self.Tom.goto(0, 0)
        # Jerry 歸位，並透過Jerry來寫字
        self.Jerry.goto(0, 0)
        self.Jerry.color('brown')
        self.Jerry.write("GAME OVER", align='center',
                         font=("Comic Sans MS", 50, "bold"))
        self.Jerry.goto(0, -50)
        survivedTime = self.end-self.start
        # 透過{ :1.f } 將剪好的秒數取道小數後一位
        self.Jerry.write("YOU SURVIVED {:.1f} SECONDS".format(
            survivedTime), align='center', font=("Comic Sans MS", 20, "bold"))
        self.Jerry.up()
        self.Jerry.goto(50, -70)
        self.Jerry.stamp()
        self.Tom.up()
        self.Tom.goto(-50, -70)
        self.Tom.stamp()
    # Jerry要有 上下左右4個動作，我們需要向遊樂場綁定，將鍵盤上的上下左右綁訂到這4個方法內
    # 設定按下上下鍵後Jerry能做什麼

    def Jerry_Up(self):
        self.Jerry.setheading(90)
        self.Jerry.forward(20)

    def Jerry_Down(self):
        self.Jerry.setheading(270)
        self.Jerry.forward(20)

    def Jerry_Left(self):
        self.Jerry.setheading(180)
        self.Jerry.forward(20)

    def Jerry_Right(self):
        self.Jerry.setheading(0)
        self.Jerry.forward(20)

    def KeepGoing(self):
        while True:
            # 先獲得Tom跟Jerry之間的角度，透過海龜的toward來獲得角度，並讓Tom轉向這角度
            angle = self.Tom.towards(self.Jerry)
            self.Tom.setheading(angle)
            # 讓Tom 往前走，遊戲難度取決Tom的移動速度
            self.TomSpeed += 0.05
            self.Tom.forward(self.TomSpeed)
            print(self.TomSpeed)
            # 如果Tom追到Jerry後遊戲就結束，透過distance來判斷雙方距離，距離小於多少px就結束
            distance = self.Tom.distance(self.Jerry)
            if distance < 10:
                self.end = time.time()
                # 清空螢幕並中斷
                self.playground.clear()
                self.GameOver_ShowSecond()
                break