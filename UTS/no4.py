# Program Perhitungan midpoint
# Oleh :  Isa Iman Muhammad
#         20051397019
#         2020A D4 Manajemen Informatika

print("Program Kalkulasi Midpoint")

print("Nilai midpoint dari garis : ")
def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    print(f'Midpoint x: {x}')
    print(f'Midpoint y: {y}')
    
midpoint(2, 2, 4, 4)