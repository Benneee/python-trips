#--
# ToDos
# Create the text from the msg variable: "1 Welcome Ring To Tyler"
# Reverse the text created

msg='welcome to Python 101: Strings'
num = msg[20];
welcome_text = msg[:7];
ring_text = msg[-5:-1]
to_text = msg[8:10]
name = msg[8]+msg[12]+msg[2]+msg[1]+msg[-5]

sentence = num + ' ' + welcome_text + ' ' + ring_text + ' ' + to_text + ' ' + name
# print(sentence.title())

# reversing the text
print(sentence[::-1]);
