import CA
import CADrawer


ca = CA.CA(30, 150)
ca.start_single()
ca.loop(149)
#drawer = CADrawer.PyplotDrawer()
#drawer.draw(ca)
#drawer.show()

array = ca.get_array()

for i in array[:, 150]:
    print(i)
