class Admin(object):
    def __init__(self, nama='', password=''):
        self.nama=nama
        self.password=password

    def setAdmin(self, name,passw):
        self.nama = name
        self.password=passw
    
    def cek(self):
        if self.nama =='user' and self.password =='user':
            return True
        else:
            return False