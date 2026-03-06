name="VikRam"

print(name.upper())
print(name.lower())

title="pYthon ProGRamMing"
print(title.title())

mobile="1234567890"
print(mobile[:2]+"******"+mobile[-2:])

location="Bangalore"
replacedArea= location.replace("Bangalore","Mysore")
print(replacedArea)

uber_id="Hi, This is your Uber Id is: UB12342.Please does share others."

id=uber_id.split(":")[1].split(".")[0].strip()
print(id)

zomota = "zomota is provide the coupen code for Zomota100"

if "Zomota100" in zomota:
    print("Zomota100 is available in the coupon.")

LovName="vikram swe"

initial="".join([name[0].upper() for name in LovName.split()])
print(initial)