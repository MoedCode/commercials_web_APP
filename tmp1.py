def get_img_list(self):
    print(self["img_list"])
    return [] if not self.get('img_list') else self['img_list'].split(",")

x = {'img_list':"dam, you" , 'B':True}
m = get_img_list(x)
print(m)

def set_img_list(value):
     return ",".join(value) if value else ""

print(set_img_list(m))