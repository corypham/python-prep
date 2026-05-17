# variable scope: where a var is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> built-in

y = 67

def func1():
  a = 1
  def func2():
    a = 2
    print(a)


func1()