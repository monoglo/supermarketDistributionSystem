import time
import system
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

sy = system.System()  # 实例化System对象
# Basic window settings
root = tk.Tk()  # 根页面初始化
root.title("超市配送系统")
root.geometry("700x400")
# Main frame
frame_main = ttk.Frame(root, padding="3 3 12 12")  # 主页面frame
# Secondry frame
frame_left = ttk.Frame(frame_main)  # 左部分frame
frame_right = ttk.Frame(frame_main)  # 右部分frame
# Third frame
frame_left_button = ttk.Frame(frame_left,
                              relief="sunken",
                              borderwidth=1,
                              padding="0 0 0 100")
frame_left_clock = ttk.Frame(frame_left)
# Left button
button_order = ttk.Button(frame_left_button, text="订单管理")
button_stock = ttk.Button(frame_left_button, text="库存管理")
button_customer = ttk.Button(frame_left_button, text="客户管理")
button_courier = ttk.Button(frame_left_button, text="配送员管理")
button_administrator = ttk.Button(frame_left_button, text="管理员管理")
button_purchase = ttk.Button(frame_left_button, text="进货管理")
button_statistics = ttk.Button(frame_left_button, text="统计")
button_setttings = ttk.Button(frame_left_button, text="设置")
# Time label
label_showtime = ttk.Label(frame_left_clock, text="当前时间：")
label_time = ttk.Label(frame_left_clock,
                       text=time.strftime('%Y-%m-%d\n%H:%M:%S',
                                          time.localtime(time.time())))
# Welcome Page
frame_page_welcome = ttk.Frame(frame_right)
label_hw = ttk.Label(frame_page_welcome,
                     text='你好世界！',
                     font=("Source Han Serif", 26, "bold"))
label_welcome = ttk.Label(frame_page_welcome,
                          text='Welcome!',
                          font=("Source Han Serif", 18, "bold"))
label_hw.pack()
label_welcome.pack()

# Order Page
frame_page_order = ttk.Frame(frame_right)
button_create_order = ttk.Button(frame_page_order, text="创建订单")
button_search_order = ttk.Button(frame_page_order, text="查找订单")
label_active_order = ttk.Label(frame_page_order, text="正在进行中的订单：")
# Active order Treeview
scrollbar_active_order = ttk.Scrollbar(frame_page_order)
treeview_active_order = ttk.Treeview(frame_page_order,
                                     height=7,
                                     show="headings")
treeview_active_order["columns"] = ("订单编号", "购买人", "总金额", "下单时间", "当前状态")
# 设置每列宽度和对齐方式
treeview_active_order.column("订单编号", anchor='center', width=100)
treeview_active_order.column("购买人", anchor='center', width=60)
treeview_active_order.column("总金额", anchor='center', width=60)
treeview_active_order.column("下单时间", anchor='center', width=100)
treeview_active_order.column("当前状态", anchor='center', width=100)
# 设置每列表头标题文本
treeview_active_order.heading("订单编号", text="订单编号")
treeview_active_order.heading("购买人", text="购买人")
treeview_active_order.heading("总金额", text="总金额")
treeview_active_order.heading("下单时间", text="下单时间")
treeview_active_order.heading("当前状态", text="当前状态")
label_completed_order = ttk.Label(frame_page_order, text="已完成的订单：")
# Completed order Treeview
scrollbar_completed_order = ttk.Scrollbar(frame_page_order)
treeview_completed_order = ttk.Treeview(frame_page_order,
                                        height=6,
                                        show="headings")
treeview_completed_order["columns"] = ("订单编号", "购买人", "总金额", "下单时间", "完成时间",
                                       "完成状态")
# 设置每列宽度和对齐方式
treeview_completed_order.column("订单编号", anchor='center', width=100)
treeview_completed_order.column("购买人", anchor='center', width=60)
treeview_completed_order.column("总金额", anchor='center', width=60)
treeview_completed_order.column("下单时间", anchor='center', width=100)
treeview_completed_order.column("完成时间", anchor='center', width=100)
treeview_completed_order.column("完成状态", anchor='center', width=100)
# 设置每列表头标题文本
treeview_completed_order.heading("订单编号", text="订单编号")
treeview_completed_order.heading("购买人", text="购买人")
treeview_completed_order.heading("总金额", text="总金额")
treeview_completed_order.heading("下单时间", text="下单时间")
treeview_completed_order.heading("完成时间", text="完成时间")
treeview_completed_order.heading("完成状态", text="当前状态")
# Grid Page Widgets
button_create_order.grid(column=0, row=0, sticky="w")
button_search_order.grid(column=0, row=0, sticky="e")
label_active_order.grid(column=0, row=1, columnspan=2, sticky="w")
treeview_active_order.grid(column=0, row=2, columnspan=3)
scrollbar_active_order.grid(column=3, row=2, sticky="nsw")
scrollbar_active_order.config(command=treeview_active_order.yview)
label_completed_order.grid(column=0, row=3, columnspan=2, sticky="w")
treeview_completed_order.grid(column=0, row=4, columnspan=4)
scrollbar_completed_order.grid(column=4, row=4, sticky="nsw")
scrollbar_completed_order.config(command=treeview_completed_order.yview)

# Page Stock
frame_page_stock = ttk.Frame(frame_right)
button_add_goods = ttk.Button(frame_page_stock, text="新增商品")
button_search_goods = ttk.Button(frame_page_stock, text="查找商品")
button_list_goods = ttk.Button(frame_page_stock, text="列出商品")
label_current_goods = ttk.Label(frame_page_stock, text="当前库存商品：")
scrollbar_current_goods = ttk.Scrollbar(frame_page_stock)
treeview_current_goods = ttk.Treeview(frame_page_stock,
                                      height=15,
                                      show="headings")
treeview_current_goods["columns"] = ("批次编号", "商品编号", "商品名", "商品种类", "到期时间",
                                     "进货时间", "单位", "数量", "价格", "成本")
treeview_current_goods.column("批次编号", anchor='center', width=60)
treeview_current_goods.column("商品编号", anchor='center', width=60)
treeview_current_goods.column("商品名", anchor='center', width=60)
treeview_current_goods.column("商品种类", anchor='center', width=60)
treeview_current_goods.column("到期时间", anchor='center', width=60)
treeview_current_goods.column("进货时间", anchor='center', width=60)
treeview_current_goods.column("单位", anchor='center', width=40)
treeview_current_goods.column("数量", anchor='center', width=50)
treeview_current_goods.column("价格", anchor='center', width=60)
treeview_current_goods.column("成本", anchor='center', width=60)

treeview_current_goods.heading("批次编号", text="批次编号")
treeview_current_goods.heading("商品编号", text="商品编号")
treeview_current_goods.heading("商品名", text="商品名")
treeview_current_goods.heading("商品种类", text="商品种类")
treeview_current_goods.heading("到期时间", text="到期时间")
treeview_current_goods.heading("进货时间", text="进货时间")
treeview_current_goods.heading("单位", text="单位")
treeview_current_goods.heading("数量", text="数量")
treeview_current_goods.heading("价格", text="价格")
treeview_current_goods.heading("成本", text="成本")
# Grid Page Widgets
button_add_goods.grid(column=0, row=0, sticky="w")
button_search_goods.grid(column=1, row=0, sticky="w")
button_list_goods.grid(column=2, row=0, sticky="w")
label_current_goods.grid(column=0, row=1, columnspan=2, sticky="w")
treeview_current_goods.grid(column=0, row=2, columnspan=4)
scrollbar_current_goods.grid(column=4, row=2, sticky="nsw")
scrollbar_current_goods.config(command=treeview_current_goods.yview)

# Page Customer
frame_page_customer = ttk.Frame(frame_right)
button_add_customer = ttk.Button(frame_page_customer, text="新增客户")
button_search_customer = ttk.Button(frame_page_customer, text="查找客户")
button_list_customer = ttk.Button(frame_page_customer, text="列出客户")
label_current_customer = ttk.Label(frame_page_customer, text="客户列表：")
scrollbar_current_customer = ttk.Scrollbar(frame_page_customer)
treeview_current_customer = ttk.Treeview(frame_page_customer,
                                         height=15,
                                         show="headings")
treeview_current_customer["columns"] = ("编号", "用户名", "昵称", "邮箱", "手机", "地址",
                                        "用户组", "余额", "状态")
treeview_current_customer.column("编号", anchor='center', width=40)
treeview_current_customer.column("用户名", anchor='center', width=60)
treeview_current_customer.column("昵称", anchor='center', width=60)
treeview_current_customer.column("邮箱", anchor='center', width=60)
treeview_current_customer.column("手机", anchor='center', width=60)
treeview_current_customer.column("地址", anchor='center', width=60)
treeview_current_customer.column("用户组", anchor='center', width=60)
treeview_current_customer.column("余额", anchor='center', width=60)
treeview_current_customer.column("状态", anchor='center', width=60)
treeview_current_customer.heading("编号", text="编号")
treeview_current_customer.heading("用户名", text="用户名")
treeview_current_customer.heading("昵称", text="昵称")
treeview_current_customer.heading("邮箱", text="邮箱")
treeview_current_customer.heading("手机", text="手机")
treeview_current_customer.heading("地址", text="地址")
treeview_current_customer.heading("用户组", text="用户组")
treeview_current_customer.heading("余额", text="余额")
treeview_current_customer.heading("状态", text="状态")
# Grid Page Widgets
button_add_customer.grid(column=0, row=0, sticky="w")
button_search_customer.grid(column=1, row=0, sticky="w")
button_list_customer.grid(column=2, row=0, sticky="w")
label_current_customer.grid(column=0, row=1, columnspan=2, sticky="w")
treeview_current_customer.grid(column=0, row=2, columnspan=4)
scrollbar_current_customer.grid(column=4, row=2, sticky="nsw")
scrollbar_current_customer.config(command=treeview_current_customer.yview)

# Page courier
frame_page_courier = ttk.Frame(frame_right)
button_add_courier = ttk.Button(frame_page_courier, text="新增配送员")
button_search_courier = ttk.Button(frame_page_courier, text="查找配送员")
button_list_courier = ttk.Button(frame_page_courier, text="列出配送员")
label_current_courier = ttk.Label(frame_page_courier, text="配送员列表：")
scrollbar_current_courier = ttk.Scrollbar(frame_page_courier)
treeview_current_courier = ttk.Treeview(frame_page_courier,
                                        height=15,
                                        show="headings")
treeview_current_courier["columns"] = ("编号", "用户名", "昵称", "邮箱", "手机", "地址",
                                       "用户组", "递送次数", "薪水", "状态")
treeview_current_courier.column("编号", anchor='center', width=40)
treeview_current_courier.column("用户名", anchor='center', width=60)
treeview_current_courier.column("昵称", anchor='center', width=60)
treeview_current_courier.column("邮箱", anchor='center', width=60)
treeview_current_courier.column("手机", anchor='center', width=60)
treeview_current_courier.column("地址", anchor='center', width=60)
treeview_current_courier.column("用户组", anchor='center', width=60)
treeview_current_courier.column("递送次数", anchor='center', width=60)
treeview_current_courier.column("薪水", anchor='center', width=60)
treeview_current_courier.column("状态", anchor='center', width=60)
treeview_current_courier.heading("编号", text="编号")
treeview_current_courier.heading("用户名", text="用户名")
treeview_current_courier.heading("昵称", text="昵称")
treeview_current_courier.heading("邮箱", text="邮箱")
treeview_current_courier.heading("手机", text="手机")
treeview_current_courier.heading("地址", text="地址")
treeview_current_courier.heading("用户组", text="用户组")
treeview_current_courier.heading("递送次数", text="递送次数")
treeview_current_courier.heading("薪水", text="薪水")
treeview_current_courier.heading("状态", text="状态")
# Grid Page Widgets
button_add_courier.grid(column=0, row=0, sticky="w")
button_search_courier.grid(column=1, row=0, sticky="w")
button_list_courier.grid(column=2, row=0, sticky="w")
label_current_courier.grid(column=0, row=1, columnspan=2, sticky="w")
treeview_current_courier.grid(column=0, row=2, columnspan=4)
scrollbar_current_courier.grid(column=4, row=2, sticky="nsw")
scrollbar_current_courier.config(command=treeview_current_courier.yview)

# Page administrator
frame_page_administrator = ttk.Frame(frame_right)
button_add_administrator = ttk.Button(frame_page_administrator, text="新增管理员")
button_search_administrator = ttk.Button(frame_page_administrator,
                                         text="查找管理员")
button_list_administrator = ttk.Button(frame_page_administrator, text="列出管理员")
label_current_administrator = ttk.Label(frame_page_administrator,
                                        text="当前管理员列表：")
scrollbar_current_administrator = ttk.Scrollbar(frame_page_administrator)
treeview_current_administrator = ttk.Treeview(frame_page_administrator,
                                              height=15,
                                              show="headings")
treeview_current_administrator["columns"] = ("编号", "用户名", "昵称", "电子邮箱", "手机号码",
                                             "地址", "用户组", "状态")
treeview_current_administrator.column("编号", anchor='center', width=40)
treeview_current_administrator.column("用户名", anchor='center', width=60)
treeview_current_administrator.column("昵称", anchor='center', width=80)
treeview_current_administrator.column("电子邮箱", anchor='center', width=100)
treeview_current_administrator.column("手机号码", anchor='center', width=60)
treeview_current_administrator.column("地址", anchor='center', width=60)
treeview_current_administrator.column("用户组", anchor='center', width=100)
treeview_current_administrator.column("状态", anchor='center', width=70)
treeview_current_administrator.heading("编号", text="编号")
treeview_current_administrator.heading("用户名", text="用户名")
treeview_current_administrator.heading("昵称", text="昵称")
treeview_current_administrator.heading("电子邮箱", text="电子邮箱")
treeview_current_administrator.heading("手机号码", text="手机号码")
treeview_current_administrator.heading("地址", text="地址")
treeview_current_administrator.heading("用户组", text="用户组")
treeview_current_administrator.heading("状态", text="状态")
# Grid Page Widgets
button_add_administrator.grid(column=0, row=0, sticky="W")
button_search_administrator.grid(column=1, row=0, sticky="W")
button_list_administrator.grid(column=2, row=0, sticky="W")
label_current_administrator.grid(column=0, row=1, sticky="W")
treeview_current_administrator.grid(column=0, row=2, columnspan=5)
scrollbar_current_administrator.grid(column=5, row=2, sticky="nsw")
scrollbar_current_administrator.config(
    command=treeview_current_administrator.yview)

# Grid Frame
frame_main.pack(side="left")
frame_left.pack(side="left")
frame_left_button.pack()
frame_left_clock.pack()
frame_right.pack(fill="both")
button_order.pack()
button_stock.pack()
button_customer.pack()
button_courier.pack()
button_administrator.pack()
button_purchase.pack()
button_statistics.pack()
button_setttings.pack()
label_showtime.pack()
label_time.pack()
frame_page_welcome.pack()


def trickit():
    # 时间自动更新
    # Time trick
    currentTime = time.strftime('%Y-%m-%d\n%H:%M:%S',
                                time.localtime(time.time()))
    label_time.config(text=currentTime)
    root.update()
    label_time.after(1000, trickit)


def switchPage(page):
    frame_page_welcome.pack_forget()
    frame_page_stock.pack_forget()
    frame_page_customer.pack_forget()
    frame_page_courier.pack_forget()
    frame_page_administrator.pack_forget()
    frame_page_order.pack_forget()
    page.pack()


def del_all_treeview(tree):
    # 清空administrator的treeview
    for item in tree.get_children():
        tree.delete(item)


def administrator_list_all():
    # 列出所有管理员
    del_all_treeview(treeview_current_administrator)
    rest = sy.search_account_administrator('all', '1', 0)
    for item in rest:
        treeview_current_administrator.insert(
            "",
            0,
            values=(item['aid'], item['name'], item['screenName'],
                    item['email'], item['phone'], item['adress'],
                    item['group'], item['status']))


def customer_list_all():
    # 列出所有管理员
    del_all_treeview(treeview_current_customer)
    rest = sy.search_account_customer('all', '1', 0)
    for item in rest:
        treeview_current_customer.insert(
            "",
            0,
            values=(item['cuid'], item['name'], item['screenName'],
                    item['email'], item['phone'], item['adress'],
                    item['group'], item['balance'], item['status']))


def courier_list_all():
    # 列出所有管理员
    del_all_treeview(treeview_current_courier)
    rest = sy.search_account_courier('all', '1', 0)
    for item in rest:
        treeview_current_courier.insert(
            "",
            0,
            values=(item['coid'], item['name'], item['screenName'],
                    item['email'], item['phone'], item['adress'],
                    item['group'], item['deliveryTimes'], item['salary'],
                    item['status']))


def good_list_all():
    # 列出所有管理员
    del_all_treeview(treeview_current_goods)
    rest = sy.search_good('all', '1', 0)
    for item in rest:
        treeview_current_goods.insert(
            "",
            0,
            values=(item['gid'], item['productNumber'], item['name'],
                    item['type'], item['expireDate'], item['createTime'],
                    item['unit'], item['quantity'], item['price'],
                    item['cost']))


def search_administrator_gui():
    # 搜索栏
    def search_administrator():
        try:
            del_all_treeview(treeview_current_administrator)
            rest = sy.search_account_administrator(method_selected.get(),
                                                   value.get(), 0)
            for item in rest:
                treeview_current_administrator.insert(
                    "",
                    0,
                    values=(item['aid'], item['name'], item['screenName'],
                            item['email'], item['phone'], item['adress'],
                            item['group'], item['status']))
            switchPage(frame_page_administrator)
            searchwindow.destroy()
            messagebox.showinfo("Success", "Search out!")
        except Exception as e:
            messagebox.showerror("Error", e)

    searchwindow = tk.Toplevel()
    searchwindow.title('管理员搜索')
    searchwindow.geometry('350x30')
    method_selected = tk.StringVar()
    value = tk.StringVar()
    comboxlist = ttk.Combobox(searchwindow, textvariable=method_selected)
    comboxlist["values"] = ("name", "screenName", "email", "phone", "adress",
                            "group", "status")
    comboxlist.current(0)
    comboxlist.grid(row=0, sticky='W')
    tk.Entry(searchwindow, textvariable=value).grid(row=0,
                                                    column=1,
                                                    sticky='W')
    tk.Button(searchwindow, text="搜索",
              command=search_administrator).grid(row=0, column=2, sticky='W')


def search_customer_gui():
    # 搜索栏
    def search_customer():
        try:
            del_all_treeview(treeview_current_customer)
            rest = sy.search_account_customer(method_selected.get(),
                                              value.get(), 0)
            for item in rest:
                treeview_current_customer.insert(
                    "",
                    0,
                    values=(item['cuid'], item['name'], item['screenName'],
                            item['email'], item['phone'], item['adress'],
                            item['group'], item['status']))
            switchPage(frame_page_customer)
            searchwindow.destroy()
            messagebox.showinfo("Success", "Search out!")
        except Exception as e:
            messagebox.showerror("Error", e)

    searchwindow = tk.Toplevel()
    searchwindow.title('管理员搜索')
    searchwindow.geometry('350x30')
    method_selected = tk.StringVar()
    value = tk.StringVar()
    comboxlist = ttk.Combobox(searchwindow, textvariable=method_selected)
    comboxlist["values"] = ("name", "screenName", "email", "phone", "adress",
                            "group", "status")
    comboxlist.current(0)
    comboxlist.grid(row=0, sticky='W')
    tk.Entry(searchwindow, textvariable=value).grid(row=0,
                                                    column=1,
                                                    sticky='W')
    tk.Button(searchwindow, text="搜索",
              command=search_customer).grid(row=0, column=2, sticky='W')


def search_courier_gui():
    # 搜索栏
    def search_courier():
        try:
            del_all_treeview(treeview_current_courier)
            rest = sy.search_account_courier(method_selected.get(),
                                             value.get(), 0)
            for item in rest:
                treeview_current_courier.insert(
                    "",
                    0,
                    values=(item['cuid'], item['name'], item['screenName'],
                            item['email'], item['phone'], item['adress'],
                            item['group'], item['status']))
            switchPage(frame_page_courier)
            searchwindow.destroy()
            messagebox.showinfo("Success", "Search out!")
        except Exception as e:
            messagebox.showerror("Error", e)

    searchwindow = tk.Toplevel()
    searchwindow.title('配送员搜索')
    searchwindow.geometry('350x30')
    method_selected = tk.StringVar()
    value = tk.StringVar()
    comboxlist = ttk.Combobox(searchwindow, textvariable=method_selected)
    comboxlist["values"] = ("name", "screenName", "email", "phone", "adress",
                            "group", "status")
    comboxlist.current(0)
    comboxlist.grid(row=0, sticky='W')
    tk.Entry(searchwindow, textvariable=value).grid(row=0,
                                                    column=1,
                                                    sticky='W')
    tk.Button(searchwindow, text="搜索", command=search_courier).grid(row=0,
                                                                    column=2,
                                                                    sticky='W')


def add_administrator_gui():
    # 添加管理员
    def add_administrator():
        try:
            del_all_treeview(treeview_current_administrator)
            sy.create_account_administrator(name.get(), screenName.get(),
                                            email.get(), phone.get(),
                                            adress.get(), password.get())
            messagebox.showinfo("Success", "Create a new administrator!")
            addwindow.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    addwindow = tk.Toplevel()
    addwindow.title('添加管理员')
    addwindow.geometry('220x180')
    name = tk.StringVar()
    screenName = tk.StringVar()
    email = tk.StringVar()
    phone = tk.StringVar()
    adress = tk.StringVar()
    password = tk.StringVar()
    tk.Label(addwindow, text='用户名：').grid(row=0, sticky='W')
    tk.Entry(addwindow, textvariable=name).grid(row=0, column=1, sticky='W')
    tk.Label(addwindow, text='昵称：').grid(row=1, sticky='W')
    tk.Entry(addwindow, textvariable=screenName).grid(row=1,
                                                      column=1,
                                                      sticky='W')
    tk.Label(addwindow, text='邮箱：').grid(row=2, sticky='W')
    tk.Entry(addwindow, textvariable=email).grid(row=2, column=1, sticky='W')
    tk.Label(addwindow, text='手机号码：').grid(row=3, sticky='W')
    tk.Entry(addwindow, textvariable=phone).grid(row=3, column=1, sticky='W')
    tk.Label(addwindow, text='地址：').grid(row=4, sticky='W')
    tk.Entry(addwindow, textvariable=adress).grid(row=4, column=1, sticky='W')
    tk.Label(addwindow, text='密码：').grid(row=5, sticky='W')
    tk.Entry(addwindow, show='*', textvariable=password).grid(row=5,
                                                              column=1,
                                                              sticky='W')
    tk.Button(addwindow, text='提交', command=add_administrator).grid(row=6,
                                                                    column=1,
                                                                    sticky='E')


def search_good_gui():
    # 搜索栏
    def search_good():
        try:
            del_all_treeview(treeview_current_goods)
            rest = sy.search_good(method_selected.get(), value.get(), 0)
            for item in rest:
                treeview_current_goods.insert(
                    "",
                    0,
                    values=(item['gid'], item['productNumber'], item['name'],
                            item['type'], item['expireDate'],
                            item['createTime'], item['unit'], item['quantity'],
                            item['price'], item['cost']))
            switchPage(frame_page_stock)
            searchwindow.destroy()
            messagebox.showinfo("Success", "Search out!")
        except Exception as e:
            messagebox.showerror("Error", e)

    searchwindow = tk.Toplevel()
    searchwindow.title('库存搜索')
    searchwindow.geometry('350x30')
    method_selected = tk.StringVar()
    value = tk.StringVar()
    comboxlist = ttk.Combobox(searchwindow, textvariable=method_selected)
    comboxlist["values"] = ('gid', 'productNumber', 'name', 'type',
                            'expireDate', 'createTime', 'unit', 'quantity',
                            'price', 'cost')
    comboxlist.current(0)
    comboxlist.grid(row=0, sticky='W')
    tk.Entry(searchwindow, textvariable=value).grid(row=0,
                                                    column=1,
                                                    sticky='W')
    tk.Button(searchwindow, text="搜索", command=search_good).grid(row=0,
                                                                 column=2,
                                                                 sticky='W')


def add_customer_gui():
    # 添加客户
    def add_customer():
        try:
            del_all_treeview(treeview_current_customer)
            sy.create_account_customer(name.get(), screenName.get(),
                                       email.get(), phone.get(), adress.get(),
                                       password.get())
            messagebox.showinfo("Success", "Create a new customer!")
            addwindow.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    addwindow = tk.Toplevel()
    addwindow.title('添加客户')
    addwindow.geometry('220x180')
    name = tk.StringVar()
    screenName = tk.StringVar()
    email = tk.StringVar()
    phone = tk.StringVar()
    adress = tk.StringVar()
    password = tk.StringVar()
    tk.Label(addwindow, text='用户名：').grid(row=0, sticky='W')
    tk.Entry(addwindow, textvariable=name).grid(row=0, column=1, sticky='W')
    tk.Label(addwindow, text='昵称：').grid(row=1, sticky='W')
    tk.Entry(addwindow, textvariable=screenName).grid(row=1,
                                                      column=1,
                                                      sticky='W')
    tk.Label(addwindow, text='邮箱：').grid(row=2, sticky='W')
    tk.Entry(addwindow, textvariable=email).grid(row=2, column=1, sticky='W')
    tk.Label(addwindow, text='手机号码：').grid(row=3, sticky='W')
    tk.Entry(addwindow, textvariable=phone).grid(row=3, column=1, sticky='W')
    tk.Label(addwindow, text='地址：').grid(row=4, sticky='W')
    tk.Entry(addwindow, textvariable=adress).grid(row=4, column=1, sticky='W')
    tk.Label(addwindow, text='密码：').grid(row=5, sticky='W')
    tk.Entry(addwindow, show='*', textvariable=password).grid(row=5,
                                                              column=1,
                                                              sticky='W')
    tk.Button(addwindow, text='提交', command=add_customer).grid(row=6,
                                                               column=1,
                                                               sticky='E')


def add_courier_gui():
    # 添加客户
    def add_courier():
        try:
            del_all_treeview(treeview_current_courier)
            sy.create_account_courier(name.get(), screenName.get(),
                                      email.get(), phone.get(), adress.get(),
                                      password.get())
            messagebox.showinfo("Success", "Create a new courier!")
            addwindow.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    addwindow = tk.Toplevel()
    addwindow.title('添加客户')
    addwindow.geometry('220x180')
    name = tk.StringVar()
    screenName = tk.StringVar()
    email = tk.StringVar()
    phone = tk.StringVar()
    adress = tk.StringVar()
    password = tk.StringVar()
    tk.Label(addwindow, text='用户名：').grid(row=0, sticky='W')
    tk.Entry(addwindow, textvariable=name).grid(row=0, column=1, sticky='W')
    tk.Label(addwindow, text='昵称：').grid(row=1, sticky='W')
    tk.Entry(addwindow, textvariable=screenName).grid(row=1,
                                                      column=1,
                                                      sticky='W')
    tk.Label(addwindow, text='邮箱：').grid(row=2, sticky='W')
    tk.Entry(addwindow, textvariable=email).grid(row=2, column=1, sticky='W')
    tk.Label(addwindow, text='手机号码：').grid(row=3, sticky='W')
    tk.Entry(addwindow, textvariable=phone).grid(row=3, column=1, sticky='W')
    tk.Label(addwindow, text='地址：').grid(row=4, sticky='W')
    tk.Entry(addwindow, textvariable=adress).grid(row=4, column=1, sticky='W')
    tk.Label(addwindow, text='密码：').grid(row=5, sticky='W')
    tk.Entry(addwindow, show='*', textvariable=password).grid(row=5,
                                                              column=1,
                                                              sticky='W')
    tk.Button(addwindow, text='提交', command=add_courier).grid(row=6,
                                                              column=1,
                                                              sticky='E')


def add_good_gui():
    # 添加商品批次
    def add_good():
        try:
            del_all_treeview(treeview_current_goods)
            sy.create_good(productName.get(), name.get(), type.get(),
                           expireTime.get(), unit.get(), quantity.get(),
                           price.get(), cost.get())
            messagebox.showinfo("Success", "Create a new good!")
            addwindow.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    addwindow = tk.Toplevel()
    addwindow.title('添加商品批次')
    addwindow.geometry('220x220')
    productName = tk.StringVar()
    name = tk.StringVar()
    type = tk.StringVar()
    expireTime = tk.StringVar()
    unit = tk.StringVar()
    quantity = tk.StringVar()
    price = tk.StringVar()
    cost = tk.StringVar()
    tk.Label(addwindow, text='商品编号：').grid(row=0, sticky='W')
    tk.Entry(addwindow, textvariable=productName).grid(row=0,
                                                       column=1,
                                                       sticky='W')
    tk.Label(addwindow, text='商品名：').grid(row=1, sticky='W')
    tk.Entry(addwindow, textvariable=name).grid(row=1, column=1, sticky='W')
    tk.Label(addwindow, text='商品种类：').grid(row=2, sticky='W')
    tk.Entry(addwindow, textvariable=type).grid(row=2, column=1, sticky='W')
    tk.Label(addwindow, text='到期时间：').grid(row=3, sticky='W')
    tk.Entry(addwindow, textvariable=expireTime).grid(row=3,
                                                      column=1,
                                                      sticky='W')
    tk.Label(addwindow, text='单位：').grid(row=4, sticky='W')
    tk.Entry(addwindow, textvariable=unit).grid(row=4, column=1, sticky='W')
    tk.Label(addwindow, text='数量：').grid(row=5, sticky='W')
    tk.Entry(addwindow, textvariable=quantity).grid(row=5,
                                                    column=1,
                                                    sticky='W')
    tk.Label(addwindow, text='价格').grid(row=6, sticky='W')
    tk.Entry(addwindow, textvariable=price).grid(row=6, column=1, sticky='W')
    tk.Label(addwindow, text='成本').grid(row=7, sticky='W')
    tk.Entry(addwindow, textvariable=cost).grid(row=7, column=1, sticky='W')
    tk.Button(addwindow, text='提交', command=add_good).grid(row=8,
                                                           column=1,
                                                           sticky='E')


def login():
    # 登录
    try:
        sy.login(entry_username.get(), entry_password.get(), 'administrator')
        label_welcome['text'] = 'Welcome ' + sy.logined['screenName'] + '!'
        window_login.destroy()
        root.deiconify()
    except Exception as e:
        messagebox.showerror("Error", e)


def cancel():
    # 取消
    window_login.destroy()  # Removes the toplevel window
    root.destroy()  # Removes the hidden root window
    sys.exit()


def on_closing_login():
    # 登陆页面关闭执行destroy
    window_login.destroy()  # Removes the toplevel window
    root.destroy()  # Removes the hidden root window
    sys.exit()


label_time.after(1000, trickit)
button_order.config(command=lambda: switchPage(frame_page_order))
button_stock.config(command=lambda: switchPage(frame_page_stock))
button_customer.config(command=lambda: switchPage(frame_page_customer))
button_courier.config(command=lambda: switchPage(frame_page_courier))
button_administrator.config(
    command=lambda: switchPage(frame_page_administrator))
button_list_administrator.config(command=administrator_list_all)
button_add_administrator.config(command=add_administrator_gui)
button_search_administrator.config(command=search_administrator_gui)
button_list_customer.config(command=customer_list_all)
button_add_customer.config(command=add_customer_gui)
button_search_customer.config(command=search_customer_gui)
button_list_courier.config(command=courier_list_all)
button_add_courier.config(command=add_courier_gui)
button_search_courier.config(command=search_courier_gui)
button_list_goods.config(command=good_list_all)
button_add_goods.config(command=add_good_gui)
button_search_goods.config(command=search_good_gui)

if __name__ == "__main__":
    window_login = tk.Toplevel()
    window_login.title('登录')
    window_login.geometry('280x200')
    window_login.protocol("WM_DELETE_WINDOW", on_closing_login)
    label_username = ttk.Label(window_login, text='用户名：')
    label_password = ttk.Label(window_login, text='密码：')
    entry_username = ttk.Entry(window_login)
    entry_password = ttk.Entry(window_login, show='*')
    button_login = ttk.Button(window_login, text='登录', command=login)
    button_cancel = ttk.Button(window_login, text='取消', command=cancel)
    label_username.grid(column=0, row=0, pady=10, sticky='E')
    label_password.grid(column=0, row=1, pady=10, sticky='E')
    entry_username.grid(column=1, row=0, sticky='W')
    entry_password.grid(column=1, row=1, sticky='W')
    button_login.grid(column=0, row=2, pady=10, sticky='W')
    button_cancel.grid(column=1, row=2, sticky='E')
    root.withdraw()
    root.mainloop()
