import tkinter as tk
from PIL import ImageTk,Image
import  random
import pygame
pygame.mixer.init()
class EndWindow() :
    def __init__(self,total) :
        self.total=total
        self.end_window=tk.Tk()
        self.end_window.title('END_WINDOW')
        self.end_window.geometry('2000x2000')
        self.end_window.configure(bg='maroon')
        self.end_frame=tk.Frame(self.end_window,width=2000,height=2000)
        self.end_frame.pack()
        self.end_image=Image.open("end window bg.jpg")
        self.end_photo=ImageTk.PhotoImage(self.end_image)
        self.end_wall=tk.Label(self.end_frame,image=self.end_photo)
        self.end_wall.place(x=10,y=10)
    
        self.gameover_label=tk.Label(self.end_window,text=f'GAME OVER !\n YOUR SCORE IS : {self.total}',fg='magenta',bg='black',font=('Helvetica',40,'bold'))
        self.gameover_label.place(x=500,y=350)
        self.exit_game_button=tk.Button(self.end_window,text="EXIT",fg='magenta',bg='black',font=('Algerian',40,'bold'),command=self.exit_game)
        self.exit_game_button.place(x=700,y=550)
        

    def exit_game(self):
        pygame.mixer.music.stop()
        self.end_window.destroy()

 



class GameWindow :
    def __init__(self) :
        self.game_window=tk.Tk()
        self.game_window.geometry("2000x2000")
        self.game_frame=tk.Frame(self.game_window,width=1500,height=1500)
        self.game_frame.pack()
        self.game_image=Image.open("game background.jpeg")
        self.game_photo=ImageTk.PhotoImage(self.game_image.resize((1500,850),resample=0))
        self.game_wall=tk.Label(self.game_frame,image=self.game_photo)
        self.game_wall.place(x=5,y=5)

        self.one=tk.Label(text='1',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.two=tk.Label(text='2',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.three=tk.Label(text='3',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.four=tk.Label(text='4',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.five=tk.Label(text='5',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.six=tk.Label(text='6',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.one.place(x=120,y=250)
        self.two.place(x=120,y=320)
        self.three.place(x=120,y=390)
        self.four.place(x=120,y=460)
        self.five.place(x=120,y=530)
        self.six.place(x=120,y=600)

        self.one_score=tk.Label(text="0",bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.two_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.three_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.four_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.five_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.six_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.one_score.place(x=180,y=250)
        self.two_score.place(x=180,y=320)
        self.three_score.place(x=180,y=390)
        self.four_score.place(x=180,y=460)
        self.five_score.place(x=180,y=530)
        self.six_score.place(x=180,y=600)

        self.oneb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda : self.add_to_score('1'))
        self.twob=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('2'))
        self.threeb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('3'))
        self.fourb=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('4'))
        self.fiveb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('5'))
        self.sixb=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('6'))
        self.oneb.place(x=230,y=250)
        self.twob.place(x=230,y=320)
        self.threeb.place(x=230,y=390)
        self.fourb.place(x=230,y=460)
        self.fiveb.place(x=230,y=530)
        self.sixb.place(x=230,y=600)

        self.threex=tk.Label(text='  3X  ',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.fourx=tk.Label(text='  4X  ',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.house=tk.Label(text='House ',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.large=tk.Label(text='Large ',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.small=tk.Label(text='Small ',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.yahtzee=tk.Label(text='Yatzy ',bg="dark olive green",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.chance=tk.Label(text='Chance',bg="burlywood3",fg="black",font=("Helvetica",20,"bold"),relief="sunken",padx=8,pady=5)
        self.yahtzee.place(x=500,y=550)
        self.chance.place(x=500,y=610)
        self.threex.place(x=500,y=250)
        self.fourx.place(x=500,y=310)
        self.house.place(x=500,y=370)
        self.large.place(x=500,y=430)
        self.small.place(x=500,y=490)
        self.threex_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.fourx_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.house_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.large_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.small_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.yahtzee_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.chance_score=tk.Label(text='0',bg="white",fg="grey",font=("Helvetica",20,"bold"),relief="sunken",padx=5,pady=2)
        self.threex_score.place(x=620,y=250)
        self.fourx_score.place(x=620,y=310)
        self.house_score.place(x=620,y=370)
        self.large_score.place(x=620,y=430)
        self.small_score.place(x=620,y=490)
        self.yahtzee_score.place(x=620,y=550)
        self.chance_score.place(x=620,y=610)

        self.threexb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('3x'))
        self.fourxb=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('4x'))
        self.houseb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('house'))
        self.largeb=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('large'))
        self.smallb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('small'))
        self.yahtzeeb=tk.Button(text='add',bg="burlywood3",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('yahtzee'))
        self.chanceb=tk.Button(text='add',bg="dark olive green",fg="black",font=("Helvetica",15,"bold"),relief="sunken",padx=8,pady=5,command=lambda :self.add_to_score('chance'))
        self.threexb.place(x=680,y=250)
        self.fourxb.place(x=680,y=310)
        self.houseb.place(x=680,y=370)
        self.largeb.place(x=680,y=430)
        self.smallb.place(x=680,y=490)
        self.yahtzeeb.place(x=680,y=550)
        self.chanceb.place(x=680,y=610)
        

        self.die1=tk.Label(self.game_window)
        self.die2=tk.Label(self.game_window)
        self.die3=tk.Label(self.game_window)
        self.die4=tk.Label(self.game_window)
        self.die5=tk.Label(self.game_window)


        self.total=0
        self.list_of_optionsref=["1","2","3","4","5","6","3x","4x","house","small","large","yahtzee","chance"]
        self.list_of_options=["1","2","3","4","5","6","3x","4x","house","small","large","yahtzee","chance"]
       
        self.higher_case_total=0
        self.possibilities={}

        self.rollcount=0
        self.round=0

        self.quit_button=tk.Button(text="QUIT",fg='red',bg='LemonChiffon4',font=('Algerian',15,'bold'),command=self.quit_game)
        self.quit_button.place(x=1450,y=25)

        self.roll_dice_button=tk.Button(text="ROLL DICE",command=self.roll_dice,font=('Helvetica',15,'bold'),bg='white',fg='LemonChiffon4')
        self.roll_dice_button.place(x=650,y=700)
        self.inst='*********INSTRUCTIONS*********\n'
        self.instructionshead=tk.Label(text=self.inst+"              ROLL THE DICE           ",fg="goldenrod1",bg="RosyBrown4",font="Helvetica 20 bold",padx=10,pady=10)
        self.instructionshead.place(x=900,y=250)
        '''self.instructions=tk.Label(text='                     ROLL THE DICE                    ',fg="goldenrod1",bg="RosyBrown4",font="Helvetica 20 bold",padx=10,pady=10)
        self.instructions.place(x=900,y=300)'''

        self.encouragement=tk.Label(text='GOOD LUCK !',fg="gray2",bg="cyan4",font="Helvetica 20 bold",padx=10,pady=10)
        self.encouragement.place(x=920,y=450)

        self.instructionslist=['ROLL THE DICE ','     CLICK THE FIX BUTTON OF THE       \nDICE YOU WANT TO FIX         ','CLICK THE ADD BUTTON OF THE OPTION\n YOU WANT TO BE ADDED TO YOUR SCORE',"one turn is over.choose","one turn is over.You cannot roll the dice\nwithout adding an option to your score"]
        self.encouragementlist=['     YAHTZEE !    \n wow !you are so lucky','              GOOD LUCK !              ','Hey ! Higher case Total has reached 63.\n YOU GOT BONUS','     GOOD LUCK !     ']
    
        self.restartb=tk.Button(text="RESTART",font=('Algerian',15,'bold'),fg='red',bg='LemonChiffon4',command=self.restart)
        self.restartb.place(x=1300,y=25)

        self.score_upto=tk.Label(text="YOUR SCORE : "+str(self.total),font=('Algerian',35,'bold'),fg='cyan',bg='LemonChiffon4')
        self.score_upto.place(x=920,y=550)

    def restart(self) :
        self.game_window.destroy()
        gamey=GameWindow()
        gamey.game_window.mainloop()

    def calculate_and_display_possibilities(self) :   

        self.possibilities={}

        for i in self.list_of_options :
            self.possibilities[i]=0
        lis=self.lis
        set_lis=set(lis)

        if len(set_lis)==1 :
            for i in range(1,7) :
                if str(i) in self.list_of_options :
                    self.possibilities[str(i)]=(lis.count(i)*i)

            for i in self.list_of_options :
                if i not in ['1','2','3','4','5','6'] :
                        self.possibilities[i]=50

        else :

            if "chance" in self.list_of_options :
                self.possibilities["chance"]=sum(lis)

            for i in range(1,7) :
                if str(i) in self.list_of_options :
                    self.possibilities[str(i)]=(lis.count(i)*i)

                if "3x" in self.list_of_options :
                    if len(set_lis)<=3 :
                        for i in set_lis :
                            if lis.count(i)>=3 :
                                self.possibilities["3x"]=sum(lis)
                                break
                    else :
                        self.possibilities["3x"]=0

                if "4x" in self.list_of_options :
                    if len(set_lis)==2 :
                        for i in set_lis :
                            if lis.count(i)==4 :
                                self.possibilities["4x"]=4*i
                                break
                    else :
                        self.possibilities["4x"]=0

                if 'house' in self.list_of_options :
                    if len(set_lis)==2 and (lis.count(lis[0])==2 or lis.count(lis[0])==3) :
                        self.possibilities['house']=25
                    else :
                        self.possibilities['house']=0

                if "large" in self.list_of_options  :
                    if len(set_lis)==5 :
                        c=0
                        for i in range(0,4) :
                            if sorted(list(set_lis))[i+1]-sorted(list(set_lis))[i]==1 :
                                continue
                            else :
                                c+=1
                        if c==0 :
                            self.possibilities["large"]=40
                        else :
                            self.possibilities['large']=0
                    else :
                        self.possibilities['large']=0

                if 'small' in self.list_of_options :
                    if len(set_lis)>=4 :
                        c=0
                        for i in range(0,3) :
                            if sorted(list(set_lis))[i+1]-sorted(list(set_lis))[i]==1 :
                                continue
                            else :
                                c+=1                       
                        if c==0 :
                            self.possibilities["small"]=30
                        else :
                            self.possibilities['small']=0
                    else :
                        self.possibilities['small']=0

        for i in self.possibilities :
                            if i=='1':
                                self.one_score['text']=str(self.possibilities['1'])
                            if i=='2':
                                self.two_score['text']=str(self.possibilities['2'])
                            if i=='3':
                                self.three_score['text']=str(self.possibilities['3'])
                            if i=='4':
                                self.four_score['text']=str(self.possibilities['4'])
                            if i=='5':
                                self.five_score['text']=str(self.possibilities['5'])
                            if i=='6':
                                self.six_score['text']=str(self.possibilities['6'])
                            if i=='3x':
                                self.threex_score['text']=str(self.possibilities['3x'])
                            if i=='4x':
                                self.fourx_score['text']=str(self.possibilities['4x'])
                            if i=='large':
                                self.large_score['text']=str(self.possibilities['large'])
                            if i=='small':
                                self.small_score['text']=str(self.possibilities['small'])
                            if i=='house':
                                self.house_score['text']=str(self.possibilities['house'])
                            if i=='chance':
                                self.chance_score['text']=str(self.possibilities['chance'])
                            if i=='yahtzee':
                                self.yahtzee_score['text']=str(self.possibilities['yahtzee'])
        if 'yahtzee' in self.list_of_options and self.possibilities['yahtzee']==50 :
            self.encouragement.configure(text=self.encouragementlist[0])
        if list(self.possibilities.values()).count(0)>5 :
            self.encouragement.configure(text=self.encouragementlist[1])
        self.instructionshead.configure(text=self.inst+self.instructionslist[2])

    def add_to_score(self,selected) :
            self.total+=self.possibilities[selected]
            if selected in ['1','2','3','4','5','6'] :
                self.higher_case_total+=self.possibilities[selected]
            if self.higher_case_total>63 :
                self.encouragement.configure(text=self.instructionslist[2])
            if selected=='1' :
                self.oneb.destroy()
                self.one_score.configure(fg='grey')
            if selected=='2' :
                self.twob.destroy()
                self.two_score.configure(fg="grey")
            if selected=='3' :
                self.threeb.destroy()
                self.three_score.configure(fg="grey")
            if selected=='4' :
                self.fourb.destroy()
                self.four_score.configure(fg="grey")
            if selected=='5' :
                self.fiveb.destroy()
                self.five_score.configure(fg="grey")
            if selected=='6' :
                self.sixb.destroy()
                self.six_score.configure(fg="grey")
            if selected=='chance' :
                self.chanceb.destroy()
                self.chance_score.configure(fg="grey")
            if selected=='large' :
                self.largeb.destroy()
                self.large_score.configure(fg="grey")
            if selected=='small' :
                self.smallb.destroy()
                self.small_score.configure(fg="grey")
            if selected=='3x' :
                self.threexb.destroy()
                self.threex_score.configure(fg="grey")
            if selected=='4x' :
                self.fourxb.destroy()
                self.fourx_score.configure(fg="grey")
            if selected=='yahtzee' :
                self.yahtzeeb.destroy()
                self.yahtzee_score.configure(fg="grey")
            if selected=='house' :
                self.houseb.destroy()
                self.house_score.configure(fg="grey")
            self.list_of_options.remove(selected)
            if len(self.list_of_options)==0 :
                self.game_window.destroy()
                game3=EndWindow(self.total)
                game3.end_window.mainloop()
            self.round+=1
            self.score_upto.configure(text='YOUR SCORE : '+str(self.total))
            self.instructionshead.configure(text=self.inst+'ROUND '+str(self.round)+' is over...'+self.instructionslist[0])
            self.rollcount=0


    def roll_dice(self) :
        if self.rollcount==3:
            self.instructionshead.configure(text=self.inst+self.instructionslist[4])
        else:
            self.lis=[]
            for i in range(5) :
                self.lis.append(random.randint(1,6))
            a=0
            for i in range(5) :
                a+=100
                if i==0 :
                    self.ima1=Image.open(f"die{str(self.lis[i])}.png")
                    self.photo1=ImageTk.PhotoImage(self.ima1)
                    self.die1.configure(image=self.photo1)
                    self.die1.place(x=a,y=700)
                    
                elif i==1 :
                    self.ima2=Image.open(f"die{str(self.lis[i])}.png")
                    self.photo2=ImageTk.PhotoImage(self.ima2)
                    self.die2.configure(image=self.photo2)
                    self.die2.place(x=a,y=700)
                    
                elif i==2 :
                    self.ima3=Image.open(f"die{str(self.lis[i])}.png")
                    self.photo3=ImageTk.PhotoImage(self.ima3)
                    self.die3.configure(image=self.photo3)
                    self.die3.place(x=a,y=700)
                   
                elif i==3 :
                    self.ima4=Image.open(f"die{str(self.lis[i])}.png")
                    self.photo4=ImageTk.PhotoImage(self.ima4)
                    self.die4.configure(image=self.photo4)
                    self.die4.place(x=a,y=700)
                    
                elif i==4 :
                    self.ima5=Image.open(f"die{str(self.lis[i])}.png")
                    self.photo5=ImageTk.PhotoImage(self.ima5)
                    self.die5.configure(image=self.photo5)
                    self.die5.place(x=a,y=700)
                           
            self.rollcount+=1
            if self.rollcount==3:
                self.instructionshead.configure(text=self.inst+self.instructionslist[3])
            self.calculate_and_display_possibilities()

    def quit_game(self):
        self.game_window.destroy()
class StartWindow :
    def __init__(self,parent) :

        self.parent=parent
        self.parent.title("YAHTZEE-STARTING-WINDOW")
        self.parent.geometry('2000x2000')
        pygame.mixer.music.load("game window.mp3")
        pygame.mixer.music.play()

        self.canvas=tk.Canvas(self.parent,width=2000,height=2000,bg='dark olive green')
        self.canvas.pack()
        self.headlabel=tk.Label(self.canvas,text='YAHTZEE',font=('Britannic Bold',150,'bold'),bg='dark olive green',fg='wheat3')
        self.headlabel.place(x=700,y=225)
        self.starlabel1=tk.Label(self.canvas,text='**********************',font=('Britannic Bold',60,'bold'),fg='Wheat3',bg='dark olive green')
        self.starlabel1.place(x=710,y=450)
        self.starlabel2=tk.Label(self.canvas,text='**********************',font=('Britannic Bold',60,'bold'),fg='Wheat3',bg='dark olive green')
        self.starlabel2.place(x=710,y=170)


        self.gif=Image.open("dice gif.gif")

        self.frames=[]

        try :
            while True :
                self.frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(len(self.frames))
        except EOFError :
            pass

        self.update(0)

        

        self.start_game_button=tk.Button(self.canvas,text="START THE GAME",fg='Firebrick4',bg='#d4af37',font=('Broadway',35,'bold'),command=self.start_game)
        self.start_game_button.place(x=800,y=580)

    def update(self,index) :
        frame=self.frames[index]
        self.canvas.create_image(300,300,image=frame)
        index+=1
        if index==len(self.frames):
            index=0
        self.parent.after(1,self.update,index)

    def start_game(self) :
        self.parent.destroy()
        game=GameWindow()
        game.game_window.mainloop()


 



if __name__ == "__main__" :
    root=tk.Tk()
    start_window=StartWindow(root)
    root.mainloop()