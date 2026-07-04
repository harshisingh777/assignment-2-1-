class Observer:
    def update(self,s,m): raise NotImplementedError
class EmailNotifier(Observer):
    def update(self,s,m): print('Email',s,m)
class AuditLogNotifier(Observer):
    def update(self,s,m): print('Audit',s,m)
class MarksUpdateNotifier:
    def __init__(self): self.obs=[]
    def register(self,o): self.obs.append(o)
    def deregister(self,o): self.obs.remove(o)
    def notify(self,s,m):
        for o in list(self.obs): o.update(s,m)
if __name__=='__main__':
 n=MarksUpdateNotifier();e=EmailNotifier();a=AuditLogNotifier();n.register(e);n.register(a);n.notify(1,90);n.deregister(e);n.notify(1,95)
