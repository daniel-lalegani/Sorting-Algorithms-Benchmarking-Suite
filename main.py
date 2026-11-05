#importing needed modules
from tkinter import *
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from win32api import GetLogicalDriveStrings
from PIL import Image,ImageTk
import os
import datetime as dt
import pandas as pd
from statistics import stdev
from tkinter import messagebox,filedialog
from random import randint,random


#main form basic preferences
root = Tk()
root.title("Sorting Algorithms")
xxx = root.winfo_screenwidth()
yyy = root.winfo_screenheight()
root.geometry(f"{xxx}x{yyy}")
root.resizable(False,False)
ratio_x= xxx / 1366
ratio_y= yyy / 768

#defining main variables
algorithm=IntVar(value=1)
input_list=[]
data_analysis = pd.DataFrame(columns=["No", "Number","Algorithm","'If's Checked","Swaps","Time"])
number_of_operation=0
enter_value_counter=0


#preparing and resizing images
drive_image_orginal = Image.open("drive_icon.png")
drive_image_resized = drive_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
drives_image = ImageTk.PhotoImage(drive_image_resized)
browse_image_orginal=Image.open("browsing_icon.png")
browse_image_resized=browse_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
browsing_icon=ImageTk.PhotoImage(browse_image_resized)
folder_image_orginal=Image.open("folder_icon.png")
folder_image_resized=folder_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
folder_icon=ImageTk.PhotoImage(folder_image_resized)
txt_image_orginal=Image.open("txt_icon.png")
txt_image_resized=txt_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
txt_icon=ImageTk.PhotoImage(txt_image_resized)
next_image_orginal=Image.open("next_icon.png")
next_image_resized=next_image_orginal.resize((int(47*ratio_x),int(30*ratio_x)))
next_icon=ImageTk.PhotoImage(next_image_resized)
prev_image_orginal=Image.open("prev_icon.png")
prev_image_resized=prev_image_orginal.resize((int(47*ratio_x),int(30*ratio_x)))
prev_icon=ImageTk.PhotoImage(prev_image_resized)
start_image_orginal=Image.open("start_icon.png")
start_image_resized=start_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
start_icon=ImageTk.PhotoImage(start_image_resized)
reset_image_orginal=Image.open("reset_icon.png")
reset_image_resized=reset_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
reset_icon=ImageTk.PhotoImage(reset_image_resized)
analysis_image_orginal=Image.open("analysis_icon.png")
analysis_image_resized=analysis_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
analysis_icon=ImageTk.PhotoImage(analysis_image_resized)
info_image_orginal=Image.open("info_icon.png")
info_image_resized=info_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
info_icon=ImageTk.PhotoImage(info_image_resized)
save_image_orginal=Image.open("Save-icon.png")
save_image_resized=save_image_orginal.resize((int(35*ratio_x),int(35*ratio_x)))
save_icon=ImageTk.PhotoImage(save_image_resized)
program_icon_orginal=Image.open("program_icon.png")
program_icon=ImageTk.PhotoImage(program_icon_orginal)
root.wm_iconphoto(False,program_icon)

#functions
def main_sort():
    global input_list,algorithm,data_analysis,number_of_operation,if_number_merge,if_number_quick,swap_number_quick
    scrolled_text2.delete("1.0",END)
    algorithm_type = algorithm.get()
    number_of_operation+=1
    #bubble sort
    if algorithm_type==1:
        swap_number = 0
        if_number = 0
        change_swap = 1
        output_list = input_list.copy()
        start_time = dt.datetime.now()
        while change_swap != 0:
            first = swap_number
            for i in range(len(output_list) - 1):
                if_number += 1
                if output_list[i] > output_list[i + 1]:
                    swap_number += 1
                    temp = output_list[i]
                    output_list[i] = output_list[i + 1]
                    output_list[i + 1] = temp
            change_swap = swap_number - first
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration=duration.total_seconds()*1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in output_list:
            scrolled_text2.insert(END,f"{i}\n")
        data_analysis.loc[len(data_analysis)]=[number_of_operation,len(input_list),"Bubble Sort",if_number,swap_number,"{:.0f} microseconds".format(duration)]
    #selection sort
    elif algorithm_type==2:
        output_list = input_list.copy()
        swap_number = 0
        if_number = 0
        start_time = dt.datetime.now()
        for i in range(len(input_list) - 1):
            min_value = output_list[i]
            in_place = True
            for j in range(i + 1, len(input_list)):
                if_number += 1
                if output_list[j] < min_value:
                    min_value = output_list[j]
                    index = j
                    in_place = False
            if in_place == False:
                swap_number += 1
                temp = output_list[i]
                output_list[i] = min_value
                output_list[index] = temp
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in output_list:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Selection Sort", if_number,
                                                 swap_number, "{:.0f} microseconds".format(duration)]


    #insertion sort
    elif algorithm_type==3:
        output_list = input_list.copy()
        swap_number = 0
        if_number = 0
        start_time = dt.datetime.now()
        for i in range(1, len(input_list)):
            if_number+=1
            if output_list[i]<output_list[i-1]:
                output_list[i],output_list[i-1]=output_list[i-1],output_list[i]
                swap_number+=1
                for j in range(i-1, 0, -1):
                    if_number += 1
                    if output_list[j - 1] > output_list[j]:
                        output_list[j], output_list[j - 1] = output_list[j - 1], output_list[j]
                        swap_number += 1
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in output_list:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Insertion Sort", if_number,
                                                 swap_number, "{:.0f} microseconds".format(duration)]


    #merge sort
    elif algorithm_type==4:
        output_list = input_list.copy()
        if_number_merge = 0
        start_time = dt.datetime.now()
        output_list=merge_sort_devide(output_list)
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in output_list:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Merge Sort", if_number_merge,
                                                 None,"{:.0f} microseconds".format(duration)]
    #quick sort
    elif algorithm_type==5:
        if_number_quick = 0
        swap_number_quick = 0
        start_time = dt.datetime.now()
        quick_sort_(0, len(input_list) - 1)
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in input_list:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Quick Sort", if_number_quick,
                                                 swap_number_quick, "{:.0f} microseconds".format(duration)]


    #heap sort
    elif algorithm_type==6:
        output_list = input_list.copy()
        if_number = 0
        swap_number=0
        start_time = dt.datetime.now()
        c=[]
        while len(output_list) > 2:
            n = len(output_list)
            for i in range(n//2-1,-1,-1):
                if_number+=3
                high=i
                l=2*i+1
                r=2*i+2
                if l<n and output_list[high] < output_list[l]:
                    high=l
                if r < n and output_list[high] < output_list[r]:
                    high = r
                if high != i:
                    swap_number += 1
                    output_list[i],output_list[high]=output_list[high],output_list[i]
            output_list[n-1],output_list[0]=output_list[0],output_list[n-1]
            b=output_list.pop(n-1)
            c.insert(0,b)
        if len(output_list) == 2:
            if_number+=1
            if output_list[0] > output_list[1]:
                swap_number+=1
                c.insert(0, output_list[0])
                c.insert(0, output_list[1])
            else:
                c.insert(0, output_list[1])
                c.insert(0, output_list[0])
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in c:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Heap Sort", if_number,
                                                 swap_number, "{:.0f} microseconds".format(duration)]


    #counting sort
    elif algorithm_type==7:
        int_value=True
        for i in input_list:
            if int(i)!= i:
                messagebox.showerror("Counting sort input", "all values should be integer")
                int_value==False
                break
        if int_value==True:
            start_time = dt.datetime.now()
            n = len(input_list)
            max_value = max(input_list)
            min_value = min(input_list)
            range_value = max_value - min_value + 1
            output_list = [0] * n
            counting_list = [0] * range_value
            for i in range(0, n):
                counting_list[input_list[i] - min_value] += 1
            for i in range(1, range_value):
                counting_list[i] = counting_list[i] + counting_list[i - 1]
            for i in range(0, n):
                position = counting_list[input_list[i] - min_value]
                counting_list[input_list[i] - min_value] -= 1
                output_list[position - 1] = input_list[i]
            end_time = dt.datetime.now()
            duration = end_time - start_time
            duration = duration.total_seconds() * 1000000
            duration_label.configure(text="{:.0f} microseconds".format(duration))
            std_dev= stdev(input_list)
            for i in output_list:
                scrolled_text2.insert(END, f"{i}\n")
            data_analysis.loc[len(data_analysis)] = [number_of_operation, "{}\tstd dev={:.2f}".format(len(input_list),std_dev), "Counting Sort", None,
                                                     None, "{:.0f} microseconds".format(duration)]

    #radix sort
    elif algorithm_type==8:
        int_value = True
        for i in input_list:
            if int(i) != i:
                messagebox.showerror("Radix sort input", "all values should be integer")
                int_value == False
                break
        if int_value == True:
            start_time = dt.datetime.now()
            max_value = max(input_list)
            n = len(input_list)
            digit = 1
            while max_value / digit >= 1:
                output_list = [0] * n
                counting_list = [0] * 10
                for i in range(0, n):
                    index = input_list[i] // digit
                    counting_list[index % 10] += 1
                for i in range(1, 10):
                    counting_list[i] += counting_list[i - 1]
                for i in range(n - 1, -1, -1):
                    index = input_list[i] // digit
                    output_list[counting_list[index % 10] - 1] = input_list[i]
                    counting_list[index % 10] -= 1
                input_list = output_list.copy()
                digit *= 10
            end_time = dt.datetime.now()
            duration = end_time - start_time
            duration = duration.total_seconds() * 1000000
            duration_label.configure(text="{:.0f} microseconds".format(duration))
            for i in input_list:
                scrolled_text2.insert(END, f"{i}\n")
            data_analysis.loc[len(data_analysis)] = [number_of_operation,
                                                     len(input_list), "Radix Sort",
                                                     None,
                                                     None, "{:.0f} microseconds".format(duration)]

    #bucket sort
    elif algorithm_type==9:
        start_time = dt.datetime.now()
        buckets_list = []
        try:
            for i in range(10):
                buckets_list.append([])
            for j in input_list:
                index = int(10 * j)
                buckets_list[index].append(j)
            for p in range(len(buckets_list)):
                for i in range(1, len(buckets_list[p])):
                    if buckets_list[p][i] < buckets_list[p][i - 1]:
                        buckets_list[p][i], buckets_list[p][i - 1] = buckets_list[p][i - 1], buckets_list[p][i]
                        for j in range(i - 1, 0, -1):
                            if buckets_list[p][j - 1] > buckets_list[p][j]:
                                buckets_list[p][j], buckets_list[p][j - 1] = buckets_list[p][j - 1], buckets_list[p][j]
            index = 0
            for i in range(10):
                for j in range(len(buckets_list[i])):
                    input_list[index] = buckets_list[i][j]
                    index += 1
            end_time = dt.datetime.now()
            duration = end_time - start_time
            duration = duration.total_seconds() * 1000000
            duration_label.configure(text="{:.0f} microseconds".format(duration))
            for i in input_list:
                scrolled_text2.insert(END, f"{i}\n")
            data_analysis.loc[len(data_analysis)] = [number_of_operation,len(input_list),
                                                     "Bucket Sort",
                                                     None,
                                                     None, "{:.0f} microseconds".format(duration)]

        except:
            messagebox.showerror("Bucket sort input","all values should be in range (0,1)")
    #python sort
    elif algorithm_type==10:
        output_list = input_list.copy()
        start_time = dt.datetime.now()
        output_list.sort()
        end_time = dt.datetime.now()
        duration = end_time - start_time
        duration = duration.total_seconds() * 1000000
        duration_label.configure(text="{:.0f} microseconds".format(duration))
        for i in output_list:
            scrolled_text2.insert(END, f"{i}\n")
        data_analysis.loc[len(data_analysis)] = [number_of_operation, len(input_list), "Python Sort", None,
                                                None,"{:.0f} microseconds".format(duration)]

def quick_sort_(start,end):
    global if_number_quick,swap_number_quick,input_list
    if start<end:
        pivot=input_list[end]
        sorted_index=start-1
        for i in range(start,end):
            if_number_quick+=1
            if input_list[i]<= pivot:
                swap_number_quick +=1
                sorted_index += 1
                input_list[sorted_index],input_list[i]=input_list[i],input_list[sorted_index]
        input_list[sorted_index+1],input_list[end]=input_list[end],input_list[sorted_index+1]
        quick_sort_(start,sorted_index)
        quick_sort_(sorted_index+2,end)

def merge_sort_devide(input):
    global if_number_merge
    output_list=input.copy()
    if len(output_list)==1:
        return output_list
    elif len(output_list)==2:
        if_number_merge+=1
        if output_list[1]<output_list[0]:
            temp=output_list[0]
            output_list[0]=output_list[1]
            output_list[1]=temp
        return output_list
    else:
        n = len(output_list)
        a = merge_sort_devide(output_list[0:n//2])
        b = merge_sort_devide(output_list[n//2:n ])
        d=merge_sort_combine(a,b)
        return d

def merge_sort_combine(a,b):
    global if_number_merge
    d=[]
    while len(a)!=0 and len(b)!=0:
        if_number_merge+=1
        if a[0]<b[0]:
            c=a.pop(0)
            d.append(c)
        else:
            c = b.pop(0)
            d.append(c)
    while len(a)!=0 :
        c=a.pop(0)
        d.append(c)
    while len(b) != 0:
        c = b.pop(0)
        d.append(c)
    return d



def resett():
    global input_list,enter_value_counter
    input_list = []
    enter_value_counter = 0
    label_9.config(text="0")
    scrolled_text1.config(state='normal')
    scrolled_text1.delete("1.0",END)
    scrolled_text1.config(state='disabled')
    scrolled_text2.delete("1.0", END)
    try:
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_f_point.delete(0, END)
        entry_f_numbers.delete(0, END)
    except:
        pass
    entry_3.insert(0, "Min")
    entry_4.insert(END, "Max")
    entry_5.insert(END, "Number")
    entry_f_point.insert(END, "Digits After 0.")
    entry_f_numbers.insert(END, "Number")

def file_browser(a=""):
    global xxx, yyy,form2,form3,address
    if a=="":
        address=""
        form3 = Toplevel()
        form3["background"] = "#F1FAEE"
        form3.wm_iconphoto(False,browsing_icon)
        form3.title("File Browser")
        container = Frame(form3, bg="#F1FAEE")
        canvas = Canvas(container, bg="#F1FAEE")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#F1FAEE")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        drives = GetLogicalDriveStrings()
        drives = drives.split('\\\000')[:-1]
        hard_drives={}
        for i in range(0,len(drives)):
            hard_drives[i]=Button(scrollable_frame,image=drives_image,bg="#F1FAEE",text=drives[i],compound="left",command=lambda a=drives[i]:file_browser(a))
            hard_drives[i].pack(side=TOP)
    else:
        form3.destroy()
        form3 = Toplevel()
        form3["background"] = "#F1FAEE"
        form3.title("File Browser")
        form3.wm_iconphoto(False, browsing_icon)
        container = Frame(form3,bg="#F1FAEE")
        canvas = Canvas(container,bg="#F1FAEE")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas,bg="#F1FAEE")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        if len(a)==2:
            address=a+"/"
        else:
            address=address+"/"+a
        item_list=os.listdir(address)
        files={}
        for i in range(len(item_list)):
            if "." not in item_list[i]:
                files[i]=Button(scrollable_frame,image=folder_icon,bg="#F1FAEE",text=item_list[i],compound="left",command=lambda a=item_list[i]:file_browser(a))
                files[i].grid(row=i,column=0,sticky="W")
            elif ".txt" in item_list[i]:
                files[i] = Button(scrollable_frame, image=txt_icon, bg="#F1FAEE", text=item_list[i],compound="left", command=lambda path=address+"/"+item_list[i]:open_txt1(path))
                files[i].grid(row=i, column=0, sticky="W")

def open_txt1(path):
    global form3,input_list
    input_list = []
    scrolled_text1.config(state='normal')
    scrolled_text1.delete("1.0",END)
    form3.destroy()
    with open(path,"r") as f:
        input_txt=f.readlines()
    for i in input_txt:
        try:
            input_list.append(eval(i))
        except:
            if i=='\n':
                pass
            else:
                input_list.append(int(i))
    for i in input_list:
        scrolled_text1.insert(END, "{}\n".format(i))
    scrolled_text1.config(state='disabled')

def analysis_show():
    global xxx,yyy,data_analysis
    analysis_window=Toplevel()
    analysis_window.wm_iconphoto(False, analysis_icon)
    analysis_window.title("Analysis")
    analysis_window.geometry("{}x{}".format(int(.8*xxx),int(.8*yyy)))
    analysis_window.resizable(False,False)
    frame1 = LabelFrame(analysis_window, text="Data")
    frame1.place(relheight=1, relwidth=1)
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=.97, relwidth=.97)
    scrollx = Scrollbar(frame1, orient="horizontal", command=tv1.xview)
    scrolly = Scrollbar(frame1, orient="vertical", command=tv1.yview)
    tv1.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    scrollx.pack(side="bottom", fill="x")
    scrolly.pack(side="right", fill="y")
    tv1["column"] = list(data_analysis.columns)
    tv1["show"] = "headings"
    for i in tv1["column"]:
        tv1.heading(i, text=i)
    rows = data_analysis.to_numpy().tolist()
    for row in rows:
        tv1.insert("", "end", values=row)
def next_button_():
    global input_list,enter_value_counter
    scrolled_text1.config(state='normal')
    if enter_value_counter==0:
        input_list=[]
        scrolled_text1.delete("1.0",END)
    a=eval(entry_1.get())
    if enter_value_counter == 0:
        scrolled_text1.insert(END, f"{a}")
    else:
        scrolled_text1.insert(END,f"\n{a}")
    input_list.append(a)
    enter_value_counter+=1
    scrolled_text1.config(state='disabled')
    entry_1.delete(0,END)
    label_9.config(text=f"{enter_value_counter}")
def prev_button_():
    global input_list,enter_value_counter
    if enter_value_counter>0:
        scrolled_text1.config(state='normal')
        scrolled_text1.delete(f"{enter_value_counter}.0",END)
        a=input_list.pop(enter_value_counter-1)
        entry_1.delete(0,END)
        entry_1.insert(0,a)
        enter_value_counter-=1
        scrolled_text1.config(state='disabled')
        label_9.config(text=f"{enter_value_counter}")
def random_button_():
    global input_list
    input_list=[]
    scrolled_text1.config(state='normal')
    scrolled_text1.delete("1.0", END)
    scrolled_text2.delete("1.0", END)
    min_value=int(entry_3.get())
    max_value = int(entry_4.get())
    number_value = int(entry_5.get())
    for i in range(number_value):
        input_list.append(randint(min_value,max_value))
    for i in input_list:
        scrolled_text1.insert(END, f"{i}\n")
    scrolled_text1.config(state='disabled')

def random_f_button():
    global input_list
    input_list=[]
    scrolled_text1.config(state='normal')
    scrolled_text1.delete("1.0", END)
    scrolled_text2.delete("1.0", END)
    number=int(entry_f_numbers.get())
    point=int(entry_f_point.get())
    if point>17:
        point=17
    i=0
    while i<number:
        a=int(random()*(10**point))
        b=a/(10**point)
        if b!=0:
            input_list.append(b)
            i +=1
    for i in input_list:
        scrolled_text1.insert(END, "{}\n".format(i))
    scrolled_text1.config(state='disabled')

def save_button_():
    global number_of_operation
    sorted_text=scrolled_text2.get("1.0",END)
    data=sorted_text.split("\n")
    save_location=filedialog.askdirectory(title="Select a folder to save txt file in")
    if save_location !="":
        repeated=0
        name=''
        done=False
        while done==False:
            try:
                if repeated==0:
                    with open(f"{save_location}/sorted{number_of_operation}.txt","x") as f:
                        name=f"sorted{number_of_operation}.txt"
                        for i in data:
                            f.write(f"{i}\n")
                        done=True
                        messagebox.showinfo("Save", f"{name} saved in {save_location}")
                else:
                    with open(f"{save_location}/sorted{number_of_operation}({repeated}).txt","x") as f:
                        name=f"sorted{number_of_operation}({repeated}).txt"
                        for i in data:
                            f.write(f"{i}\n")
                        done=True
                        messagebox.showinfo("Save", f"{name} saved in {save_location}")
            except:
                pass
            repeated += 1



def info_button_():
    global xxx, yyy
    info_window = Toplevel()
    info_window.wm_iconphoto(False, info_icon)
    info_window.title("Info")
    info_window.geometry("{}x{}".format(int(.8 * xxx), int(.8 * yyy)))
    info_window.resizable(False, False)
    scrolled_text_info=ScrolledText(info_window,font=("times new roman",int(15 * ratio_x)))
    scrolled_text_info.place(relheight=1,relwidth=1)
    scrolled_text_info.insert("1.0","""Sorting Algorithms (ver 1 , June 2022)
Developer: Daniel Lalegani
Email: danielirani2000@gmail.com
Created by Python 3.10 - tkinter
Special Thanks To Dear Mohammad Ahmadpour 


Help:
-Values in the .txt file you want to import, should be in the form of "each line one number".
-While manually entering numbers, you can also use right and left arrow keys of your keyboard instead of visual buttons.
-This program can be run with any screen resolution.
-Generating random floating numbers, the maximum number of digits after "." is 17.
-To save the output (sorted array) as .txt file (each line one number), click on save icon in the bottom of the main window.
-The algorithms' Speed of operation can not be compared to each other when low size data is imported.
-In the analysis window, some values are shown by "None" phrase, which means they can not be computed during the operation.
-Counting sort algorithm showed to have inverse relationship with dispersion of data, therefore standard deviation of each set of data is calculated and showed when using this algorithm.


Base Code Used For Each Algorithm (not exactly the used one):
** Bubble sort **
swap_number=0
change_swap = 1
while change_swap != 0:
    first = swap_number
    for i in range(len(input_list) - 1):
        if_number += 1
        if input_list[i] > input_list[i + 1]:
            swap_number += 1
            input_list[i],input_list[i + 1]=input_list[i + 1],input_list[i]
    change_swap = swap_number - first
print(input_list)

** Selection sort **
for i in range(len(input_list) - 1):
    min_value = input_list[i]
    in_place = True
    for j in range(i + 1, len(input_list)):
        if input_list[j] < min_value:
            min_value = output_list[j]
            index = j
            in_place = False
    if in_place == False:
        temp = output_list[i]
        output_list[i] = min_value
        output_list[index] = temp
print(input_list)

** insertion sort **
for i in range(1, len(input_list)):
    if input_list[i]<input_list[i-1]:
        input_list[i],input_list[i-1]=input_list[i-1],input_list[i]
        for j in range(i-1, 0, -1):
            if input_list[j - 1] > input_list[j]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
print(input_list)

** Merge sort **
input_list=merge_sort_devide(input_list)
print(input_list)
def merge_sort_devide(input):
    output_list=input.copy()
    if len(output_list)==1:
        return output_list
    elif len(output_list)==2:
        if output_list[1]<output_list[0]:
            output_list[0],output_list[1]=output_list[1],output_list[0]
        return output_list
    else:
        n = len(output_list)
        a = merge_sort_devide(output_list[0:n//2])
        b = merge_sort_devide(output_list[n//2:n ])
        d=merge_sort_combine(a,b)
        return d

def merge_sort_combine(a,b):
    d=[]
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c=a.pop(0)
            d.append(c)
        else:
            c = b.pop(0)
            d.append(c)
    while len(a)!=0 :
        c=a.pop(0)
        d.append(c)
    while len(b) != 0:
        c = b.pop(0)
        d.append(c)
    return d

** Quick sort **
quick_sort_(0, len(input_list) - 1)
print(input_list)
def quick_sort_(start,end):
    global input_list
    if start<end:
        pivot=input_list[end]
        sorted_index=start-1
        for i in range(start,end):
            if input_list[i]<= pivot:
                sorted_index += 1
                input_list[sorted_index],input_list[i]=input_list[i],input_list[sorted_index]
        input_list[sorted_index+1],input_list[end]=input_list[end],input_list[sorted_index+1]
        quick_sort_(start,sorted_index)
        quick_sort_(sorted_index+2,end)


** Heap sort **
c=[]
while len(input_list) > 2:
    n = len(input_list)
    for i in range(n//2-1,-1,-1):
        high=i
        l=2*i+1
        r=2*i+2
        if l<n and input_list[high] < input_list[l]:
            high=l
        if r < n and input_list[high] < input_list[r]:
            high = r
        if high != i:
            input_list[i],input_list[high]=input_list[high],input_list[i]
    input_list[n-1],input_list[0]=input_list[0],input_list[n-1]
    b=input_list.pop(n-1)
    c.insert(0,b)
if len(input_list) == 2:
    if input_list[0] > input_list[1]:
        c.insert(0, input_list[0])
        c.insert(0, input_list[1])
    else:
        c.insert(0, input_list[1])
        c.insert(0, input_list[0])
print(c)

** counting sort **
int_value=True
for i in input_list:
    if int(i)!= i:
        messagebox.showerror("Counting sort input", "all values should be integer")
        int_value==False
        break
if int_value==True:
    n = len(input_list)
    max_value = max(input_list)
    min_value = min(input_list)
    range_value = max_value - min_value + 1
    output_list = [0] * n
    counting_list = [0] * range_value
    for i in range(0, n):
        counting_list[input_list[i] - min_value] += 1
    for i in range(1, range_value):
        counting_list[i] = counting_list[i] + counting_list[i - 1]
    for i in range(0, n):
        position = counting_list[input_list[i] - min_value]
        counting_list[input_list[i] - min_value] -= 1
        output_list[position - 1] = input_list[i]
    print(output_list)

** radix sort **
int_value = True
for i in input_list:
    if int(i) != i:
        messagebox.showerror("Radix sort input", "all values should be integer")
        int_value == False
        break
if int_value == True:
    max_value = max(input_list)
    n = len(input_list)
    digit = 1
    while max_value / digit >= 1:
        output_list = [0] * n
        counting_list = [0] * 10
        for i in range(0, n):
            index = input_list[i] // digit
            counting_list[index % 10] += 1
        for i in range(1, 10):
            counting_list[i] += counting_list[i - 1]
        for i in range(n - 1, -1, -1):
            index = input_list[i] // digit
            output_list[counting_list[index % 10] - 1] = input_list[i]
            counting_list[index % 10] -= 1
        input_list = output_list.copy()
        digit *= 10
    print(input_list)

** Bucket sort **
buckets_list = []
try:
    for i in range(10):
        buckets_list.append([])
    for j in input_list:
        index = int(10 * j)
        buckets_list[index].append(j)
    for p in range(len(buckets_list)):
        for i in range(1, len(buckets_list[p])):
            if buckets_list[p][i] < buckets_list[p][i - 1]:
                buckets_list[p][i], buckets_list[p][i - 1] = buckets_list[p][i - 1], buckets_list[p][i]
                for j in range(i - 1, 0, -1):
                    if buckets_list[p][j - 1] > buckets_list[p][j]:
                        buckets_list[p][j], buckets_list[p][j - 1] = buckets_list[p][j - 1], buckets_list[p][j]
    index = 0
    for i in range(10):
        for j in range(len(buckets_list[i])):
            input_list[index] = buckets_list[i][j]
            index += 1
    print(input_list)
except:
    messagebox.showerror("Bucket sort input","all values should be in range (0,1)")
    """)
    scrolled_text_info.config(state="disabled")


#objects>>input part
canvas = Canvas(height=yyy,width=xxx,bg="#F1FAEE")
canvas.place(x=0,y=0)
label_1=Label(text="Input", font=("times new roman",int(20 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_1.place(x=0.10 *xxx,y=.04*yyy)
frame_1 = LabelFrame(width=int(.16*xxx), height=int(.62*yyy), bg="#F1FAEE", font=("times new roman",int(14 * ratio_x)), bd=0, fg="#1d3557")
frame_1.place(x=.03*xxx,y=.14*yyy)
label_3=Label(text="-A txt file", font=("times new roman",int(11 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_3.place(x=0.04 *xxx,y=.18*yyy)
browsing_button1 = Button(image=browsing_icon,borderwidth=0,bg="#F1FAEE",command=file_browser)
browsing_button1.place(x=.15*xxx,y=.17*yyy)
label_4=Label(text="-Enter Numbers", font=("times new roman",int(11 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_4.place(x=0.04 *xxx,y=.28*yyy)
entry_1=Entry(font=("times new roman",int(11 * ratio_x)), width=int(0.013 * xxx))
entry_1.place(x=0.06 *xxx,y=.33*yyy)
next_button=Button(relief="ridge",text="next>>", font=("times new roman",int(9 * ratio_x)), bg="#F1FAEE", fg="#1d3557",image=next_icon,command=next_button_)
next_button.place(x=0.13 *xxx,y=.38*yyy)
prev_button=Button(relief="ridge",text="<<prev", font=("times new roman",int(9 * ratio_x)), bg="#F1FAEE", fg="#1d3557",image=prev_icon,command=prev_button_)
prev_button.place(x=0.05 *xxx,y=.38*yyy)
label_9=Label(text="0", font=("times new roman",int(13 * ratio_x)), bg="#F1FAEE", fg="#1d3557")
label_9.place(x=0.103 *xxx,y=.388*yyy)
label_5=Label(text="-Random Int Numbers", font=("times new roman",int(11 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_5.place(x=0.04 *xxx,y=.48*yyy)
entry_3=Entry(font=("times new roman",int(10 * ratio_x)), width=int(0.004 * xxx))
entry_3.place(x=0.04 *xxx,y=.53*yyy)
entry_3.insert(END,"Min")
entry_4=Entry(font=("times new roman",int(10 * ratio_x)), width=int(0.004 * xxx))
entry_4.place(x=0.08 *xxx,y=.53*yyy)
entry_4.insert(END,"Max")
entry_5=Entry(font=("times new roman",int(10 * ratio_x)), width=int(0.006 * xxx))
entry_5.place(x=0.12 *xxx,y=.53*yyy)
entry_5.insert(END,"Number")
generate_button=Button(relief="ridge",text="Generate", font=("times new roman",int(9 * ratio_x)), bg="#A7B7DC", fg="#1d3557", width=int(0.013 * xxx),command=random_button_)
generate_button.place(x=0.04 *xxx,y=.56*yyy)
label_f=Label(text="-Random Floating Point Numbers\nrange(0,1)", font=("times new roman",int(11 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_f.place(x=0.04 *xxx,y=.62*yyy)
entry_f_point=Entry(font=("times new roman",int(10 * ratio_x)), width=int(0.012 * xxx))
entry_f_point.place(x=0.04 *xxx,y=.68*yyy)
entry_f_point.insert(END,"Digits After 0.")
entry_f_numbers=Entry(font=("times new roman",int(10 * ratio_x)), width=int(0.006 * xxx))
entry_f_numbers.place(x=0.12 *xxx,y=.68*yyy)
entry_f_numbers.insert(END,"Number")
generate_button_f=Button(relief="ridge",text="Generate", font=("times new roman",int(9 * ratio_x)), bg="#A7B7DC", fg="#1d3557", width=int(0.013 * xxx),command=random_f_button)
generate_button_f.place(x=0.04 *xxx,y=.71*yyy)

#objects>>selection of algorithms part
label_2=Label(text="Select Algorithm", font=("times new roman",int(20 * ratio_x)), bg="#A8DADC", fg="#1d3557")
label_2.place(x=0.82 *xxx,y=.04*yyy)
frame_3 = LabelFrame(width=int(.16*xxx), height=int(.30*yyy),text="Basic Sorting Algorithms", bg="#F1FAEE", font=("times new roman",int(14 * ratio_x)), bd=0, fg="#1d3557")
frame_3.place(x=.81*xxx,y=.12*yyy)
frame_4 = LabelFrame(width=int(.16*xxx), height=int(.18*yyy),text="Advance Sorting Algorithms", bg="#F1FAEE", font=("times new roman",int(14 * ratio_x)), bd=0, fg="#1d3557")
frame_4.place(x=.81*xxx,y=.46*yyy)
frame_5 = LabelFrame(width=int(.16*xxx), height=int(.17*yyy),text="Python Sorting Algorithm", bg="#F1FAEE", font=("times new roman",int(14 * ratio_x)), bd=0, fg="#1d3557")
frame_5.place(x=.81*xxx,y=.68*yyy)
bubble_sort=Radiobutton(text="1-Bubble sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=1)
bubble_sort.place(x=.82*xxx,y=.16*yyy)
selection_sort=Radiobutton(text="2-Selection sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=2)
selection_sort.place(x=.82*xxx,y=.2*yyy)
insertion_sort=Radiobutton(text="3-Insertion sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=3)
insertion_sort.place(x=.82*xxx,y=.24*yyy)
merge_sort=Radiobutton(text="4-Merge sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=4)
merge_sort.place(x=.82*xxx,y=.28*yyy)
quick_sort=Radiobutton(text="5-Quick sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=5)
quick_sort.place(x=.82*xxx,y=.32*yyy)
heap_sort=Radiobutton(text="6-Heap sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=6)
heap_sort.place(x=.82*xxx,y=.36*yyy)
counting_sort=Radiobutton(text="7-Counting sort (just int)",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=7)
counting_sort.place(x=.82*xxx,y=.50*yyy)
radix_sort=Radiobutton(text="8-Radix sort (just int)",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=8)
radix_sort.place(x=.82*xxx,y=.54*yyy)
bucket_sort=Radiobutton(text="9-Bucket sort               \n( values in range(0,1) )",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=9)
bucket_sort.place(x=.82*xxx,y=.58*yyy)
python_sort=Radiobutton(text="10-Python built-in sort",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557",var=algorithm,value=10)
python_sort.place(x=.82*xxx,y=.72*yyy)
label_11=Label(text="(Timsort algorithm which is\na hybrid sorting algorithm,\nderived from merge sort and\ninsertion sort)",font=("times new roman",int(11*ratio_x),"italic"),bg="#F1FAEE",fg="#1d3557")
label_11.place(x=.82*xxx,y=.75*yyy)
#objects>>center part
     #scrolled textbox
label_input=Label(text="Input", font=("times new roman",int(15 * ratio_x)), bg="#F1FAEE", fg="#1d3557")
label_input.place(x=.32*xxx,y=.16*yyy)
label_input=Label(text="Sorted", font=("times new roman",int(15 * ratio_x)), bg="#F1FAEE", fg="#1d3557")
label_input.place(x=.62*xxx,y=.16*yyy)
scrolled_text1=ScrolledText(root,width=int(.031*xxx),height=int(.031*yyy))
scrolled_text1.place(x=.22*xxx,y=.20*yyy)
scrolled_text2=ScrolledText(root,width=int(.031*xxx),height=int(.031*yyy))
scrolled_text2.place(x=.52*xxx,y=.20*yyy)
#objects>>top part
titlelabel= Label(text="Sorting Algorithms", font=("times new roman", int(24 * ratio_x), "italic"), fg="white", bg="#457b9d")
titlelabel.pack(side=TOP, pady=30 * ratio_y)
#objects>>buttom
start=Button(text="Start",image=start_icon, font=("times new roman", int(13 * ratio_x), "italic"), fg="white", bg="#457b9d", command=lambda  :main_sort(),relief="flat")
start.place(x=0.37 *xxx,y=.75*yyy)
duration_label=Label(text="",font=("times new roman", int(13 * ratio_x), "italic"), fg="white", bg="#457b9d")
duration_label.place(x=0.45 *xxx,y=.75*yyy)
clearbutton=Button(text="Reset",image=reset_icon, font=("times new roman", int(13 * ratio_x), "italic"), fg="white", bg="#457b9d", command=lambda :resett(),relief="flat")
clearbutton.place(x=0.595*xxx,y=.75*yyy)
help_button=Button(text="About", font=("times new roman", int(9 * ratio_x), "bold"), fg="#1d3557", bg="#457b9d",image=info_icon,relief="flat",command=info_button_)
help_button.place(x=0.29 *xxx,y=.825*yyy)
analysis_show=Button(text="Data Analysis", font=("times new roman", int(9 * ratio_x), "bold"), fg="#1d3557", bg="#457b9d",image=analysis_icon,relief="flat",command=analysis_show)
analysis_show.place(x=0.48 *xxx,y=.825*yyy)
save_button=Button(text="About", font=("times new roman", int(9 * ratio_x), "bold"), fg="#1d3557", bg="#457b9d",image=save_icon,relief="flat",command=save_button_)
save_button.place(x=0.67 *xxx,y=.825*yyy)
#events
entry_3.bind('<Button-1>',lambda x : entry_3.delete(0,END))
entry_4.bind('<Button-1>',lambda x : entry_4.delete(0,END))
entry_5.bind('<Button-1>',lambda x : entry_5.delete(0,END))
entry_f_point.bind('<Button-1>',lambda x : entry_f_point.delete(0,END))
entry_f_numbers.bind('<Button-1>',lambda x : entry_f_numbers.delete(0,END))
entry_1.bind('<Right>',lambda x: next_button_())
entry_1.bind('<Left>',lambda x: prev_button_())
#shapes
canvas.create_polygon(.27*xxx,.02*yyy,.73*xxx,.02*yyy,.78*xxx,.15*yyy,.22*xxx,.15*yyy,fill="#457b9d")
canvas.create_polygon(.02*xxx,.02*yyy,.25*xxx,.02*yyy,.20*xxx,.15*yyy,.20*xxx,.74*yyy,.25*xxx,.89*yyy,.02*xxx,.89*yyy,fill="#A8DADC")
canvas.create_polygon(.75*xxx,.02*yyy,.98*xxx,.02*yyy,.98*xxx,.89*yyy,.75*xxx,.89*yyy,.80*xxx,.74*yyy,.80*xxx,.15*yyy,fill="#A8DADC")
canvas.create_polygon(.22*xxx,.74*yyy,.78*xxx,.74*yyy,.73*xxx,.89*yyy,.27*xxx,.89*yyy,fill="#457b9d")
mainloop()