import os

os.chdir('/Users/milenanapierala/Desktop/PROJECTS/FILES/videos')

for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    # print(f_name)

    f_num, f_title = f_name.split('-')
    # print(f_num)
    f_title = f_title.strip() #zeby usunąć odstępy między słowami, jeśli są
    f_num = f_num.strip().zfill(2)

    # print('{}-{}'.format(f_num, f_title, f_ext))
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    print(new_name)

    os.rename(f, new_name)
