# == = is, != = is not? not is?
#https://smoothiecoding.kr/python-tkinter-installation/
#https://wikidocs.net/132610
#https://www.delftstack.com/ko/tutorial/tkinter-tutorial/tkinter-message-box/

#https://m.blog.naver.com/noorol/221037083349
#https://sksstar.tistory.com/176

#https://hyoje420.tistory.com/48

#https://gomguard.tistory.com/125

#https://076923.github.io/posts/Python-tkinter-23/

#https://blog.naver.com/heesupark92/220736209269
import random, time, io, platform, tkinter, sys;
from tkinter import ttk, messagebox;
#항상 def마다 글로벌 선언, def는 항상 맨앞
#global 다음 try 주의
fullver = "v1.9.58-321";
ver = 9;
winver = "10.0.17763";
window1_size = "480x240";#메인
window2_size = "480x240";#타자수
window3_size = "480x240";#연습시작
window0_size = "240x480";#단어목록
windowm1_size = "240x480";#설정
#topmost = tkinter.IntVar();
#topmost_temp = tkinter.BooleanVar();
#print("test");
error = [];
error_message = {
    FileNotFoundError : ".py 파일과 같은 경로에 dictionary.txt 파일이 없습니다.\ndictionary.txt 파일은 한 줄에 적힌 문구를 한 문제로 인식합니다. 마지막은 공백 개행이 오도록 해주세요."
, io.UnsupportedOperation : "dictionary.txt 파일을 찾았지만 읽을 수 없습니다."
, ValueError : "잘못된 값입니다. 파일을 열지 못했거나 찾는 단어가 파일에 없습니다."
, UnicodeDecodeError : ".py 파일과 같은 경로에 존재하는 dictionary.txt 파일의 인코딩이 UTF-8이어야 합니다."
, SyntaxError : "치명적인 오류가 발생했습니다."
, UnboundLocalError : "전역 변수를 사용할 수 없습니다."
, EOFError : "따옴표가 끝맺어지지 않았거나 Python IDLE에서만 작동하는 기능을 사용하려 했습니다."
, ImportError : "그러한 모듈이 없습니다."
, ModuleNotFoundError : "모듈이 있으나 찾을 수 없습니다."
, AttributeError : "모듈이 잘못된 라이브러리를 참조했습니다."
, NameError : "그러한 함수 또는 변수가 없거나 사용할 수 없습니다."
, IndexError : "단어 목록이 비어있습니다."
, RuntimeError : "반복 처리 도중 변수의 크기가 변경되었습니다."
, IndentationError : "들여쓰기 오류입니다."
, ZeroDivisionError : "피자 1판을 0명의 친구와 나누려고 시도했습니다."
, RecursionError : "무한 루프입니다."
, KeyError : "그러한 키가 없습니다."
, TypeError : "잘못된 자료형입니다."
, KeyboardInterrupt : "사용자가 프로그램을 강제로 종료했습니다."
, PermissionError : "권한이 없습니다. 경로가 잘못되었거나 이미 사용 중인 파일일 수도 있습니다."
};
print("간단한 타자 연습", fullver, "\n\n\nOS 버전:", platform.system(), platform.win32_ver()[0], platform.win32_ver()[1], "\nPython 버전:", platform.python_version(), platform.python_build());

#source.close();
class main():
    menu = 0;
    timer = 3;
    topmost = True;
    window2_askokcancel = False;
    def  __init__(self, root):
        #if root == None: root = {};
        #지금부터 글로벌에 있는변수들 싹다 self 붙이고 global은 지우기
        global n, Q, topmost_temp, error;
        self.root = root;
        try:
            with open("dictionary.txt", "r+") as self.source:
                self.dictionary = self.source.readlines(); self.source.seek(0);#w는 쓰기만 되고 읽을 수가 없음;;
                self.i = 1; menu_suc = 0;
                while menu_suc == 0:
                    #print("시작됨");
                    #print("menu는 1입니다.");
                    if self.menu == 0:
                        #else: print("메뉴의 번호나 글자를 입력해주세요.");
                        self.window1 = tkinter.Tk();#2.0
                        #window1_frame1 = tkinter.Frame();
                        #print("1");
                        self.window1.title(f"간단한 타자 연습 {fullver}");
                        self.window1.geometry(window1_size);
                        #print("2");
                        self.window1.attributes("-topmost", self.topmost);
                        if int(platform.python_version_tuple()[1]) < ver: tkinter.messagebox.showwarning("호환성 문제", "현재 Python 버전이 개발 당시 사용된 Python 버전보다 낮습니다! 제대로 동작하지 않을 수 있습니다.");
                        for i in [2, 1, 0]:
                            if str(platform.win32_ver()[1]).split('.')[i] < winver.split('.')[i]:
                                tkinter.messagebox.showwarning("호환성 문제", "현재 OS 버전이 개발 당시 사용된 OS 버전보다 낮습니다! 제대로 동작하지 않을 수 있습니다.");
                                break;
                        if self.dictionary == []:
                            tkinter.messagebox.showerror("타자 연습을 시작할 수 없음", "단어 목록이 비어있어서 타자 연습을 시작할 수 없습니다. 단어를 추가하세요!");
                            #self.menu = 2;
                        #def menu1(): menu = 1;
                        #print("테스트");
                        #def menu2(): menu = 2;
                        #print("입니다");
                        tkinter.ttk.Button(self.window1, text = "타자 연습", command = lambda: self.menu1(root), width = 30, compound = 'c').grid(row = 0, column = 0, columnspan = 2);
                        tkinter.ttk.Button(self.window1, text = "단어 목록", command = lambda: self.menu2(root), width = 30, compound = 'c').grid(row = 0, column = 2, columnspan = 2);
                        tkinter.ttk.Button(self.window1, text = "설정", command = lambda: self.setting(root), width = 30, compound = 'c').grid(row = 1, column = 1, columnspan = 2);
                        tkinter.ttk.Button(self.window1, text = "종료", command = lambda: self.shutdown(root), width = 15, compound = 'c').grid(row = 2, column = 1, columnspan = 2);
                        #tkinter.ttk.Button(window1, text = "종료", command = shutdown).pack();
                        #grid와 pack은 동시에 사용불가
                        #print("3");
                        self.window1.focus_set();
                        self.window1.mainloop();
                    elif (self.menu == 1) or (self.menu == "타자 연습") or (self.menu == "타자연습"):

                        '''def press_strat():
                            if n == 0: n = 9999;
                            tkinter.ttk.Label(window1, text = f"{n}개를 출제합니다.\n준비되었으면 시작하세요...").grid(row = 0, column = 0, columnspan = 3);
                        '''
                        self.window2 = tkinter.Tk();
                        self.window2.title("문제 수 입력");
                        self.window2.geometry(window2_size);
                        self.window2.attributes("-topmost", self.topmost);
                        
                        tkinter.ttk.Label(self.window2, text = "몇문제를 풀까요?").grid(row = 0, column = 0);
                        n = tkinter.ttk.Entry(self.window2);#저기에 tkinter.ttk 어쩌구를 붙이면 모듈 라이브러리로 인식해서 entry 그자체를 받음.
                        #위에 grid를 붙이는 순간 n은 입력값이 아닌 grid 값을 받음.
                        n.grid(row = 0, column = 1, columnspan = 3);
                        tkinter.ttk.Button(self.window2, text = "확인", command = lambda: self.window2_askokcancel==self.press_start(root)).grid(row = 1, column = 1);
                        tkinter.ttk.Button(self.window2, text = "취소", command = lambda: self.window2.destroy()).grid(row = 1, column = 2);
                        self.window2.focus_set();
                        menu_suc = 1; menu = 0; self.window2_askokcancel = False;
                        self.window2.mainloop();
                        #input(f"{n}개를 출제합니다.\n준비되면 시작하세요...");
                    elif (self.menu == 2) or (self.menu == "단어목록") or (self.menu == "단어 목록"):
                        menu_suc = 2;
                        #print("단어 목록을 편집합니다.");
                        while menu_suc == 2:
                            window0 = tkinter.Tk();
                            window0.title("단어 목록 편집");
                            window0.geometry(window0_size);
                            window0.attributes("-topmost", self.topmost);

                            tkinter.ttk.Button(window0, text = "목록 보기", command = lambda: self.view_list(root)).grid(row = 0, column = 0);
                            tkinter.ttk.Button(window0, text = "단어 추가", command = lambda: self.add_word(root)).grid(row = 1, column = 0);
                            tkinter.ttk.Button(window0, text = "단어 찾기", command = lambda: self.find_word(root)).grid(row = 2, column = 0);
                            tkinter.ttk.Button(window0, text = "단어 삭제", command = lambda: self.delete_word(root)).grid(row = 3, column = 0);
                            tkinter.ttk.Button(window0, text = "나가기", command = window0.destroy).grid(row = 4, column = 0);
                            #menu = str(input("1. 목록 보기\n2. 단어 추가\n3. 단어 검색\n4. 단어 삭제\n5. 나가기\n"));
                            window0.focus_set();
                            window0.mainloop();
                            if (self.menu == 2) or (self.menu == "단어 추가") or (self.menu == "단어추가"):
                                pass;
                            elif (self.menu == 3) or (self.menu == "단어 검색") or (self.menu == "단어검색"):
                                pass;
                            elif (self.menu == 4) or (self.menu == "단어삭제") or (self.menu == "단어 삭제"):
                                pass;
                            elif (self.menu == 5) or (self.menu == "나가기"):
                                pass;
                            else: 
                                #print("메뉴의 번호나 글자를 입력해주세요.");
                                continue;
                            self.menu = 0;
                            menu_suc = 0;
                            #print("test");
                        #print(menu_suc);
                    elif self.window2_askokcancel == True: #True/False
                        self.window2_askokcancel = False;
                        #dictionary = source.readlines(); source.seek(0);#여기서 문제
                        #print(source.readlines());
                        #print(dictionary);
                        #print(len(dictionary));
                        #print(dictionary[-1]);
                        isnewlined = self.dictionary[-1];
                        while "\n" in self.dictionary:
                            #print("suc");
                            with open("dictionary.txt", "w+") as self.source2:
                                self.dictionary.remove("\n");
                                self.source2.write("".join(self.dictionary));
                        if isnewlined[-1] != "\n":#\n은 한개 취급;;
                            #print(isnewlined[-2:0]);
                            #print(isnewlined);
                            #print(dictionary);
                            with open("dictionary.txt", "a+") as self.source2:
                                self.source2.write("\n");
                                self.dictionary = self.source.readlines(); self.source.seek(0);
                        window3 = tkinter.Tk();
                        window3.title("타자 연습");
                        window3.geometry(window3_size);
                        window3.attributes("-topmost", self.topmost);

                        #if timer != int: timer = timer.get();#실행이 안돼도 들어가있으면 일단 에러
                        timer_temp = self.timer;
                        '''while timer_temp != 0:
                            timer_label = tkinter.ttk.Label(window3, text = timer_temp).pack();
                            timer_temp = timer_temp-1;#여기도 get때문에 위처럼 처리해야하는데 방법좀 생각해봐
                            time.sleep(1);
                            timer_label.destroy();'''
                        started(root);
                        self.window3.focus_set();
                        self.window3.mainloop();
                        #len
                    elif self.menu == -2:
                        self.menu = 0;
                        
                        windowm1 = tkinter.Tk();
                        windowm1.title("설정");
                        windowm1.geometry(windowm1_size);
                        windowm1.attributes("-topmost", self.topmost);
                        if self.topmost == 1 or self.topmost == True:#or 뒤에 식이 와야함
                            topmost_temp = tkinter.BooleanVar();
                            topmost_temp.set(True);#print("궁'예'지책");
                            #print(topmost_temp.get());
                        elif self.topmost == 0 or self.topmost == False:
                            topmost_temp = tkinter.BooleanVar();
                            topmost_temp.set(False);
                            #print(topmost_temp.get());

                        tkinter.ttk.Label(windowm1, text = "시작하기 전에 카운트다운").grid(row = 0, column = 0);
                        self.timer = tkinter.ttk.Entry(windowm1);
                        self.timer.grid(row = 0, column = 1);
                        tkinter.ttk.Checkbutton(windowm1, text = "창 항상 위에 표시", variable = topmost_temp, command = lambda: self.enable_topmost(root)).grid(row = 1, column = 0);
                        tkinter.ttk.Button(windowm1, text = "나가기", command = windowm1.destroy).grid(row = 3, column = 0);
                        windowm1.focus_set();
                        windowm1.mainloop();
                    elif self.menu == -1: sys.exit("프로그램을 종료했습니다.");
                #while menu_suc == 1:
        except FileNotFoundError as excep:
            with open("dictionary.txt", "w+") as self.source:
                tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def menu1(self, root):#타자연습
        try:
            self.menu = 1;
            #window1_frame1.destroy();
            self.window1.destroy();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def menu2(self, root):#단어목록
        try:
            self.menu = 2;
            #window1_frame1.destroy();
            self.window1.destroy();
            #print(self.menu);
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def setting(self, root):#설정
        try:
            self.menu = -2;
            self.window1.destroy();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def enable_topmost(self, root):#항상 위에 표시
        global topmost_temp;
        try:
            if topmost_temp.get() == True:
                self.topmost = True;
                topmost_temp.set(True);
                #print(topmost);
            elif topmost_temp.get() == False:
                self.topmost = False;
                topmost_temp.set(False);
                #print(topmost);
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def shutdown(self, root):#종료
        try:
            self.menu = -1;
            self.window1.destroy();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def press_start(self, root):
        global n;
        try: n = int(n.get());
        except AttributeError: pass;
        except ValueError:
            tkinter.messagebox.showerror("문제 수 오류", "올바른 값을 입력하세요.");
            #self.window2.destroy();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
        if n == 0: n = 9999;
        #문제: 메시지박스는 실행시 무조건 창이 하나 생김
        #if self.window2.state() == "normal": 
        self.window2.destroy();#비주얼 스튜디오는 성능이 너무 좋아서 편법 소용X
        return tkinter.messagebox.askokcancel("준비", f"{n}개를 출제합니다. 준비되었으면 시작하세요...");#True False 둘중하나
    def started(self, root):
        global window3, n, Q, start;
        start = time.time();
        try: Q = random.choice(self.dictionary);
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
        self.i = 1;
        while i <= n:#여기 주목
            print("시작");
            tkinter.ttk.Label(window3, text = f"문제 {i}").grid(row = 0, column = 0);
            tkinter.ttk.Label(window3, text = Q).grid(row = 2, column = 0);
            A = tkinter.ttk.Entry(window3);
            A.grid(row = 3, column = 0);
            tkinter.ttk.Button(window3, text = "확인", command = lambda: self.iscorrect(root)).grid(row = 3, column = 1);
            
        stop = time.time();
        result_time = stop - start;
        result_min = int(result_time / 60);
        result_sec = result_time - (60 * result_min);
        result_msec = str(result_sec - int(result_sec));
        print(f"경과한 시간: {result_min}분 {int(result_sec)}초 {result_msec[2:5]}\n맞춘 횟수: {i - 1}\n틀린 횟수: {error}");
        #반올림 방식이 다름 주의
        self.dictionary = self.source.readlines(); self.source.seek(0);
        menu_suc = 0;
    def iscorrect(self, root):
        global window3, n, Q;
        if Q != A.get()+"\n":
            '''print(Q);
            print(A);'''#문제에 자꾸 개행이 추가됨
            error = error + 1;
            print("오타\n");
            #continue;#루프중에는 사용못한다 뜨는데 이거 없이 가능?
        else: print("정답\n");
        self.i = self.i + 1;
        self.dictionary.remove(Q);
        if self.dictionary == []: print("더 이상 출제할 문제가 없습니다."); #break;#여기 루프밖이라 에러뜨는데 이거없이 가능?
        Q = random.choice(self.dictionary);
    def view_list(self, root):
        try:
            self.dictionary = self.source.readlines(); self.source.seek(0);
            print("\n"+"".join(self.dictionary));
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def add_word(self, root):
        try:
            #dictionary = source.readlines(); source.seek(0);
            window_add_word = tkinter.Tk();
            window_add_word.title("단어 추가");
            window_add_word.geometry("360x480");
            tkinter.ttk.Label(window_add_word, "추가할 단어 입력").grid(row = 0, column = 0);
            word = str(tkinter.ttk.Entry(window_add_word).grid(row = 0, column = 1, columnspan = 2))+"\n";
            tkinter.ttk.Button(window_add_word, "추가", command = lambda: self.add_word2(root)).grid(row = 0, column = 3);
            tkinter.ttk.Button(window_add_word, "취소", command = window_add_word.destroy).grid(row = 1, column = 1);
            window_add_word.focus_set();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def add_word2(self, root):
        #global error_message;
        try:
            if word == "\n":
                tkinter.messagebox.showwarning("단어 추가 오류", "단어를 입력하세요.");
                add_word();
            else:
                self.dictionary = self.source.readlines(); self.source.seek(0);
                #print(dictionary);
                #input();
                #source = open("dictionary.txt", 'a+');
                #dictionary = source.readlines(); source.seek(0);
                '''source.write(word);
                source.write("\n");'''
                try:
                    with open("dictionary.txt", "a+") as self.source2:
                        self.dictionary = self.source2.readlines(); self.source2.seek(0);
                except Exception as excep:
                    tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
                    error.append(type(excep));
                else:
                    with open("dictionary.txt", "a+") as self.source2:
                        #source2.write("".join(dictionary)+word);
                        source2.write(word);
                        #input();
                        #source = open("dictionary.txt", 'r+');
                        dictionary = self.source.readlines(); self.source.seek(0);#여기서 문제 발생
                        #input();
                        #print(dictionary);
                        tkinter.messagebox.showinfo("단어 추가 성공", f"{word}을(를) 단어 목록에 추가했습니다.");
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def find_word(self, root):
        try:
            window_find_word = tkinter.Tk();
            window_find_word.title("단어 찾기");
            window_find_word.geometry("360x480");
            tkinter.ttk.Label(window_find_word, "찾을 단어 입력").grid(row = 0, column = 0);
            word = str(tkinter.ttk.Entry(window_find_word).grid(row = 0, column = 1, columnspan = 2))+"\n";
            tkinter.ttk.Button(window_find_word, "찾기", command = lambda: self.find_word2(root)).grid(row = 0, column = 3);
            tkinter.ttk.Button(window_find_word, "취소", command = window_find_word.destroy).grid(row = 1, column = 1);
            window_find_word.focus_set();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def find_word2(self, root):
        try:
            if word == "\n":
                tkinter.messagebox.showwarning("단어 찾기 오류", "단어를 입력하세요.");
                find_word();
            elif word in self.dictionary: print(f"단어 목록에 {word}이(가) 있습니다.");
            else: print(f"단어 목록에 {word}이(가) 없습니다. 추가해보세요!");
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
    def delete_word(self, root):
        try:
            window_delete_word = tkinter.Tk();
            window_delete_word.title("단어 삭제");
            window_delete_word.geometry("360x240");
            tkinter.ttk.Label(window_delete_word, "지울 단어 입력").grid(row = 0, column = 0);
            word = str(tkinter.ttk.Entry(window_delete_word).grid(row = 0, column = 1, columnspan = 2))+"\n";
            tkinter.ttk.Button(window_delete_word, "삭제", command = lambda: self.delete_word2(root)).grid(row = 0, column = 3);
            tkinter.ttk.Button(window_delete_word, "취소", command = window_delete_word.destroy).grid(row = 1, column = 1);
            window_delete_word.focus_set();
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));    
    def delete_word2(self, root):
        try:
            if word == "\n":
                tkinter.messagebox.showwarning("단어 삭제 오류", "단어를 입력하세요.");
                delete_word();
            elif word in self.dictionary:
                try:
                    with open("dictionary.txt", "w+") as self.source2:
                        self.source2.seek(0);
                except Exception as excep:
                    tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
                    error.append(type(excep));
                else:
                    with open("dictionary.txt", "w+") as self.source2:
                        self.dictionary.remove(word);
                        self.source2.write("".join(self.dictionary));
                        tkinter.messagebox.showinfo("단어 삭제 성공", f"단어 목록에서 {word}을(를) 삭제했습니다.");
            else: tkinter.messagebox.showwarning("단어 삭제 실패", f"단어 목록에 {word}이(가) 없습니다.");
        except Exception as excep:
            tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
            error.append(type(excep));
#main();
while True:
    try:
        root = None;#대체왜;;
        if len(error) == 0: main(root);
        else:
            #global i;
            print("\n오류 목록");
            for i in range(len(error)):
                print(error[i]);
            tkinter.messagebox.showerror("오류", "오류로 인해 프로그램을 더 이상 실행할 수 없습니다. 자세한 내용은 콘솔창을 참고하세요.");
            sys.exit("프로그램을 종료했습니다.");
    except Exception as excep:
        tkinter.messagebox.showerror(type(excep), f"{excep}\n\n{error_message[type(excep)]}");
        error.append(type(excep));
