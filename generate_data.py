import csv, copy, time
from combinator import linked_list


####
#Define the data
###

#in rupiah
food = {
	"Nasi Goreng": 15000,
	"Indomie": 2000,
	"Bakso ayam": 12000,
	"Sate": 16000,
	"Rendang": 25000,
	"Sayur lodeh": 14000,
	"Gado Gado": 13000,
	"Rawon": 20000,
	"Ketoprak": 12500,
	"Siomay": 9000,
	"Seblak": 8000
	}
water = 1000 #rupiah / liter
electric = 900 #rupiah / kwh
internet = 1000 #rupiah / GB
clothes_wash = 10000 #rupiah / kg 

###
#generate the data
###

def main():
	water_pos = []
	electric_pos = []
	internet_pos = []
	cloth_pos = []
	i0, i1, i2, i3 = 0, 0, 0, 0
	for i in range(1, 11):
		water_pos.append(0.8+i0) #0.8 liter / day
		cloth_pos.append(0.9+i1) #0.9 kg / day
		internet_pos.append(200+i2)	#200mb / day
		electric_pos.append(10+i3) #10kwh / day
		i0+=0.2
		i1+=0.3
		i2+=150
		i3+=2.5

	with open("id_live_cost.csv", "w+") as fwrite:
		writer = csv.writer(fwrite)
		index = 0
		print("Generating...")
		try:
			while True:
				LL = linked_list(5)
				LL[0] += index
				combination = LL.get_data()
				f = list(food.keys())[int(combination[0])]
				w = water_pos[int(combination[1])]
				e = electric_pos[int(combination[2])]
				i = internet_pos[int(combination[3])]
				c = cloth_pos[int(combination[4])]
				price = food[f] + round(w*water, 2) + round(e*electric, 2) + round(i*internet, 2) + round(c*clothes_wash, 2)
				writer.writerow([f, format(w, ".2f"), format(e, ".2f"), format(i, ".2f"), format(c, ".2f"), price])
				index+=1
		except TypeError:
			pass
		print("Finish with %d lines"%(index))

if __name__=="__main__":
	main()
	

	
