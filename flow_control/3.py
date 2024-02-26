# The code will print 'Product2' and 'Product not found!' as the second 
# time `bar_code_scanner is called it use a numeric type `142` which has no case

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)