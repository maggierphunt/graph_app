import arabic_reshaper
from bidi.algorithm import get_display
print("إسمي ماجي"); #translation: 'my name is Maggie' - prints backwards and disjointed
print ("يجام يمسإ"); #'my name is Maggie', typed bacwards so prints right way, still disjointed

my_text = "إسمي ماجي";
reshaped_text = arabic_reshaper.reshape(my_text);    # correct its shape - links the letters
print(reshaped_text); #joined up forms of the letters, but still going in the wrong direction
bidi_text = get_display(reshaped_text);           # correct its direction - right to left
print(bidi_text);

bidi_text_2= get_display("hiya");
print (bidi_text_2); # does not redirect Roman alphabet


def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer # 3
returned_value = add_two_numbers_and_return_value()
print (returned_value)