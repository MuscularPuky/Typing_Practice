# == = is, != = is not? not is?
import random, time, io
print("간단한 타자 연습 v1.2.28-105\n");
#source.close();
try:
    with open("dictionary.txt", "r+") as source:
        dictionary = source.readlines(); source.seek(0);#포인터 재정렬. 이것때문에 뻘짓을 얼마나
except FileNotFoundError: print("오류: FileNotFoundError\n.py 파일과 같은 경로에 dictionary.txt 파일이 없습니다.\ndictionary.txt 파일은 한 줄에 적힌 문구를 한 문제로 인식합니다. 마지막은 공백 개행이 오도록 해주세요."); input("계속하려면 아무 키나 누르세요...");
except io.UnsupportedOperation: print("오류: io.UnsupportedOperation\ndictionary.txt 파일을 찾았지만 읽을 수 없습니다."); input("계속하려면 아무 키나 누르세요...");
except ValueError: print("오류: ValueError\n잘못된 값입니다. 파일을 열지 못했거나 찾는 단어가 파일에 없습니다."); input("계속하려면 아무 키나 누르세요...");
except UnicodeDecodeError: print("오류: UnicodeDecodeError\n.py 파일과 같은 경로에 존재하는 dictionary.txt 파일의 인코딩이 UTF-8이어야 합니다."); input("계속하려면 아무 키나 누르세요...");
else:
    with open("dictionary.txt", "r+") as source:
        dictionary = source.readlines(); source.seek(0);#w는 쓰기만 되고 읽을 수가 없음;;
        i = 1; error = 0; menu_suc = 0;
        while menu_suc == 0:
            if dictionary == []:
                print("\n단어 목록이 비어있어서 타자 연습을 시작할 수 없습니다. 단어를 추가하세요!"); input("계속하려면 아무 키나 누르세요...");
                menu = 2;
            else: menu = str(input("메뉴의 번호나 글자를 입력해주세요.\n1. 타자 연습\n2. 단어 목록\n"));
            if (menu == '1') or (menu == "타자 연습") or (menu == "타자연습"):
                n = int(input("타자 연습을 시작합니다. 몇 문제를 풀까요?\n"));
                if n == 0:
                    n = 9999;
                #break;
                menu_suc = 1; menu = 0;
                input(f"{n}개를 출제합니다.\n준비되면 시작하세요...");
                start = time.time();
                #dictionary = source.readlines(); source.seek(0);#여기서 문제
                #print(source.readlines());
                #print(dictionary);
                #print(len(dictionary));
                #print(dictionary[-1]);
                isnewlined = dictionary[-1];
                while "\n" in dictionary:
                    #print("suc");
                    with open("dictionary.txt", "w+") as source2:
                        dictionary.remove("\n");
                        source2.write("".join(dictionary));
                if isnewlined[-1] != "\n":#\n은 한개 취급;;
                    #print(isnewlined[-2:0]);
                    #print(isnewlined);
                    #print(dictionary);
                    with open("dictionary.txt", "a+") as source2:
                        source2.write("\n");
                        dictionary = source.readlines(); source.seek(0);
                try: Q = random.choice(dictionary);
                except IndexError: print("\n오류: IndexError\n단어 목록이 비어있습니다.\n"); input("계속하려면 아무 키나 누르세요...");
                Q = random.choice(dictionary);
                i = 1;
                while i <= n:
                    print(f"{i}번째 문제");
                    print(Q);
                    A = input()+"\n";
                    if Q != A:
                        '''print(Q);
                        print(A);'''#문제에 자꾸 개행이 추가됨
                        error = error + 1;
                        print("오타\n");
                        continue;
                    else: print("정답\n");
                    i = i + 1;
                    dictionary.remove(Q);
                    if dictionary == []: print("더 이상 출제할 문제가 없습니다."); break;
                    Q = random.choice(dictionary);
                stop = time.time();
                result_time = stop - start;
                result_min = int(result_time / 60);
                result_sec = result_time - (60 * result_min);
                result_msec = str(result_sec - int(result_sec));
                input(f"경과한 시간: {result_min}분 {int(result_sec)}초 {result_msec[2:5]}\n맞춘 횟수: {i - 1}\n틀린 횟수: {error}");
                #반올림 방식이 다름 주의
                dictionary = source.readlines(); source.seek(0);
                menu_suc = 0;
                #len
            elif (menu == '2') or (menu == "단어목록") or (menu == "단어 목록"):
                menu_suc = 2;
                print("단어 목록을 편집합니다.");
                while menu_suc == 2:
                    menu = str(input("1. 목록 보기\n2. 단어 추가\n3. 단어 검색\n4. 단어 삭제\n5. 나가기\n"));
                    if (menu == '1') or (menu == "목록보기") or (menu == "목록 보기"):
                        dictionary = source.readlines(); source.seek(0);
                        print("\n"+"".join(dictionary));#텍스트 파일은 이미 개행으로 분리되어있음
                    elif (menu == '2') or (menu == "단어 추가") or (menu == "단어추가"):
                        #dictionary = source.readlines(); source.seek(0);
                        word = str(input("추가하려는 단어를 입력하세요. 아무것도 입력하지 않을 시 취소됩니다.\n")+"\n");
                        if word == "\n": print("취소되었습니다.");
                        else:
                            dictionary = source.readlines(); source.seek(0);
                            #print(dictionary);
                            #input();
                            #source = open("dictionary.txt", 'a+');
                            #dictionary = source.readlines(); source.seek(0);
                            '''source.write(word);
                            source.write("\n");'''
                            try:
                                with open("dictionary.txt", "a+") as source2:
                                    dictionary = source2.readlines(); source2.seek(0);
                            except FileNotFoundError: print("오류: FileNotFoundError\n.py 파일과 같은 경로에 dictionary.txt 파일이 없습니다.\ndictionary.txt 파일은 한 줄에 적힌 문구를 한 문제로 인식합니다. 마지막은 공백 개행이 오도록 해주세요."); input("계속하려면 아무 키나 누르세요...");
                            except io.UnsupportedOperation: print("오류: io.UnsupportedOperation\ndictionary.txt 파일을 찾았지만 읽을 수 없습니다."); input("계속하려면 아무 키나 누르세요...");
                            except ValueError: print("오류: ValueError\n잘못된 값입니다. 파일을 열지 못했거나 찾는 단어가 파일에 없습니다."); input("계속하려면 아무 키나 누르세요...");
                            except UnicodeDecodeError: print("오류: UnicodeDecodeError\n.py 파일과 같은 경로에 존재하는 dictionary.txt 파일의 인코딩이 UTF-8이어야 합니다."); input("계속하려면 아무 키나 누르세요...");
                            else:
                                with open("dictionary.txt", "a+") as source2:
                                    #source2.write("".join(dictionary)+word);
                                    source2.write(word);
                                    #input();
                                    #source = open("dictionary.txt", 'r+');
                                    dictionary = source.readlines(); source.seek(0);#여기서 문제 발생
                                    #input();
                                    #print(dictionary);
                                print(f"{word}을(를) 단어 목록에 추가했습니다.");
                    elif (menu == '3') or (menu == "단어 검색") or (menu == "단어검색"):
                        word = str(input("검색할 단어를 입력하세요. 아무것도 입력하지 않을 시 취소됩니다.\n"))+"\n";
                        if word == "\n": print("취소되었습니다.");
                        elif word in dictionary:
                            print(f"단어 목록에 {word}이(가) 있습니다.");
                        else: print(f"단어 목록에 {word}이(가) 없습니다. 추가해보세요!");
                    elif (menu == '4') or (menu == "단어삭제") or (menu == "단어 삭제"):
                        word = str(input("삭제하려는 단어를 입력하세요. 아무것도 입력하지 않을 시 취소됩니다.\n"))+"\n";
                        if word == "\n": print("취소되었습니다.");
                        elif word in dictionary:
                            try:
                                with open("dictionary.txt", "w+") as source2:
                                    source2.seek(0);
                            except FileNotFoundError: print("오류: FileNotFoundError\n.py 파일과 같은 경로에 dictionary.txt 파일이 없습니다.\ndictionary.txt 파일은 한 줄에 적힌 문구를 한 문제로 인식합니다. 마지막은 공백 개행이 오도록 해주세요."); input("계속하려면 아무 키나 누르세요...");
                            except io.UnsupportedOperation: print("오류: io.UnsupportedOperation\ndictionary.txt 파일을 찾았지만 읽을 수 없습니다."); input("계속하려면 아무 키나 누르세요...");
                            except ValueError: print("오류: ValueError\n잘못된 값입니다. 파일을 열지 못했거나 찾는 단어가 파일에 없습니다."); input("계속하려면 아무 키나 누르세요...");
                            except UnicodeDecodeError: print("오류: UnicodeDecodeError\n.py 파일과 같은 경로에 존재하는 dictionary.txt 파일의 인코딩이 UTF-8이어야 합니다."); input("계속하려면 아무 키나 누르세요...");
                            else:
                                with open("dictionary.txt", "w+") as source2:
                                    dictionary.remove(word);
                                    source2.write("".join(dictionary));
                                print(f"단어 목록에서 {word}을(를) 삭제했습니다.");
                        else: print(f"삭제할 수 없습니다. 단어 목록에 {word}이(가) 없습니다.");
                    elif (menu == '5') or (menu == "나가기"):
                        menu = 0; menu_suc = 0; break;
                    else:
                        print("메뉴의 번호나 글자를 입력해주세요."); continue;
                    menu = 0; #print("test");
                #print(menu_suc);
            #else: print("메뉴의 번호나 글자를 입력해주세요.");
