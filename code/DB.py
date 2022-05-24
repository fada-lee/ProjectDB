
import pymysql
from tkinter import messagebox
from datetime import datetime

class DB_connect:

    global con,cur 
    con = pymysql.connect(host='localhost',user='root',password='04122543',database='dormitory')
    cur = con.cursor()
    

    def Register(student_id,fname,lname,password,email,phone):                  
        query=("select*from students where student_id=%s")
        value=(student_id,)
        cur.execute(query,value)
        row= cur.fetchone()
        if row != None:
            messagebox.showerror("Error","User already Exist, Please try with another StudentId")
        
        else:
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s)" ,\
                    (student_id ,fname,lname, password,\
                    email,phone))                     
            con.commit()            
            

    def Login(student_id,password):          
        query=("select*from students where student_id=%s and password=%s")
        value=(student_id,password)
        cur.execute(query,value)            
        row= cur.fetchone()
        return row


    def forgot_pass(student_id):
        query=("select*from students where student_id=%s")
        value = (student_id,)
        cur.execute(query,value)
        row = cur.fetchone()
        return row

    #========================== ข้อมูล Students =========================================================
    def name(student_id):
        query=("""SELECT student_id, 
	                concat(Upper(substr(fname,1,1)), Lower(substr(fname,2,LENGTH(fname)))),
                    concat(Upper(substr(lname,1,1)), Lower(substr(lname,2,LENGTH(lname)))),
                    password, email, concat(substr(Phone,1,3),'-',substr(phone,4,3),'-',substr(phone,7,10))                    
                    from students where student_id =%s""")
        value=(student_id)
        cur.execute(query,value)  
        row= cur.fetchone()
        return row

    #====================== ค้นหา Booking_ID ===============================

    def bookingid(student_id):
        query = """SELECT booking_id from bookings 
                    natural join students 
                    where student_id = %s
                    and CheckOut > curdate()                   
                    """
        value = (student_id)
        cur.execute(query,value)
        booking_id = cur.fetchone()
        return booking_id

    #========================== Functions in Booking ========================
    
    def getdorm(): #ค้นหาหอพัก
        query = """select Upper(dormitory_name)
                from dormitories"""
        cur.execute(query)
        row = cur.fetchall()
        return row

    def getroomtype(dn): #ค้นหาประเภทห้อง
        query = '''select distinct(room_type)
				from buildings 
                where dormitory_name =%s'''
        cur.execute(query,dn)
        row = cur.fetchall()
        return row

    def getbuilding(dn,rt): #ค้นหาอาคารจากชื่อหอกับประเภท
        query = '''select distinct( Upper(substr(Building_Name,(LENGTH(Building_Name)))))
				from buildings
                where dormitory_name = %s and room_type = %s '''
        cur.execute(query,(dn,rt))
        row = cur.fetchall()
        return row

    def findroom(dormname,roomtype,bd): #ค้นหาห้องว่าง
        cur.execute("""select Room_number from buildings natural join rooms  
                        where dormitory_name = %s and room_type = %s and Building_Name = %s
                        and room_status = 'v'""",(dormname,roomtype,bd))
        findrooms = cur.fetchall()
        return findrooms  


    #ใช้ def name() เพื่อแสดงข้อมูลนักเรียน

    def dataroom(dormname,roomtype): #แสดงข้อมูลห้องพัก
        cur.execute("""select Room_price, Power_p_u, Water_p_u  
                    from buildings natural join dormitories 
                    where Building_Name = %s and 
                    room_type = %s;""",(dormname,roomtype))
        pr_powwat = cur.fetchall()
        return pr_powwat

    def location(building_name): #แสดงข้อมูลห้องพัก
        cur.execute("""select Location from dormitories 
                    natural join  buildings
                    where building_name = %s """,(building_name))
        location = cur.fetchall()
        return location


    #-----บันทึกข้อมูลลงดาต้าเบส----------------
    def insertbookings(bkid,date_booking,checkIN,checkOut,stuid,buildingname,numroom):
        cur.execute("insert into bookings values(%s,%s,%s,%s,%s,%s,%s)",
                    (bkid,date_booking,checkIN,checkOut,stuid,buildingname,numroom))
        cur.execute("""update rooms set room_status = 'o' 
                        where Building_Name = %s and 
                        room_number = %s""",(buildingname,numroom))
        con.commit()
    
    #========================== Functions in Repairs ========================
    #ใช้ def bookingid() เพื่อหา booking_id

    def dormitory(booking_id): #แสดงข้อมูลหอพัก
        query = ("""select Upper(substr(r.Building_Name,1,(LENGTH(r.Building_Name)-1))),
                    Upper(substr(r.Building_Name,(LENGTH(r.Building_Name)))),
                    r.room_floor, r.room_number 
                    from  bookings b  natural join rooms r
                    where b.booking_id =%s 
                    """)
        value=(booking_id)
        cur.execute(query,value)
        row= cur.fetchone()
        return row

    #-----บันทึกข้อมูลลงดาต้าเบส----------------
    def insertrepair(booking_id,Repair_id,textrep,date_Re):
        if textrep == '':
            messagebox.showerror("Error","All field required")
            return 2
        else:
            query = ("""Select Upper(r.Building_Name), r.room_number 
                        from  bookings b natural join rooms r 
                        where booking_id =%s 
                        """)
            value=(booking_id)
            cur.execute(query,value)
            row = cur.fetchone()
            building = row[0]
            room_number = row[1]
            cur.execute("insert into repairs values(%s,%s,%s,%s,%s,0,'unpaid',null)" ,
                            (Repair_id,date_Re,textrep, building,room_number))
            con.commit()
            open_home = messagebox.askyesno('Success' ,'Report a successful repair.\nGo back home?')
            return open_home
    
    #========================== Functions in Repairs ========================
    #ใช้ def bookingid() เพื่อหา booking_id

    def dormitory(booking_id): #แสดงข้อมูลหอพัก
        query = ("""select Upper(substr(r.Building_Name,1,(LENGTH(r.Building_Name)-1))),
                    Upper(substr(r.Building_Name,(LENGTH(r.Building_Name)))),
                    r.room_floor, r.room_number 
                    from  bookings b  natural join rooms r
                    where b.booking_id =%s 
                    """)
        value=(booking_id)
        cur.execute(query,value)
        row= cur.fetchone()
        return row

    #-----บันทึกข้อมูลลงดาต้าเบส----------------
    def insertrepair(booking_id,Repair_id,textrep,date_Re):
        if textrep == '':
            messagebox.showerror("Error","All field required")
            return 2
        else:
            query = ("""Select Upper(r.Building_Name), r.room_number 
                        from  bookings b natural join rooms r 
                        where booking_id =%s 
                        """)
            value=(booking_id)
            cur.execute(query,value)
            row = cur.fetchone()
            building = row[0]
            room_number = row[1]
            cur.execute("insert into repairs values(%s,%s,%s,%s,%s,0,'unpaid',null)" ,
                            (Repair_id,date_Re,textrep, building,room_number))
            con.commit()
            open_home = messagebox.askyesno('Success' ,'Report a successful repair.\nGo back home?')
            return open_home

    #========================== Functions in Bills ========================
    #ใช้ def bookingid() เพื่อหา booking_id
    
    def repairid(stuid): #ค้นหาดูว่ามีการแจ้งซ่อมไหมแล้วยังไม่จ่ายเงินไหม
        query = """select repair_id
                    from bookings natural join repairs
                    where repair_status = 'unpaid' 
                    and Student_id = %s """
        value = (stuid)
        cur.execute(query,value)
        row = cur.fetchall()
        return row

    def repair(stuid): #ค้นหาดูว่ามีการแจ้งซ่อมไหมแล้วยังไม่จ่ายเงินไหม
        query = """select sum(repair_price)
                    from bookings natural join repairs
                    where repair_status = 'unpaid' 
                    and Student_id = %s """
        value = (stuid)
        cur.execute(query,value)
        row = cur.fetchall()
        return row

    def bills(booking_id): #ค้นหาบิลที่ยังไม่ชำระ
        query=("""select Bill_No, date_format(Bill_date, '%%M %%Y'), 
                        Water_old, Water_new, Power_old, Power_new, Bill_status,
                        concat(Upper(substr(fname,1,1)), Lower(substr(fname,2,LENGTH(fname))),
                        ' ', Upper(substr(lname,1,1)), Lower(substr(lname,2,LENGTH(lname)))),
                        Lower(gender)
                        from bills natural join bookings natural join employees 
                        where Bill_status = 'unpaid' and booking_id = %s
                        """)
        value = (booking_id)
        cur.execute(query,value)
        row = cur.fetchall()
        return row


    #ใช้ def name() เพื่อแสดงข้อมูลนักเรียน

    def room(booking_id): #หาข้อมูลห้องที่อยู่
        query = """select room_floor, room_number, room_price
                    from rooms  natural join buildings
                    natural join bookings 
                    where booking_id = %s 
                    """
        value = (booking_id)
        cur.execute(query,value)
        row = cur.fetchone()
        return row

    def billmonth(Booking_id): #เดือนที่จ่ายแล้ว
        query = """SELECT date_format(bill_date,"%%M"), 
                date_format(bill_date,"%%Y") 
                FROM bills 
                natural join rooms 
                natural join bookings 
                where booking_id =%s 
                and Bill_status='paid'
                order by bill_date desc
                LIMIT 3"""
        value = (Booking_id)
        cur.execute(query,value)
        billtext =  cur.fetchall()
        return billtext

    def dormdata(booking_id): #ข้อมูลหอพัก
        cur.execute("""SELECT d.Bank, d.Bank_no, Upper(d.dormitory_name), 
                        d.Location, concat(substr(Tel,1,3),'-',substr(Tel,4,3),
                        '-',substr(Tel,7,10)), d.Water_p_u, d.Power_p_u, 
                        b.Bank_name, upper(substr(Building_name,LENGTH(Building_Name)))
                        FROM dormitories d
                        natural join banks b
                        natural join bookings bk
                        natural join buildings
                        where Booking_id = %s""", booking_id )
        #(Bank, Bank_no, dormitory_name, Location, Tel, Water_p_u, Power_p_u, Bank_name)
        row = cur.fetchall()
        return row

    #บันทึกข้อมูลลงดาต้าเบส
    def insertpaymemt(payid,paydate,stuid,billid,filename,total,repairid):
        
        #//ไม่มีการแจ้งซ่อม
        if repairid ==():
            cur.execute("insert into payments values(%s,%s,%s,%s,%s,%s)" ,
                    (payid,paydate,stuid,billid,filename,total))
            cur.execute("update bills set bill_status = 'paid' where bill_no = %s",billid)
            con.commit()

        else:
            #//มีการแจ้งซ่อม
            cur.execute("insert into payments values(%s,%s,%s,%s,%s,%s)" ,
                    (payid,paydate,stuid,billid,filename,total))
            cur.execute("update bills set bill_status = 'paid' where bill_no = %s",billid)
            for i in range(len(repairid)):
                query = """update repairs
                            set repair_status = 'paid', 
                                pay_id =%s
                            where repair_id = %s"""
                value = (payid,repairid[i])
                cur.execute(query,value)
                cur.fetchall()
            con.commit()
        open_home = messagebox.askyesno('SUCCESS' ,'Report a successful payment.\nGo back home?')
        return open_home




    def billhistory(bookingid,month): #ประวัติการจ่ายบิล
        query=("""select Bill_No, date_format(Bill_date, '%%M %%Y'), 
                        Water_old, Water_new, Power_old, Power_new, Bill_status,
                        concat(Upper(substr(fname,1,1)), Lower(substr(fname,2,LENGTH(fname))),
                        ' ', Upper(substr(lname,1,1)), Lower(substr(lname,2,LENGTH(lname)))),
                        Lower(gender)
                        from bills natural join bookings natural join employees
                        where Bill_status = 'paid' 
                        and Booking_id = %s
                        and date_format(Bill_date, '%%M %%Y') =%s
                        """)
        values = (bookingid,month)
        cur.execute(query,values)
        row = cur.fetchall()
        return row

    def repairhistory(month): #ประวัติการชำระของการซ่อม
        query = """select sum(repair_price) from repairs 
                    natural join bills 
                    where date_format(Bill_date, '%%M %%Y') = %s"""
        value = (month)
        cur.execute(query,value)
        row =  cur.fetchall()
        return row    
    
    #========================== Functions in Profile ========================
    #ใช้ def name() เพื่อแสดงข้อมูลนักเรียน
    #บันทึกข้อมูลลงดาต้าเบส
    def updateprofile(student_id,fname,lname,password,email,phone):
                query = """update students
                            set fname = %s,
                                lname = %s,
                                password = %s, 
                                email = %s,
                                phone = %s
                                where student_id = %s
                        """
                values = (fname,lname,password,email,phone,student_id)
                cur.execute(query,values)
                con.commit()
                cur.fetchall()
                
    #========================== Functions in Upbooking ========================
    #ใช้ def name() เพื่อแสดงข้อมูลนักเรียน
    #ใช้ def bookingid() เพื่อหา booking_id
    #ใช้ def room() หาข้อมูลห้องที่อยู่
    #ใช้ def dormitory() แสดงข้อมูลหอพัก

    #แสดงวันที่checin checkout
    def showbookdate(booking_id):
        query = """select date_format(checkin,'%%d'), 
                    date_format(checkin,'%%m') , 
                    date_format(checkin,'%%Y') ,
                    date_format(checkout,'%%d'),
                    date_format(checkout,'%%m'),
                    date_format(checkout,'%%Y')
                    from bookings 
                    natural join rooms
                    where booking_id = %s                
                    """
        value = (booking_id)
        cur.execute(query,value)
        row = cur.fetchone()
        return row

    #บันทึกลงดาต้าเบส
    def updatebooking(ceckin,checkout,booking_id):
        query = """UPDATE bookings 
                    SET CheckIn = %s, 
	                CheckOut = %s 
                    WHERE (Booking_id = %s)
                """
        values = (ceckin,checkout,booking_id)
        cur.execute(query,values)
        cur.fetchall()
        con.commit()
            

    #บันถึงวันที่เช็คเอ้าลงดาต้าเบส
    def checkOut(dorm,room,booking_id):
        query1 = """UPDATE rooms
                    SET room_status = 'v'
                    WHERE (Building_Name = %s and 
                    room_number =%s)
                """
        values = (dorm,room)
        cur.execute(query1,values)
        cur.fetchall()

        query2 = """update bookings 
                 set CheckOut = CURDATE()
                    where booking_id = %s;
                """
        value = (booking_id)
        cur.execute(query2,value)
        cur.fetchall()
        con.commit()


    #========================== Functions in Payments ========================
    #ใช้ def name() เพื่อแสดงข้อมูลนักเรียน
    #ใช้ def bookingid() เพื่อหา booking_id
    #ใช้ def room() หาข้อมูลห้องที่อยู่
    #ใช้ def dormdata() แสดงข้อมูลหอพัก
    #ใช้ def bills() และ def repair() เพื่อรวมยอดชำระ
    

    def showRepair(bookingid):
        query = """select repair_date, repair_name,
                    repair_price, repair_status
                    from repairs 
                    natural join bookings
                    where booking_id = %s
                    order by repair_date desc
                    limit 10"""
        value = (bookingid)
        cur.execute(query,value)
        row =  cur.fetchall()
        return row    


#student_id,fname,lname,password,email,phone





     


    
