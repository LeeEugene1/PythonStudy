jumin = "920921-1234567"#01234567~
print('성별: ',jumin[7])
print('연: ',jumin[0:2]) #0~2직전까지(0,1)
print('월: ',jumin[2:4])
print('일: ',jumin[4:6])

print('생년월일: ',jumin[:6])#처음부터 6직전까지
# print('뒤 7자리:', jumin[7:14])
print('뒤 7자리:', jumin[7:])#7부터 끝까지

#뒤에서부터 가져오기 ~-3-2-1
print('뒤 7자리(뒤에서부터)',jumin[-7:])