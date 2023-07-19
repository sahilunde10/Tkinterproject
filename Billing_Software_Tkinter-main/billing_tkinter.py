from fileinput import filename
from logging import root
from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk
from matplotlib.pyplot import text
import random,os
from tkinter import messagebox
import tempfile

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        # -------variable---------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        



        # Product Categories list
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        self.SubCatClothing=["Select Option","Pant","Tshirt","Shirt"]
        self.Pant=["Select Option","Levis","Mufti","Spykar"]
        self.price_levis=4000
        self.price_Mufti=3000
        self.price_spykar=5000

        self.Tshirt=["Select Option","Polo","Rodster","Jack&Jones"]
        self.price_Polo=2500
        self.price_Rodster=1000
        self.price_JackJones=4255

        self.shirt=["Select Option","Peter England","Louis Philipe","Park Avenue"]
        self.price_Peter=7500
        self.price_Louis=6000
        self.price_Park=1755



        self.SubCatLifeStyle=["Select Option","Bath Soap","Face Wash","Hair Oil"]
        self.Bath_Soap=["Select Option","Lifeboy","Lux","Santoor"]
        self.price_Lifeboy=75
        self.price_Lux=60
        self.price_Santoor=55

        self.Face_Wash=["Select Option","Fair&Lovely","Fair&Handsome","MamaEarth"]
        self.price_FairLovely=80
        self.price_FairHandsome=90
        self.price_MamaEarth=70

        self.Hair_Oil=["Select Option","Parachute","Jasmin","Bajaj"]
        self.price_Parachute=25
        self.price_Jasmin=36
        self.price_Bajaj=55



        self.SubCatMobiles=["Select Option","Iphone","Samsung","RealMe","OnePlus"]
        self.Iphone=["Select Option","IphoneX","Iphone_11","Iphone_12"]
        self.price_Iphone=40000
        self.price_Iphone_11=60000
        self.price_Iphone_12=85000

        self.Samsung=["Select Option","Samsung M16","Samsung M12","Samsung M21"]
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.RealMe=["Select Option","RealMe 12","RealMe 13","RealMe 20"]
        self.price_r11=26000
        self.price_r13=10000
        self.price_r20=15000

        self.OnePlus=["Select Option","OnePlus7","OnePlus9","OnePlus10"]
        self.price_one7=46000
        self.price_one9=50000
        self.price_one10=65000




        #image
        # img=Image.open("images/wallpaper.jpg")
        # img=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # lbl_img=Label(self.root,image=self.photoimg)
        # lbl_img.place(x=0,y=0,width=500,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=10,width=1530,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=65,width=1530,height=720)

        # Customer_labelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",16,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=360,height=170)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",16,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblCustName=Label(Cust_Frame,text="Name :",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",16,"bold"),width=20)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=10)

        self.lblEmail=Label(Cust_Frame,text="Email :",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",16,"bold"),width=20)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",16,"bold"),bg="white",fg="red")
        Product_Frame.place(x=380,y=5,width=630,height=170)

        # Category
        self.lblCategory=Label(Product_Frame,text="Select Categories ",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",12),width=15,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # Sub-Category
        self.lblSubCategory=Label(Product_Frame,text="Sub Categories ",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=4)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("times new roman",12),width=15,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=4)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)


        # Product Name
        self.lblProduct=Label(Product_Frame,text="Product Name ",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=4)

        self.Combo_Product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",12),width=15,state="readonly")
        self.Combo_Product.grid(row=2,column=1,sticky=W,padx=5,pady=4)
        self.Combo_Product.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice=Label(Product_Frame,text="Price ",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblPrice.grid(row=0,column=3,sticky=W,padx=5,pady=4)

        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",12),width=15,state="readonly")
        self.Combo_Price.grid(row=0,column=4,sticky=W,padx=4,pady=4)

        # Quantity
        self.lblQuantity=Label(Product_Frame,text="Quantity ",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblQuantity.grid(row=1,column=3,sticky=W,padx=5,pady=4)

        self.entry_quantity=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",12),width=15)
        self.entry_quantity.grid(row=1,column=4,sticky=W,padx=5,pady=4)

        # middle frame

        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=180,width=1000,height=380)

        # search
        Search_Frame=Frame(Main_Frame,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.entry_search=ttk.Entry(Search_Frame,font=("times new roman",16,"bold"),width=15)
        self.entry_search.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('areal',12,'bold'),bg="red",fg="black",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)





        # RightFrame Bill Area

        RightLabelFrame=LabelFrame(Main_Frame,text="Billing Area",font=("times new roman",16,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1025,y=60,width=480,height=500)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",14))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill_labelFrame
        Buttom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",16,"bold"),bg="white",fg="red")
        Buttom_Frame.place(x=10,y=570,width=1500,height=135)

        self.lbl_SubTotal=Label(Buttom_Frame,text="Sub Total",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lbl_SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_SubTotal=ttk.Entry(Buttom_Frame,textvariable=self.sub_total,font=("times new roman",16,"bold"),width=15)
        self.entry_SubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Buttom_Frame,text="Tax",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_tax=ttk.Entry(Buttom_Frame,textvariable=self.tax_input,font=("times new roman",16,"bold"),width=15)
        self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbl_Amount=Label(Buttom_Frame,text="Total",font=("times new roman",14,"bold"),bg="white",fg="black")
        self.lbl_Amount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_Amount=ttk.Entry(Buttom_Frame,textvariable=self.total,font=("times new roman",16,"bold"),width=15)
        self.entry_Amount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button
        Btn_Frame=Frame(Buttom_Frame,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=2)

        self.Btnsave=Button(Btn_Frame,command=self.save_bill,text="Save",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.Btnsave.grid(row=0,column=3)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=4)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=5)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=('areal',15,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=6)
        self.welcome()

        self.l=[]
    # ==========================================function declaration

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to Wmart")
        self.textarea.insert(END,f"\n BILL Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email : {self.c_email.get()}")

        self.textarea.insert(END,"\n ========================================")
        self.textarea.insert(END,f"\n Products\t\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n =======================================\n")

    def AddItem(self):
        Tax=2
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product")
        else:
            self.textarea.insert(END,f'\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}')
            self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
            

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add Product to cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n\n ========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no :{self.bill_no.get()} saved sucessfully...")

            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_email.set("")
        self.c_phone.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        


    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)

    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Pant":
            self.Combo_Product.config(value=self.Pant)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Tshirt":
            self.Combo_Product.config(value=self.Tshirt)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Shirt":
            self.Combo_Product.config(value=self.shirt)
            self.Combo_Product.current(0)
            

        # Lifestyle
        if self.Combo_SubCategory.get()=="Bath Soap":
            self.Combo_Product.config(value=self.Bath_Soap)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Face Wash":
            self.Combo_Product.config(value=self.Face_Wash)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Hair Oil":
            self.Combo_Product.config(value=self.Hair_Oil)
            self.Combo_Product.current(0)

        # Mobile ["Iphone","Samsung","RealMe","OnePlus"]
        if self.Combo_SubCategory.get()=="Iphone":
            self.Combo_Product.config(value=self.Iphone)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Samsung":
            self.Combo_Product.config(value=self.Samsung)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="RealMe":
            self.Combo_Product.config(value=self.RealMe)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="OnePlus":
            self.Combo_Product.config(value=self.OnePlus)
            self.Combo_Product.current(0)
    
    def price(self,event=""):
    # Pant
        if self.Combo_Product.get()=="Levis":
            self.Combo_Price.config(value=self.price_levis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Mufti":
            self.Combo_Price.config(value=self.price_Mufti)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Spykar":
            self.Combo_Price.config(value=self.price_spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Tshirt "Polo","Rodster","Jack&Jones"
        if self.Combo_Product.get()=="Polo":
            self.Combo_Price.config(value=self.price_spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Rodster":
            self.Combo_Price.config(value=self.price_spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Jack&Jones":
            self.Combo_Price.config(value=self.price_JackJones)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Shirts "Peter England","Louis Philipe","Park Avenue"

        if self.Combo_Product.get()=="Peter England":
            self.Combo_Price.config(value=self.price_Peter)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Louis Philipe":
            self.Combo_Price.config(value=self.price_Louis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Park Avenue":
            self.Combo_Price.config(value=self.price_Park)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        # Soap "Lifeboy","Lux","Santoor"

        if self.Combo_Product.get()=="Lifeboy":
            self.Combo_Price.config(value=self.price_Lifeboy)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Lux":
            self.Combo_Price.config(value=self.price_Lux)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="Santoor":
            self.Combo_Price.config(value=self.price_Santoor)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # facewash "Fair&Lovely","Fair&Handsome","MamaEarth"

        if self.Combo_Product.get()=="Fair&Lovely":
            self.Combo_Price.config(value=self.price_FairLovely)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Fair&Handsome":
            self.Combo_Price.config(value=self.price_FairHandsome)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="MamaEarth":
            self.Combo_Price.config(value=self.price_MamaEarth)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Oil "Parachute","Jasmin","Bajaj"

        if self.Combo_Product.get()=="Parachute":
            self.Combo_Price.config(value=self.price_Parachute)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Jasmin":
            self.Combo_Price.config(value=self.price_Jasmin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Bajaj":
            self.Combo_Price.config(value=self.price_Bajaj)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Iphone "IphoneX","Iphone_11","Iphone_12"


        if self.Combo_Product.get()=="IphoneX":
            self.Combo_Price.config(value=self.price_Iphone)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Iphone_11":
            self.Combo_Price.config(value=self.price_Iphone_11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Iphone_12":
            self.Combo_Price.config(value=self.price_Iphone_12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #samsung "Samsung M16","Samsung M12","Samsung M21"

        if self.Combo_Product.get()=="Samsung M16":
            self.Combo_Price.config(value=self.price_sm16)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Samsung M12":
            self.Combo_Price.config(value=self.price_sm12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Samsung M21":
            self.Combo_Price.config(value=self.price_sm21)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # realme "RealMe 12","RealMe 13","RealMe 20"

        if self.Combo_Product.get()=="RealMe 12":
            self.Combo_Price.config(value=self.price_r11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="RealMe 13":
            self.Combo_Price.config(value=self.price_r13)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="RealMe 20":
            self.Combo_Price.config(value=self.price_r20)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # "OnePlus7","OnePlus9","OnePlus10"

        if self.Combo_Product.get()=="OnePlus7":
            self.Combo_Price.config(value=self.price_one7)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="OnePlus9":
            self.Combo_Price.config(value=self.price_one9)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="OnePlus10":
            self.Combo_Price.config(value=self.price_one10)
            self.Combo_Price.current(0)
            self.qty.set(1)



















if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

