import torch


x = torch.rand(5,3)
print(x)

x = x.new_ones(5, 3, dtype=torch.float)      
# new_* methods take in sizes

x = torch.randn_like(x, dtype=torch.float)    
# override dtype!
print("x=%s" %x)                                      
# result has the same size
print(x.size())

y = torch.rand(5, 3)
print("y=%s" %y) 
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print("x+y=%s" %result) 