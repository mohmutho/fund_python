# new_list = [] jika codenya ditaruh disini, ada side effect
# kalo bisa jangan biar functionsnya lebih pure.
# tidak memiliki side effect
def mutiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return  new_list

mutiply_by2([1,2,3])
# NB : Kalo secara garis besar data harus terpisah dengan
# pure functions