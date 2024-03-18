# class employee:
#     employees = []

#     def add_employee(self, name, id, gender, age):
#         employee.employees.append({'name':name, 'id':id, 'gender':gender, 'age':age})

#     def get_employee_more_than_25(self):
#         result = []
#         for emp in employee.employees:
#             if emp.get('age') > 25:
#                 result.append(emp.get('name'))
#         return result

#     def get_male_and_female_count(self):
#         male_count = 0
#         female_count = 0

#         for emp in employee.employees:
#             if emp.get('gender') == 'male':
#                 male_count += 1
#             elif emp.get('gender') == 'female':
#                 female_count += 1

#         return {'male':male_count, 'female':female_count}

# emp = employee()
# emp.add_employee('meghanth',123,'male',26)
# emp.add_employee('suma',124,'female',22)
# emp.add_employee('megha',125,'female',27)
# emp.add_employee('meghu',126,'male',21)

# print(emp.get_employee_more_than_25())
# print(emp.get_male_and_female_count())



# d={'Ravi':{"id":123,"gender":"male","age":25},'Suma':{"id":124,"gender":"female","age":26}}

# result = {k:v for k,v in d.items() if v.get('gender') }
# print(result)




# class employe:
#     emp={}
#     def __init__(self,name,id,gender,age) -> None:
#         self.name=name
#         self.id=id
#         self.gender=gender
#         self.age=age
#         self.emp[str(id)]={"name":self.name,"gender":self.gender,"age":self.age}

#     def get_empy_details(self):
#         return self.emp
    
#     def male_femal(self):
#         feml_count=0
#         mal_count=0
#         for i,j in self.emp.items():
#             if j["gender"]=="Female":
#                 feml_count+=1
#             elif j["gender"]=="Male":
#                 mal_count+=1

#         return f"Female count : {feml_count} , Male count : {mal_count}"

#     def def_above_25(self):
#         res={}
#         for i,j in self.emp.items():
#             if j.get('age')>24:
#                 res[i]=j
#         return res


    
# obj1=employe("Meghu",100,"Male",27)
# obj2=employe("suma",101,"Female",21)
# print(obj1.get_empy_details())
# print(obj1.male_femal())
# print(obj1.def_above_25())


# l=[1,2,3]
# print(dir(l))

# def gene_():
#     a=[1,2,3,4]
#     i=0
#     while True:
#         yield a[i]
#         i+=1
# x=gene_()
# print(next(x))
# print(next(x))


# d1={"one":"a","two":'b',"three":"c"}
# d2={"four":"d","five":"e","one":'f'}
# for i in d2:
#     if(i in d1):
#         d1[i]=[d1[i],d2[i]]
#     else:
# #         d1[i]=d2[i]
# # print(d1)
# n=10
# a=0
# b=1
# for i in range(0,n-2):


# d={"a":1,"b":2}
# for i in d:
#     if d[i]%2==0:
#         print(i)


# class a:
#     def __init__(self):
#         self.hello()

#     def hello(self):
#         print("hello")

# obj = a()